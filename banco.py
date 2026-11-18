import json
from pathlib import Path
import duckdb
import pandas as pd

BASE = Path(__file__).parent
obj = json.loads((BASE / 'dados' / 'original.json').read_text(encoding='utf-8'))
df = pd.DataFrame(obj['daily']).rename(columns={
    'time': 'data', 'temperature_2m_min': 'temperatura_min_c',
    'temperature_2m_max': 'temperatura_max_c', 'precipitation_sum': 'precipitacao_mm'
})
df['data'] = pd.to_datetime(df['data'], errors='raise')
for campo in ['temperatura_min_c', 'temperatura_max_c', 'precipitacao_mm']:
    df[campo] = pd.to_numeric(df[campo], errors='coerce')
assert len(df) == 30, 'Esperados 30 registros'
assert df['data'].nunique() == 30, 'Datas ausentes ou duplicadas'
assert df['data'].min() == pd.Timestamp('2026-09-01')
assert df['data'].max() == pd.Timestamp('2026-09-30')
assert not df.isna().any().any(), 'Existem valores ausentes: revisar antes da carga'
assert (df['temperatura_min_c'] <= df['temperatura_max_c']).all()
assert (df['precipitacao_mm'] >= 0).all()
df['localidade'] = 'Campinas-SP'
df.to_csv(BASE / 'dados' / 'tratados.csv', index=False)
con = duckdb.connect(str(BASE / 'dados' / 'clima.duckdb'))
con.execute('''CREATE TABLE IF NOT EXISTS clima_diario (
    data DATE PRIMARY KEY, localidade VARCHAR, temperatura_min_c DOUBLE,
    temperatura_max_c DOUBLE, precipitacao_mm DOUBLE)''')
con.register('dados_novos', df)
con.execute('''INSERT OR REPLACE INTO clima_diario
    SELECT CAST(data AS DATE), localidade, temperatura_min_c, temperatura_max_c, precipitacao_mm FROM dados_novos''')
print('Registros no banco:', con.execute('SELECT COUNT(*) FROM clima_diario').fetchone()[0])
con.close()

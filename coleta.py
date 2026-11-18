import json
from datetime import datetime, timezone
from pathlib import Path
import requests

PASTA = Path(__file__).parent / 'dados'
PASTA.mkdir(exist_ok=True)
PARAMETROS = {
    'latitude': -22.9056, 'longitude': -47.0608,
    'start_date': '2026-09-01', 'end_date': '2026-09-30',
    'daily': 'temperature_2m_min,temperature_2m_max,precipitation_sum',
    'timezone': 'America/Sao_Paulo'
}
resposta = requests.get('https://archive-api.open-meteo.com/v1/archive', params=PARAMETROS, timeout=60)
resposta.raise_for_status()
dados = resposta.json()
if 'daily' not in dados:
    raise ValueError('Resposta da API sem dados diarios')
(PASTA / 'original.json').write_text(json.dumps(dados, indent=2, ensure_ascii=False), encoding='utf-8')
(PASTA / 'metadados_coleta.json').write_text(json.dumps({'coletado_em_utc': datetime.now(timezone.utc).isoformat(), 'url': resposta.url, 'parametros': PARAMETROS}, indent=2, ensure_ascii=False), encoding='utf-8')
print('Coleta concluída:', len(dados['daily']['time']), 'dias; JSON preservado.')

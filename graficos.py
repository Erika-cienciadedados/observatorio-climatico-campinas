import duckdb
import matplotlib.pyplot as plt
from pathlib import Path

pasta = Path("docs")
pasta.mkdir(exist_ok=True)

con = duckdb.connect("dados/clima.duckdb", read_only=True)
df = con.execute("""
    SELECT data, temperatura_min_c, temperatura_max_c, precipitacao_mm
    FROM clima_diario
    ORDER BY data
""").df()
con.close()

df["data"] = df["data"].astype(str)

plt.figure(figsize=(12, 5))
plt.plot(df["data"], df["temperatura_min_c"], label="Minima")
plt.plot(df["data"], df["temperatura_max_c"], label="Maxima")
plt.title("Temperaturas diarias - Campinas - Setembro de 2026")
plt.xlabel("Data")
plt.ylabel("Temperatura (C)")
plt.xticks(rotation=60)
plt.legend()
plt.tight_layout()
plt.savefig(pasta / "grafico_temperaturas.png", dpi=150)
plt.close()

plt.figure(figsize=(12, 5))
plt.bar(df["data"], df["precipitacao_mm"])
plt.title("Precipitacao diaria - Campinas - Setembro de 2026")
plt.xlabel("Data")
plt.ylabel("Precipitacao (mm)")
plt.xticks(rotation=60)
plt.tight_layout()
plt.savefig(pasta / "grafico_chuvas.png", dpi=150)
plt.close()

print("Graficos criados com sucesso na pasta docs!")

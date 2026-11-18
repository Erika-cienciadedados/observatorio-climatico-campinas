# Observatório Climático de Campinas (SP)

## Projeto Integrador — Ciência de Dados

### 1. Apresentação
Este projeto tem como objetivo analisar dados climáticos do município de Campinas (SP), utilizando ferramentas de Ciência de Dados para organizar, armazenar, consultar e visualizar informações sobre temperaturas e precipitação.

O estudo considera 30 registros diários referentes a setembro de 2026.

### 2. Objetivos
- Coletar e organizar dados climáticos.
- Armazenar as informações em um banco de dados.
- Realizar consultas utilizando SQL.
- Identificar variações de temperatura e precipitação.
- Apresentar os resultados por meio de gráficos.

### 3. Tecnologias utilizadas
- **Python:** processamento e automação.
- **Pandas:** manipulação dos dados.
- **DuckDB:** armazenamento e consultas.
- **SQL:** análise das informações.
- **Matplotlib:** criação dos gráficos.
- **GitHub:** documentação e disponibilização do projeto.

### 4. Metodologia
O projeto foi desenvolvido em etapas: coleta de dados, organização dos registros, armazenamento no DuckDB, consultas SQL e elaboração de gráficos.

### 5. Resultados
A análise dos 30 registros apresentou:

- Temperatura mínima média: **15,68 °C**
- Temperatura máxima média: **25,05 °C**
- Precipitação acumulada: **202,0 mm**
- Maior temperatura máxima registrada: **33,2 °C**, em 29/09/2026.
- Maior precipitação diária registrada: **33,0 mm**, em 12/09/2026.

### 6. Visualização dos dados

**Gráfico de temperaturas**

![Gráfico de temperaturas](grafico_temperaturas.png)

**Gráfico de precipitação**

![Gráfico de precipitação](grafico_chuvas.png)

### 7. Arquivos do projeto
- `coleta.py` — coleta dos dados.
- `banco.py` — armazenamento no banco de dados.
- `consultas.sql` — consultas SQL.
- `graficos.py` — geração dos gráficos.
- `requirements.txt` — dependências do projeto.

### 8. Conclusão
O projeto demonstra a aplicação de ferramentas de Ciência de Dados na análise de informações climáticas, permitindo identificar variações de temperatura e precipitação no período estudado.

Os resultados podem servir como base para estudos posteriores e para ampliar a compreensão das condições climáticas de Campinas (SP).

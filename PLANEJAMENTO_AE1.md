# AE1 — Planejamento do Observatório Climático Local

**Título:** Observatório Climático Local: temperaturas e precipitação em Campinas/SP, setembro de 2026.

**Problema:** Dados históricos sobre temperatura e precipitação nem sempre são apresentados de maneira simples para a comunidade. Como organizá-los em indicadores acessíveis para apoiar a compreensão das condições meteorológicas passadas?

**Público-alvo:** Moradores de Campinas, especialmente pessoas que planejam deslocamentos e atividades externas.

**Objetivo geral:** Coletar, tratar e analisar dados históricos de Campinas, convertendo-os em indicadores e gráficos de fácil interpretação.

**Recorte:** Campinas/SP (-22.9056, -47.0608), de 1 a 30 de setembro de 2026. Três variáveis: temperatura mínima diária, temperatura máxima diária e precipitação diária acumulada.

**Perguntas:** (1) Qual a temperatura máxima e em que dia ocorreu? (2) Quais os dias mais chuvosos? (3) Como variou a amplitude térmica diária?

**KPIs:** Média das máximas (°C); média das mínimas (°C); precipitação acumulada (mm).

**Visualizações propostas:** Série temporal de temperatura mínima/máxima; barras de precipitação diária.

**Método:** Coleta da API histórica Open-Meteo via Python Requests; tratamento e validação em pandas; armazenamento em DuckDB; consultas SQL; documentação no GitHub.

**Relevância extensionista:** Comunicar os achados históricos de forma acessível à comunidade, sem confundi-los com previsão meteorológica. Público e canal de devolutiva serão definidos antes da etapa final.

**Limitações:** Dados modelados/reanálise, não necessariamente medidos por estação local; apenas 30 dias, insuficientes para inferências sobre mudança climática.

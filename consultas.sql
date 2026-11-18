-- KPI 1: media das temperaturas maximas (graus Celsius)
SELECT ROUND(AVG(temperatura_max_c), 2) AS temperatura_maxima_media_c FROM clima_diario;
-- KPI 2: media das temperaturas minimas (graus Celsius)
SELECT ROUND(AVG(temperatura_min_c), 2) AS temperatura_minima_media_c FROM clima_diario;
-- KPI 3: precipitacao acumulada (milimetros)
SELECT ROUND(SUM(precipitacao_mm), 2) AS precipitacao_total_mm FROM clima_diario;
-- Pergunta 1: dia(s) de maior temperatura
SELECT data, temperatura_max_c FROM clima_diario WHERE temperatura_max_c = (SELECT MAX(temperatura_max_c) FROM clima_diario) ORDER BY data;
-- Pergunta 2: dias mais chuvosos (top 5)
SELECT data, precipitacao_mm FROM clima_diario ORDER BY precipitacao_mm DESC, data LIMIT 5;
-- Pergunta 3: amplitude termica diaria
SELECT data, ROUND(temperatura_max_c - temperatura_min_c, 2) AS amplitude_termica_c FROM clima_diario ORDER BY data;

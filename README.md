## Mission Control AI integrado com Solaris-1
GS2026.1 —> Soluções em energias renováveis e sustentáveis integrada com Pensamento Computacional e Automação com Python  

## *Equipe: Polaris* 

Ana Julia Yumi Inoue - RM: 569430

João Pedro Santos Ferreira - RM: 569202

Maria Fernanda Dias Ribeiro - RM: 569999

-----
### Missão (nave analisada): **Solaris-1**
-----

## Objetivo: 
desenvolver uma solução para monitoramento de sistemas energéticos em uma missão espacial experimental, aplicando conceitos de energia, potência, energias renováveis e sustentabilidade na análise de dados simulados dos módulos da operação.

Descrição do projeto
----------
O Mission Control AI integrado com Solaris-1 é um sistema de monitoramento operacional desenvolvido para acompanhar em tempo real as condições energéticas de uma missão espacial experimental. O Sistema acompanha os sensores da nave Solaris‑1 em 8 ciclos de missão, avaliando automaticamente cada leitura, emitindo alertas e sugerindo ações corretivas, com destaque para a energia solar como fonte renovável essencial da operação.

Onde entra Energias Renováveis? 
----- 
A missão Solaris-1 depende inteiramente de painéis fotovoltaicos (painéis solares) como fonte energia primária. O sistema monitora a geração solar em Watts a cada ciclo e detecta automaticamente quedas causadas por:

* Tempestades de partículas solares
* Falhas estruturais nos painéis
* Interferências eletromagnéticas

Isso conecta diretamente o projeto ao tema da disciplina: eficiência energética, fontes renováveis e sustentabilidade operacional.

-----------------
Estruturas de Dados
--------
Os dados da missão estão organizados em uma matriz chamada `dados_missao`.

Cada linha representa um ciclo da missão.

Cada coluna guarda uma informação específica:

* Temperatura (°C)

* Comunicação (%)

* Bateria (%)

* Oxigênio (%)

* Estabilidade (%)


Status da missão 
-----------
NORMAL  ATENÇÃO / CRÍTICO

----
Alertas 
----
### Temperatura:

< 18 °C ou > 30 °C → Atenção

35 °C → Crítico

### Comunicação:

< 30% → Crítico

30–59% → Atenção

≥ 60% → Normal

### Bateria:

< 20% → Crítico

20–49% → Atenção

≥ 50% → Normal

### Oxigênio:

< 80% → Crítico

80–89% → Atenção

≥ 90% → Normal

### Estabilidade:

< 40% → Crítico

40–69% → Atenção

≥ 70% → Normal

----
PONTUAÇÃO
----
O sistema transforma os estados dos sensores em pontos. Cada ciclo da missão recebe uma soma que indica o nível de risco:


### * Cada ciclo recebe uma pontuação pontos por sensor

0 = NORMAL

1 = ATENÇÃO

2 = CRÍTICO

*OBS: Como existem 5 sensores, o máximo possível por ciclo é 10 pontos.

---
Classificação final da missão:
---
Depois de somar os pontos de todos os sensores, o sistema classifica o ciclo:

Pontuação	 e Classificação

0 – 2      = missão estável 

3 - 5      = missão em atenção 

6 ou mais  = missão crítica 



-----
Exemplos de recomendações automáticas:
-----
“Acionar sistema de resfriamento dos painéis”

“Ativar modo de economia de energia”

“Verificar integridade dos painéis solares”



Exemplo Prático de Saída
----
Temperatura = Crítico (2 pontos)

Comunicação = Atenção (1 ponto)

Bateria = Crítico (2 pontos)

Oxigênio = Normal (0 pontos)

Estabilidade = Atenção (1 ponto)

Pontuação total = 6 pontos → Missão Crítica

---
FUNÇÃO e DESCRIÇÃO

`analisar_temperatura()`     =      Classifica a temperatura do módulo 

`analisar_comunicacao()`     =      Classifica a qualidade do sinal

`analisar_bateria()`         =      Classifica o nível de bateria 

`aanalisar_energia_solar()`        =      Classifica o nível de energia

`analisar_estabilidade()`    =      Classifica a estabilidade dos sistemas 

`calcular_risco_ciclo()`     =      Calcula a pontuação total do ciclo 

`classificar_ciclo()`        =      Retorna o status do ciclo pela pontuação 

`gerar_recomendacao()`       =      Gera recomendações automáticas por ciclo 

`analisar_tendencia()`       =      Compara o risco do 1º e último ciclos 

`identificar_area_mais_afetada()`  = Soma risco acumulado por área 

`exibir_ciclos()`                  = Exibe a análise detalhada de cada ciclo 

`gerar_relatorio_final()`          = Exibe o relatório consolidado da missão 



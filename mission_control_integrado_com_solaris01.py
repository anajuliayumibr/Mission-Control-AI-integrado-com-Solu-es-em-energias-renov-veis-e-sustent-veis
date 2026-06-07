# MISSION CONTROL AI — SOLARIS-1
# GS2026.1 - Soluções em Energias Renováveis e Sustentáveis

# Integrantes:
# Ana Julia Yumi Inoue     - RM: 569430
# João Pedro Santos Ferreira - RM: 569202
# Maria Fernanda Dias Ribeiro - RM: 569999


# INFORMAÇÕES DA MISSÃO
nome_missao = "Solaris-1"
nome_equipe = "Equipe Polaris - Ana Julia, João Pedro e Maria Fernanda"

# Matriz principal: cada linha = 1 ciclo
# Colunas: [temperatura (°C), comunicacao (%), bateria (%), energia_solar (W), estabilidade (%)]

dados_missao = [
    [21, 94, 91, 96, 99],  # Ciclo 01 - Lançamento e estabilização inicial
    [27, 83, 75, 95, 88],  # Ciclo 02 - Ajuste de trajetória
    [30, 66, 60, 92, 71],  # Ciclo 03 - Interferência solar leve
    [36, 45, 40, 88, 58],  # Ciclo 04 - Falha parcial no painel de energia
    [41, 20, 14, 8, 32],  # Ciclo 05 - Tempestade de partículas - risco crítico
    [33, 58, 35, 83, 52],  # Ciclo 06 - Protocolo de recuperação ativado
    [29, 72, 47, 88, 62],  # Ciclo 07 - Recuperação parcial dos sistemas
    [23, 88, 63, 93, 78],  # Ciclo 08 - Estabilização pós-crise
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de bateria",
    "Energia solar (painéis)",
    "Estabilidade operacional",
]


# FUNÇÕES DE ANÁLISE DOS SENSORES


def analisar_temperatura(valor):
    if valor > 80:
        return "CRÍTICO", 2, "Risco de superaquecimento severo"
    elif valor > 40:
        return "ATENÇÃO", 1, "Temperatura elevada — monitorar painéis"
    elif valor < 0:
        return "ATENÇÃO", 1, "Temperatura abaixo do ideal"
    else:
        return "NORMAL", 0, "Temperatura estável"

def analisar_comunicacao(valor):
    if valor < 20:
        return "CRÍTICO", 2, "Perda iminente de contato com a base"
    elif valor < 50:
        return "ATENÇÃO", 1, "Sinal instável — reorientar antena"
    else:
        return "NORMAL", 0, "Comunicação estável"

def analisar_bateria(valor):
    if valor < 15:
        return "CRÍTICO", 2, "Bateria em nível crítico"
    elif valor < 35:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Carga de bateria estável"

def analisar_energia_solar(valor):
    if valor < 15:
        return "CRÍTICO", 2, "Geração solar insuficiente para a missão"
    elif valor < 50:
        return "ATENÇÃO", 1, "Geração solar abaixo do esperado"
    else:
        return "NORMAL", 0, "Painéis solares operando normalmente"

def analisar_estabilidade(valor):
    if valor < 35:
        return "CRÍTICO", 2, "Estabilidade crítica — risco estrutural"
    elif valor < 65:
        return "ATENÇÃO", 1, "Estabilidade reduzida"
    else:
        return "NORMAL", 0, "Estabilidade adequada"


# FUNÇÕES DE LÓGICA E TOMADA DE DECISÃO

def calcular_risco_ciclo(ciclo):
    temperatura, comunicacao, bateria, energia_solar, estabilidade = ciclo
    _, pontos_temp, _ = analisar_temperatura(temperatura)
    _, pontos_com,  _ = analisar_comunicacao(comunicacao)
    _, pontos_bat,  _ = analisar_bateria(bateria)
    _, pontos_sol,  _ = analisar_energia_solar(energia_solar)
    _, pontos_est,  _ = analisar_estabilidade(estabilidade)
    return pontos_temp + pontos_com + pontos_bat + pontos_sol + pontos_est

def classificar_ciclo(pontuacao):
    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"

def gerar_recomendacao(ciclo):
    temperatura, comunicacao, bateria, energia_solar, estabilidade = ciclo
    recomendacoes = []
    if temperatura > 40:
        recomendacoes.append("Acionar sistema de resfriamento dos painéis")
    if comunicacao < 20:
        recomendacoes.append("Restabelecer contato com a base urgente")
    if bateria < 15:
        recomendacoes.append("Ativar modo de economia de energia")
    if energia_solar < 15:
        recomendacoes.append("Verificar integridade dos painéis solares")
    if estabilidade < 35:
        recomendacoes.append("Reduzir operações não essenciais")
    if not recomendacoes:
        return "Manter operação normal e continuar monitoramento."
    return "Ação necessária: " + ", ".join(recomendacoes) + "."

#-------------
# EXIBIÇÃO DOS CICLOS
#------------

def exibir_ciclos():
    riscos = []
    for i, ciclo in enumerate(dados_missao):
        temperatura, comunicacao, bateria, energia_solar, estabilidade = ciclo

        status_temp, _, desc_temp = analisar_temperatura(temperatura)
        status_com,  _, desc_com  = analisar_comunicacao(comunicacao)
        status_bat,  _, desc_bat  = analisar_bateria(bateria)
        status_sol,  _, desc_sol  = analisar_energia_solar(energia_solar)
        status_est,  _, desc_est  = analisar_estabilidade(estabilidade)

        pontuacao     = calcular_risco_ciclo(ciclo)
        classificacao = classificar_ciclo(pontuacao)
        recomendacao  = gerar_recomendacao(ciclo)
        riscos.append(pontuacao)

        print("\n" + "=" * 58)
        print(f" CICLO {i + 1:02d}")
        print("=" * 58)
        print(f" Temperatura    : {temperatura} °C  | {status_temp} | {desc_temp}")
        print(f" Comunicação    : {comunicacao}%    | {status_com}  | {desc_com}")
        print(f" Bateria        : {bateria}%    | {status_bat}  | {desc_bat}")
        print(f" Energia Solar  : {energia_solar} W   | {status_sol}  | {desc_sol}")
        print(f" Estabilidade   : {estabilidade}%    | {status_est}  | {desc_est}")
        print("-" * 58)
        print(f" Pontuação de risco : {pontuacao}")
        print(f" Classificação      : {classificacao}")
        print(f" Recomendação       : {recomendacao}")

    return riscos

#----------------------------------------
# RELATÓRIO FINAL
# ---------------------------------------

def gerar_relatorio_final(riscos):
    num_ciclos        = len(dados_missao)
    risco_medio       = sum(riscos) / num_ciclos
    ciclo_critico     = riscos.index(max(riscos)) + 1
    classificacao_final = classificar_ciclo(round(risco_medio))

    # Médias de energia para o relatório de sustentabilidade
    media_solar   = sum(c[3] for c in dados_missao) / num_ciclos
    media_bateria = sum(c[2] for c in dados_missao) / num_ciclos

    print("\n" + "=" * 58)
    print(" RELATÓRIO FINAL DA MISSÃO")
    print("=" * 58)
    print(f" Missão              : {nome_missao}")
    print(f" Equipe              : {nome_equipe}")
    print(f" Ciclos monitorados  : {num_ciclos}")
    print(f" Risco médio         : {risco_medio:.2f}")
    print(f" Ciclo mais crítico  : Ciclo {ciclo_critico:02d}")
    print(f" Classificação final : {classificacao_final}")
    print("-" * 58)
    print(f" Média de energia solar  : {media_solar:.1f} W")
    print(f" Média de carga bateria  : {media_bateria:.1f}%")
    print("=" * 58)

# -------------------
# EXECUÇÃO PRINCIPAL
# -----------------

print("=" * 58)
print(" MISSION CONTROL AI — SOLARIS-1")
print(" GS2026.1 | Energias Renováveis e Sustentáveis")
print("=" * 58)
print(f" Missão : {nome_missao}")
print(f" Equipe : {nome_equipe}")
print(f" Áreas monitoradas : {len(areas_monitoradas)}")
print(f" Ciclos de dados   : {len(dados_missao)}")
print("=" * 58)

riscos = exibir_ciclos()
gerar_relatorio_final(riscos)

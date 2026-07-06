# ============================================================
# MODULO 02 - AULA 12: PERSISTENCIA EM ARQUIVO TXT (Create e Read)
# ------------------------------------------------------------
# Ate agora os dados sumiam ao fechar o programa (viviam so na
# memoria). Agora vamos GRAVAR em um arquivo de texto para que
# fiquem salvos entre uma execucao e outra.
# ============================================================

ARQUIVO = "pessoas.txt"

def create(nome):
    # 'a' (append) adiciona no FIM do arquivo, sem apagar o que ja existe.
    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome}\n")

def read():
    nomes = []
    try:
        # 'r' (read) abre o arquivo para leitura.
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nomes.append(linha.strip())   # strip remove o \n do fim
    except FileNotFoundError:
        pass   # se o arquivo ainda nao existe, devolvemos a lista vazia
    return nomes

# ============================================================
# MODULO 02 - AULA 13: CRUD COMPLETO EM ARQUIVO TXT
# ------------------------------------------------------------
# CRUD = Create, Read, Update, Delete. Vamos guardar hospedes de
# um hotel em um arquivo, um por linha, com os campos separados
# por virgula. Assim NAO precisamos do eval() (que e perigoso,
# pois executa qualquer codigo que estiver no arquivo).
# ============================================================

from datetime import datetime

ARQUIVO = "hotel.txt"

def saudacao():
    hora = datetime.now().hour
    # CORRECAO do bug da versao antiga: usar elif encadeado.
    # Antes, com dois "if" soltos, a manha caia no "else" e
    # imprimia "Bom dia" E "Boa noite" ao mesmo tempo.
    if 5 <= hora < 13:
        print("Bom dia!")
    elif 13 <= hora < 18:
        print("Boa tarde!")
    else:
        print("Boa noite!")

def create(nome, idade, telefone):
    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome},{idade},{telefone}\n")

def read():
    hospedes = []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")   # [nome, idade, telefone]
                hospedes.append(dados)
    except FileNotFoundError:
        pass
    return hospedes

def update(nome, novo_nome, nova_idade, novo_telefone):
    hospedes = read()
    encontrou = False
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        for dados in hospedes:
            if dados[0].lower() == nome.lower():
                arquivo.write(f"{novo_nome},{nova_idade},{novo_telefone}\n")
                encontrou = True
            else:
                arquivo.write(",".join(dados) + "\n")
    return encontrou

def delete(nome):
    hospedes = read()
    encontrou = False
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        for dados in hospedes:
            if dados[0].lower() == nome.lower():
                encontrou = True   # simplesmente NAO reescreve = apagou
            else:
                arquivo.write(",".join(dados) + "\n")
    return encontrou

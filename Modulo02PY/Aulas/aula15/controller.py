# ============================================================
# MODULO 02 - AULA 15: RELACIONANDO DOIS ARQUIVOS + RELATORIO
# ------------------------------------------------------------
# Projeto final do modulo: um hotel guarda PESSOAS em um arquivo
# e APARTAMENTOS em outro. Depois, cruzamos os dois para gerar um
# RELATORIO (uma pessoa + o apartamento dela). Tudo com json.
#
# Aqui juntamos tudo do modulo: funcoes, arquivos, dicionarios,
# busca e persistencia segura.
# ============================================================

import json

ARQ_PESSOAS = "pessoas.json"
ARQ_APARTAMENTOS = "apartamentos.json"
ARQ_RELATORIO = "relatorio.json"

def _carregar(arquivo):
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def _salvar(arquivo, dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

def criar_pessoa(nome, cpf):
    pessoas = _carregar(ARQ_PESSOAS)
    pessoas.append({"nome": nome, "cpf": cpf})
    _salvar(ARQ_PESSOAS, pessoas)

def criar_apartamento(numero, andar):
    apartamentos = _carregar(ARQ_APARTAMENTOS)
    apartamentos.append({"numero": numero, "andar": andar})
    _salvar(ARQ_APARTAMENTOS, apartamentos)

def _buscar(lista, campo, valor):
    """Procura na lista o primeiro item cujo campo bate com o valor."""
    for item in lista:
        if item[campo] == valor:
            return item
    return None

def gerar_relatorio(cpf, numero_apartamento):
    pessoa = _buscar(_carregar(ARQ_PESSOAS), "cpf", cpf)
    if pessoa is None:
        return "Pessoa nao encontrada."

    apartamento = _buscar(_carregar(ARQ_APARTAMENTOS), "numero", numero_apartamento)
    if apartamento is None:
        return "Apartamento nao encontrado."

    # cruzando (relacionando) os dados dos dois arquivos:
    relatorio = {
        "nome": pessoa["nome"],
        "cpf": pessoa["cpf"],
        "apartamento": apartamento["numero"],
        "andar": apartamento["andar"],
    }
    _salvar(ARQ_RELATORIO, relatorio)
    return relatorio

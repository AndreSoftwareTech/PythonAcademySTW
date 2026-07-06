# ============================================================
# MODULO 02 - AULA 14: PERSISTENCIA SEGURA COM JSON  [NOVO]
# ------------------------------------------------------------
# Guardar campos separados por virgula funciona, mas quebra se o
# proprio dado tiver uma virgula (ex.: um endereco). Alem disso,
# a versao antiga usava eval() para "reconstruir" dicionarios do
# arquivo - e eval() e PERIGOSO, pois executa qualquer codigo.
#
# A solucao profissional e o modulo json: ele salva e le
# estruturas (listas e dicionarios) de forma SEGURA e organizada.
# ============================================================

import json

ARQUIVO = "hospedes.json"

def _carregar():
    """Le o arquivo json e devolve uma lista de dicionarios."""
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []   # arquivo inexistente ou vazio -> lista vazia

def _salvar(hospedes):
    """Grava a lista de dicionarios no arquivo json."""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        # ensure_ascii=False mantem acentos; indent=2 deixa legivel.
        json.dump(hospedes, f, ensure_ascii=False, indent=2)

def create(nome, idade, telefone):
    hospedes = _carregar()
    hospedes.append({"nome": nome, "idade": idade, "telefone": telefone})
    _salvar(hospedes)

def read():
    return _carregar()

def update(nome, novos_dados):
    hospedes = _carregar()
    encontrou = False
    for hospede in hospedes:
        if hospede["nome"].lower() == nome.lower():
            hospede.update(novos_dados)   # atualiza so os campos enviados
            encontrou = True
    _salvar(hospedes)
    return encontrou

def delete(nome):
    hospedes = _carregar()
    restantes = [h for h in hospedes if h["nome"].lower() != nome.lower()]
    _salvar(restantes)
    return len(restantes) != len(hospedes)   # True se algo foi removido

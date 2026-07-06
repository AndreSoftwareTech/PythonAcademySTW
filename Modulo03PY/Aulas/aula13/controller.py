# ============================================================
# MODULO 03 - AULA 13: CONTROLLER (CRUD JSON com objetos Cliente)
# ============================================================

import json
from cliente import Cliente

ARQUIVO = "clientes.json"

def _carregar():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def _salvar(lista):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=2)

def cadastrar(cliente):
    dados = _carregar()
    dados.append(cliente.to_dict())
    _salvar(dados)

def listar():
    for item in _carregar():
        print(Cliente.from_dict(item))

def buscar_por_titular(nome):
    for item in _carregar():
        if item["titular"].lower() == nome.lower():
            return Cliente.from_dict(item)
    return None

def remover(nome):
    dados = [d for d in _carregar() if d["titular"].lower() != nome.lower()]
    _salvar(dados)

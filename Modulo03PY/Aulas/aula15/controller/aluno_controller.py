# ============================================================
# CONTROLLER: CRUD em memoria com objetos Aluno
# ============================================================

import json
from model.aluno import Aluno

ARQUIVO = "alunos.json"

def _carregar():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return [Aluno.from_dict(d) for d in json.load(f)]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def _salvar(alunos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump([a.to_dict() for a in alunos], f, ensure_ascii=False, indent=2)

def cadastrar(nome, nota):
    alunos = _carregar()
    alunos.append(Aluno(nome, nota))
    _salvar(alunos)
    return f"Aluno {nome} cadastrado."

def listar():
    return _carregar()

def media_geral():
    alunos = _carregar()
    if not alunos:
        return "Nenhum aluno cadastrado."
    media = sum(a.nota for a in alunos) / len(alunos)
    return f"Media geral: {media:.2f}"

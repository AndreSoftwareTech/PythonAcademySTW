# ============================================================
# EXERCICIO 15 - "O SISTEMA ACADEMICO" (PROJETO FINAL DO MODULO)
# Base: Aula 15 (Relacionar dois arquivos + relatorio)
# ------------------------------------------------------------
# Contexto:
#   O boss final do Modulo 02: guardar ALUNOS em um arquivo e
#   CURSOS em outro, e depois cruzar os dois para gerar um
#   relatorio (qual aluno esta em qual curso). Tudo com json.
#
# Sua missao:
#   - matricular_aluno(nome, curso_id): salva em alunos.json
#   - criar_curso(curso_id, nome_curso): salva em cursos.json
#   - relatorio(nome_aluno): encontra o aluno, descobre o curso
#     dele pelo curso_id e devolve um dicionario com nome do aluno
#     + nome do curso.
#
# Regras (validando a Aula 15):
#   - Relacione os dois arquivos pelo campo em comum (curso_id).
#
# Desafio logico:
#   Se o aluno ou o curso nao existir, devolva uma mensagem clara.
# ============================================================

# --- GABARITO DO PROFESSOR ---
import json

ARQ_ALUNOS = "alunos.json"
ARQ_CURSOS = "cursos.json"

def _carregar(arquivo):
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def _salvar(arquivo, dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

def matricular_aluno(nome, curso_id):
    alunos = _carregar(ARQ_ALUNOS)
    alunos.append({"nome": nome, "curso_id": curso_id})
    _salvar(ARQ_ALUNOS, alunos)

def criar_curso(curso_id, nome_curso):
    cursos = _carregar(ARQ_CURSOS)
    cursos.append({"curso_id": curso_id, "nome_curso": nome_curso})
    _salvar(ARQ_CURSOS, cursos)

def relatorio(nome_aluno):
    aluno = None
    for a in _carregar(ARQ_ALUNOS):
        if a["nome"].lower() == nome_aluno.lower():
            aluno = a
            break
    if aluno is None:
        return "Aluno nao encontrado."

    curso = None
    for c in _carregar(ARQ_CURSOS):
        if c["curso_id"] == aluno["curso_id"]:
            curso = c
            break
    if curso is None:
        return "Curso do aluno nao encontrado."

    return {"aluno": aluno["nome"], "curso": curso["nome_curso"]}

# Demonstracao:
criar_curso(1, "Python")
criar_curso(2, "Banco de Dados")
matricular_aluno("Andre", 1)
matricular_aluno("Maria", 2)
print(relatorio("Andre"))
print(relatorio("Maria"))
print(relatorio("Fulano"))

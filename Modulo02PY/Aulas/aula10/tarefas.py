# ============================================================
# MODULO 02 - AULA 10: CRUD EM MEMORIA COM FUNCOES (usando LISTA)
# ------------------------------------------------------------
# CRUD = Create (criar), Read (ler), Update (atualizar),
# Delete (remover). Aqui os dados ficam em uma LISTA na memoria:
# eles SOMEM quando o programa fecha. Nas proximas aulas vamos
# aprender a salvar tudo em arquivo para nao perder os dados.
# ============================================================

tarefas = []

def adicionar(tarefa):
    tarefas.append(tarefa)
    return "Tarefa adicionada com sucesso"

def listar():
    return tarefas

def remover(indice):
    if indice >= 0 and indice < len(tarefas):
        tarefas.pop(indice)
        return "Tarefa removida"
    return "Indice invalido"

def quantidade():
    return len(tarefas)

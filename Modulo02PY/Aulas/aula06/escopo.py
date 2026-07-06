# ============================================================
# MODULO 02 - AULA 06: ESCOPO DE VARIAVEIS (LOCAL x GLOBAL)  [NOVO]
# ------------------------------------------------------------
# Objetivo: entender ONDE cada variavel "existe".
#   - LOCAL : criada dentro da funcao, so vive ali dentro.
#   - GLOBAL: criada fora das funcoes, visivel no programa todo.
# ============================================================

mensagem_global = "Eu existo no programa inteiro"

def mostrar():
    mensagem_local = "Eu so existo dentro desta funcao"
    print(mensagem_local)     # ok: estou dentro da funcao
    print(mensagem_global)    # ok: dentro da funcao consigo LER a global

mostrar()
print(mensagem_global)
# print(mensagem_local)  # ERRO: variavel local nao existe aqui fora

# Para ALTERAR uma variavel global de dentro de uma funcao,
# precisamos avisar o Python com a palavra 'global':
contador = 0

def incrementar():
    global contador
    contador = contador + 1

incrementar()
incrementar()
print("Contador apos 2 chamadas:", contador)   # 2

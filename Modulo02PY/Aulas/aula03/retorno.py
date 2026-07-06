# ============================================================
# MODULO 02 - AULA 03: RETORNO DE VALORES (return)
# ------------------------------------------------------------
# Objetivo: entender a diferenca entre uma funcao que apenas
# IMPRIME e uma que DEVOLVE (return) um valor para ser reutilizado.
# ============================================================

# 'return' entrega um resultado para QUEM CHAMOU a funcao.
# Assim conseguimos guardar esse valor em uma variavel.
def perguntar_nome():
    nome = input("Digite seu nome >> ")
    return nome

nome_digitado = perguntar_nome()
print("Nome recebido da funcao:", nome_digitado)

# Diferenca importante:
#   - print()  -> apenas MOSTRA na tela
#   - return   -> DEVOLVE o valor para ser usado depois

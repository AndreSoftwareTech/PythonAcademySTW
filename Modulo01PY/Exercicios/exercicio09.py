# ============================================================
# EXERCICIO 09 - "O MESMO CRACHA, OUTRO CAMINHO"
# Base: Aula 09 (Formatacao com .format())
# ------------------------------------------------------------
# Contexto:
#   Antes da f-string, o jeito classico de montar textos com
#   variaveis era o metodo .format(). Um bom programador conhece
#   os dois caminhos e entende que existem varias formas de chegar
#   ao mesmo resultado.
#
# Sua missao:
#   Refaca o cracha do exercicio anterior, mas agora usando
#   OBRIGATORIAMENTE o metodo .format() (com as chaves {} vazias).
#
# Regras (validando a Aula 09):
#   - Nada de f-string aqui. O objetivo e treinar o .format().
#
# Desafio logico:
#   Use os indices nas chaves ({0}, {1}) para imprimir o nome DUAS
#   vezes sem repetir a variavel na chamada do format.
# ============================================================

# --- GABARITO DO PROFESSOR ---
nome = input("Nome do participante >> ")
empresa = input("Empresa >> ")
funcao = input("Funcao >> ")

print("===== CRACHA =====")
print("Nome: {}".format(nome))
print("Empresa: {}".format(empresa))
print("Funcao: {}".format(funcao))

# Desafio: reaproveitando o mesmo valor pela posicao {0}
print("Ate mais, {0}! Volte sempre, {0}.".format(nome))

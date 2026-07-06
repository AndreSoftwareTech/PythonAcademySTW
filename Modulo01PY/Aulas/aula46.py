# ============================================================
# AULA 46 - ESTRUTURA DE REPETICAO WHILE (introducao)
# Objetivo: repetir um bloco ENQUANTO uma condicao for verdadeira.
# ============================================================

# Precisamos INICIAR a variavel antes de usar no while,
# caso contrario o Python nao sabe quanto vale "c" (NameError).
c = 0

while c < 10:
    print(c)
    c = c + 1   # sem esta linha o laco nunca terminaria (loop infinito)

print("Fim do while")

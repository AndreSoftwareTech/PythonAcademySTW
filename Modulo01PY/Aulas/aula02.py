# ============================================================
# AULA 02 - COMENTARIOS E BOAS PRATICAS
# Objetivo: aprender a documentar o codigo e a escrever de forma legivel.
# ============================================================

# Comentario de UMA linha comeca com #
# O Python IGNORA tudo que vem depois do # naquela linha.

print("Estudando comentarios")  # tambem da para comentar no fim da linha

# Comentario de VARIAS linhas: usamos # em cada linha,
# ou uma "string solta" com aspas triplas (muito usada como anotacao):
"""
Este e um bloco de texto usado como anotacao.
Serve para explicar trechos maiores do programa.
"""

# BOAS PRATICAS para nomear variaveis:
nome_completo = "Andre Vitor"   # use nomes que descrevem o conteudo
idade_do_aluno = 25             # separe palavras com _ (padrao snake_case)
PI = 3.14159                    # CONSTANTES costumam ficar em MAIUSCULO

print(nome_completo, idade_do_aluno, PI)

# Evite nomes sem significado, como: x, aaa, coisa1

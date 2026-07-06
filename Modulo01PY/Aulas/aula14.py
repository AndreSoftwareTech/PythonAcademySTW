# ============================================================
# AULA 14 - STRINGS: METODOS ESSENCIAIS
# Objetivo: transformar e analisar textos com metodos prontos.
# ============================================================

frase = "  Aprendendo Python na pratica  "

print(frase.upper())    # TUDO EM MAIUSCULO
print(frase.lower())    # tudo em minusculo
print(frase.strip())    # remove os espacos das pontas
print(frase.title())    # Deixa Cada Palavra Com Inicial Maiuscula
print(frase.replace("Python", "Logica"))  # troca um trecho por outro

# split() quebra a frase em uma LISTA de palavras
palavras = frase.strip().split(" ")
print(palavras)

# operador "in": verifica se um trecho existe dentro do texto
print("Python" in frase)   # True
print("Java" in frase)     # False

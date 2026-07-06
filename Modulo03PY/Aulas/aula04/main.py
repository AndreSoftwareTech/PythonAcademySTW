# ============================================================
# MODULO 03 - AULA 04: MAIN (comparando as 3 formas)
# ============================================================

from pessoa import Pessoa1, Pessoa2, Pessoa3

# Forma 1: construtor completo (melhor pratica)
p1 = Pessoa1("Ana", "Costa", 28, 62.5)
print("Pessoa1:", p1.nome, p1.idade)

# Forma 2: objeto vazio + preenchimento manual
p2 = Pessoa2()
p2.nome = input("Nome (Pessoa2) >> ")
p2.idade = int(input("Idade >> "))
print("Pessoa2:", p2.nome, p2.idade)

# Forma 3: copiar dados de outro objeto
p3 = Pessoa3()
p3.copiar_de(p1)
print("Pessoa3 (copia de P1):", p3.nome, p3.idade)

# ============================================================
# MODULO 03 - AULA 04: TRES FORMAS DE CRIAR UMA CLASSE
# ------------------------------------------------------------
# Objetivo: comparar 3 abordagens de inicializacao:
#   Pessoa1 -> __init__ completo (recomendado)
#   Pessoa2 -> __init__ vazio (atributos depois)
#   Pessoa3 -> copia manual entre objetos
#
# CORRECAO: padronizamos nomes em snake_case (nome, idade, peso).
# ============================================================

class Pessoa1:
    def __init__(self, nome, sobrenome, idade, peso):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = int(idade)
        self.peso = float(peso)

class Pessoa2:
    def __init__(self):
        pass  # objeto nasce vazio; atributos entram depois

class Pessoa3:
    def __init__(self):
        self.nome = ""
        self.sobrenome = ""
        self.idade = 0
        self.peso = 0.0

    def copiar_de(self, outra):
        self.nome = outra.nome
        self.sobrenome = outra.sobrenome
        self.idade = outra.idade
        self.peso = outra.peso

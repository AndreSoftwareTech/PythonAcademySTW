# ============================================================
# MODULO 03 - AULA 10: POLIMORFISMO [NOVO]
# ------------------------------------------------------------
# Objetivo: polimorfismo = "muitas formas". Diferentes classes
# respondem ao MESMO metodo de formas diferentes. O codigo que
# chama nao precisa saber qual tipo exato e; basta chamar o metodo.
# ============================================================

class Cachorro:
    def emitir_som(self):
        return "Au au!"

class Gato:
    def emitir_som(self):
        return "Miau!"

class Vaca:
    def emitir_som(self):
        return "Muuu!"

def apresentar_animal(animal):
    # Funcao polimorfica: funciona com QUALQUER objeto que tenha emitir_som()
    print(f"O animal diz: {animal.emitir_som()}")

# Lista heterogenea: objetos de classes diferentes, mesmo "contrato"
animais = [Cachorro(), Gato(), Vaca()]

for animal in animais:
    apresentar_animal(animal)

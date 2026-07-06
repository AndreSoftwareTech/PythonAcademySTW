# ============================================================
# EXERCICIO 08 - "A FAMILIA DOS ANIMAIS"
# Base: Aula 08 (Heranca e super())
# ------------------------------------------------------------
# Contexto:
#   Na natureza, cachorros e gatos compartilham DNA com "Animal",
#   mas cada um tem comportamentos proprios. Em OOP, a classe PAI
#   concentra o que e comum; as FILHAS especializam. super() garante
#   que o construtor da pai rode antes — ninguem nasce sem nome e especie.
#
# Sua missao:
#   Monte uma pequena hierarquia zoologica:
#     1) Classe Animal com __init__(self, nome, especie) e metodo apresentar().
#     2) Classe Cachorro(Animal) com __init__(self, nome, raca) chamando super().
#     3) Classe Gato(Animal) com __init__(self, nome, cor_pelagem) chamando super().
#     4) Cada filha sobrescreve apresentar() com mensagem caracteristica.
#     5) Cada filha implementa __str__ usando super().__str__() ou dados do pai.
#     6) Crie um cachorro e um gato; chame apresentar() e print() em ambos.
#
# Regras (validando a Aula 08):
#   - Filhas DEVEM chamar super().__init__(...) no construtor.
#   - Animal.apresentar() imprime nome e especie; filhas estendem o comportamento.
#   - Use heranca explicita: class Cachorro(Animal): (nao copie codigo do pai).
#
# Desafio logico:
#   Ambos sao Animal? Teste isinstance(cachorro, Animal) e isinstance(gato, Animal).
# ============================================================

# --- GABARITO DO PROFESSOR ---
class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def apresentar(self):
        print(f"Ola! Sou {self.nome}, um {self.especie}.")

    def __str__(self):
        return f"{self.nome} ({self.especie})"


class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, "Cachorro")
        self.raca = raca

    def apresentar(self):
        super().apresentar()
        print(f"Raca: {self.raca}. Au au!")

    def __str__(self):
        return f"{super().__str__()} | Raca: {self.raca}"


class Gato(Animal):
    def __init__(self, nome, cor_pelagem):
        super().__init__(nome, "Gato")
        self.cor_pelagem = cor_pelagem

    def apresentar(self):
        super().apresentar()
        print(f"Pelagem {self.cor_pelagem}. Miau!")

    def __str__(self):
        return f"{super().__str__()} | Pelagem: {self.cor_pelagem}"


rex = Cachorro("Rex", "Labrador")
luna = Gato("Luna", "Rajada")

rex.apresentar()
print(rex)

luna.apresentar()
print(luna)

# Desafio: polimorfismo — ambos sao Animal
print("Rex e Animal?", isinstance(rex, Animal))
print("Luna e Animal?", isinstance(luna, Animal))

for pet in (rex, luna):
    print("---", pet.nome, "---")
    pet.apresentar()

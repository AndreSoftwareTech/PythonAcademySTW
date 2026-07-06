# ============================================================
# EXERCICIO 10 - "O SHOW DOS ANIMAIS"
# Base: Aula 10 (Polimorfismo: mesmo metodo, formas diferentes)
# ------------------------------------------------------------
# Contexto:
#   Polimorfismo e "muitas formas". Diferentes classes podem ter
#   o MESMO metodo, mas cada uma responde do seu jeito. Quem
#   chama o metodo nao precisa saber qual tipo exato e.
#
# Sua missao:
#   Crie tres classes (Cachorro, Gato, Vaca), cada uma com
#   emitir_som() retornando seu som caracteristico.
#   Monte uma lista com um objeto de cada classe e, em um for,
#   chame emitir_som() de todos — sem if/elif para saber o tipo.
#
# Regras (validando a Aula 10):
#   - Cada classe implementa emitir_som() com retorno proprio.
#   - Use uma lista heterogenea e um laco for.
#
# Desafio logico:
#   Crie uma funcao apresentar_animal(animal) que receba QUALQUER
#   objeto com emitir_som() e imprima "O animal diz: ...".
# ============================================================

# --- GABARITO DO PROFESSOR ---
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
    print(f"O animal diz: {animal.emitir_som()}")


animais = [Cachorro(), Gato(), Vaca()]

for animal in animais:
    apresentar_animal(animal)

from pessoa1 import Pessoa1
from pessoa2 import Pessoa2
from pessoa3 import Pessoa3


abacate = Pessoa1(
                input("Digite Seu Nome >> "),
                input("Digite Seu SobreNome >>"),
                input("Digite Sua Idade"), 
                input("Digite Seu peso ")
                )

laranja = Pessoa2()

moranguinho = Pessoa3()


laranja.Nome = abacate.Nome
laranja.Sobrenome = abacate.Sobrenome
laranja.Idade = abacate.Idade
laranja.Peso = abacate.Peso

moranguinho.Nome = laranja.Nome
moranguinho.Sobrenome = laranja.Sobrenome
moranguinho.idade = laranja.Idade
moranguinho.Peso = laranja.Peso

print(moranguinho)

print("*"*20, "Menu de Pessoa", )
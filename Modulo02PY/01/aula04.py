def sobrenome():
    sobrenome = input("Digite seu sobrenome >> ")
    return sobrenome

def idade():
    idade = input("Digite sua idade >> ")
    return idade

def nome():
    nome = input("Digite seu nome >> ")
    return nome

def cpf():
    cpf = input("Digite seu cpf >> ")
    return cpf

a = nome()
b = sobrenome()
c = idade()
d = cpf()
print(f"Nome {a} sobrenome {b} idade {c} CPF {d}")
print(a, b, c, d)
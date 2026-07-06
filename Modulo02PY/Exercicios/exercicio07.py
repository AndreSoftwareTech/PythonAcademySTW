# ============================================================
# EXERCICIO 07 - "A URNA FLEXIVEL"
# Base: Aula 07 (Argumentos padrao e *args)
# ------------------------------------------------------------
# Contexto:
#   As vezes nao sabemos quantos valores virao. O *args deixa a
#   funcao aceitar quantos argumentos o usuario quiser.
#
# Sua missao:
#   1) Crie 'saudacao(nome, mensagem="Bem-vindo")' usando um
#      argumento PADRAO. Chame com e sem a mensagem.
#   2) Crie 'media(*notas)' que aceite QUALQUER quantidade de notas
#      e retorne a media delas.
#
# Regras (validando a Aula 07):
#   - Use argumento padrao em uma funcao e *args na outra.
# ============================================================

# --- GABARITO DO PROFESSOR ---
def saudacao(nome, mensagem="Bem-vindo"):
    print(f"{mensagem}, {nome}!")

saudacao("Andre")
saudacao("Maria", "Ola")

def media(*notas):
    return sum(notas) / len(notas)

print("Media de 3 notas:", media(8, 7, 9))
print("Media de 5 notas:", media(6, 7, 8, 9, 10))

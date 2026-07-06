# ============================================================
# EXERCICIO 02 - "O CRACHA PERSONALIZADO"
# Base: Aula 02 (Funcoes com parametros)
# ------------------------------------------------------------
# Contexto:
#   Uma funcao fica muito mais util quando trabalha com valores
#   diferentes a cada chamada. Para isso servem os parametros.
#
# Sua missao:
#   Crie uma funcao 'apresentar' que receba DOIS parametros
#   (nome e curso) e imprima uma frase de boas-vindas usando os
#   dois. Chame a funcao para pelo menos 2 alunos diferentes.
#
# Regras (validando a Aula 02):
#   - A funcao deve ter parametros; nada de valores fixos dentro.
# ============================================================

# --- GABARITO DO PROFESSOR ---
def apresentar(nome, curso):
    print(f"Ola {nome}, seja bem-vindo(a) ao curso de {curso}!")

apresentar("Andre", "Python")
apresentar("Maria", "Logica de Programacao")

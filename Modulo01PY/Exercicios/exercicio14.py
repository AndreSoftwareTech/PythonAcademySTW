# ============================================================
# EXERCICIO 14 - "O NORMALIZADOR DE CADASTRO"
# Base: Aula 14 (Strings: metodos essenciais)
# ------------------------------------------------------------
# Contexto:
#   Usuarios digitam de tudo: "  ANA ", "ana ", " AnA". Um bom
#   sistema padroniza esses dados antes de guardar, para nao virar
#   bagunca no banco.
#
# Sua missao:
#   Pergunte o nome completo do usuario (deixe ele baguncar de
#   proposito com espacos e maiusculas) e gere a versao "limpa":
#     - sem espacos sobrando nas pontas
#     - com a primeira letra de cada palavra em maiusculo
#   Depois, informe quantas PALAVRAS ele digitou.
#
# Regras (validando a Aula 14):
#   - Use strip(), title() e split().
#
# Desafio logico:
#   Troque todos os espacos por ponto (.) para gerar um "usuario de
#   login" no estilo nome.sobrenome.
# ============================================================

# --- GABARITO DO PROFESSOR ---
nome_completo = input("Digite seu nome completo >> ")

limpo = nome_completo.strip().title()
print("Nome padronizado:", limpo)

palavras = limpo.split(" ")
print("Quantidade de palavras:", len(palavras))

# Desafio: login no formato nome.sobrenome
login = limpo.lower().replace(" ", ".")
print("Login sugerido:", login)

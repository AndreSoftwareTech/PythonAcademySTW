# ============================================================
# EXERCICIO 48 - "O MENU QUE NAO DESISTE"
# Base: Aula 48 (while controlado por sim/nao)
# ------------------------------------------------------------
# Contexto:
#   Quase todo programa interativo pergunta: "deseja continuar?".
#   O while le a resposta do usuario e decide se roda de novo. Quem
#   manda no laco agora e a pessoa.
#
# Sua missao:
#   Repita a seguinte acao ENQUANTO o usuario quiser: pergunte um
#   nome e cumprimente a pessoa. Ao final de cada volta, pergunte se
#   ele deseja continuar (sim/nao). Pare quando responder "nao".
#
# Regras (validando a Aula 48):
#   - Use while comparando a resposta (dica: use .lower() para aceitar
#     "Sim", "SIM", "sim" etc).
# ============================================================

# --- GABARITO DO PROFESSOR ---
continuar = "sim"

while continuar.lower() == "sim":
    nome = input("Digite um nome >> ")
    print(f"Ola, {nome}! Que bom te ver.")
    continuar = input("Deseja continuar? (sim/nao) >> ")

print("Programa encerrado.")

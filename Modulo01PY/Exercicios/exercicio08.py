# ============================================================
# EXERCICIO 08 - "O CRACHA DO EVENTO"
# Base: Aula 08 (Interpolacao com f-string)
# ------------------------------------------------------------
# Contexto:
#   A f-string e a forma mais elegante e moderna de montar textos
#   com variaveis dentro. Ela deixa o codigo limpo e legivel.
#
# Sua missao:
#   Voce e o sistema de credenciamento de um evento de tecnologia.
#   Pergunte ao participante o nome, a empresa e a funcao. Depois,
#   imprima um cracha usando SOMENTE f-string, no formato:
#
#       ===== CRACHA =====
#       Nome: <nome>
#       Empresa: <empresa>
#       Funcao: <funcao>
#
# Regras (validando a Aula 08):
#   - Todas as variaveis devem aparecer via f-string (prefixo f"...").
# ============================================================

# --- GABARITO DO PROFESSOR ---
nome = input("Nome do participante >> ")
empresa = input("Empresa >> ")
funcao = input("Funcao >> ")

print("===== CRACHA =====")
print(f"Nome: {nome}")
print(f"Empresa: {empresa}")
print(f"Funcao: {funcao}")

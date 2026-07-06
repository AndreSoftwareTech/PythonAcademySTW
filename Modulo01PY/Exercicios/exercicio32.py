# ============================================================
# EXERCICIO 32 - "A LISTA DE CONVIDADOS SEM REPETICAO"
# Base: Aula 32 (Conjuntos - set)
# ------------------------------------------------------------
# Contexto:
#   Imagine duas listas de convidados de festas diferentes, cheias
#   de nomes repetidos. O conjunto (set) resolve isso: ele NUNCA
#   guarda duplicatas e ainda sabe comparar grupos.
#
# Sua missao:
#   Crie dois conjuntos: convidados_sabado e convidados_domingo
#   (com alguns nomes em comum). Descubra:
#     - todos os convidados unicos das duas festas (uniao)
#     - quem foi nas DUAS festas (intersecao)
#     - quem foi so no sabado (diferenca)
#
# Regras (validando a Aula 32):
#   - Use conjuntos {} e os operadores |, & e -.
# ============================================================

# --- GABARITO DO PROFESSOR ---
convidados_sabado = {"Ana", "Bruno", "Carla", "Diego"}
convidados_domingo = {"Carla", "Diego", "Eduardo", "Fabi"}

print("Todos os convidados:", convidados_sabado | convidados_domingo)
print("Foram nas duas:", convidados_sabado & convidados_domingo)
print("Somente no sabado:", convidados_sabado - convidados_domingo)

# ============================================================
# EXERCICIO 49 - "O SEGURANCA DA ENTRADA"
# Base: Aula 49 (Validacao de entrada: while True + break)
# ------------------------------------------------------------
# Contexto:
#   Usuario e criativo: ele digita o que nao devia. Um sistema
#   profissional NAO aceita dado invalido: ele insiste ate receber
#   algo correto. Esse padrao aparece em quase todo software real.
#
# Sua missao:
#   Peca uma nota de 0 a 10. Enquanto o usuario digitar um valor fora
#   dessa faixa, mostre um aviso e pergunte de novo. So siga em frente
#   quando a nota for valida, e entao confirme a nota registrada.
#
# Regras (validando a Aula 49):
#   - Use while True e saia com break quando a nota for valida.
# ============================================================

# --- GABARITO DO PROFESSOR ---
while True:
    nota = float(input("Digite uma nota de 0 a 10 >> "))
    if nota >= 0 and nota <= 10:
        break
    print("Nota invalida! Deve ser entre 0 e 10.")

print(f"Nota {nota:.1f} registrada com sucesso.")

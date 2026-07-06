# ============================================================
# AULA 20 - OPERADORES LOGICOS: and, or, not
# Objetivo: combinar varias condicoes em uma so decisao.
# ============================================================

idade = int(input("Digite sua idade >> "))
tem_carteira = input("Voce tem carteira de motorista? (sim/nao) >> ").lower()

# and -> verdadeiro SOMENTE se as DUAS condicoes forem verdadeiras
pode_dirigir = idade >= 18 and tem_carteira == "sim"
print("Pode dirigir?", pode_dirigir)

# or -> verdadeiro se PELO MENOS UMA condicao for verdadeira
fim_de_semana = input("E fim de semana? (sim/nao) >> ").lower()
feriado = input("E feriado? (sim/nao) >> ").lower()
pode_descansar = fim_de_semana == "sim" or feriado == "sim"
print("Pode descansar?", pode_descansar)

# not -> inverte o valor logico (troca True por False e vice-versa)
print("NAO pode dirigir?", not pode_dirigir)

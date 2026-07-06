# ============================================================
# AULA 45 - LACO ANINHADO (for dentro de for)
# Objetivo: repetir um laco dentro de outro (util para tabelas e padroes).
# ============================================================

# Tabuada de 1 a 5 (o laco de fora escolhe a tabuada,
# o laco de dentro faz as multiplicacoes de 1 a 10)
for tabuada in range(1, 6):
    print(f"--- Tabuada do {tabuada} ---")
    for multiplicador in range(1, 11):
        print(f"{tabuada} x {multiplicador} = {tabuada * multiplicador}")
    print()   # linha em branco entre uma tabuada e outra

# Padrao de triangulo com asteriscos
for linha in range(1, 6):
    print("*" * linha)

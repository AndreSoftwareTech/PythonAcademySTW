# ============================================================
# EXERCICIO 51 - "PROJETO FINAL: O SISTEMA DE MATRICULAS"
# Base: Aula 51 (Projeto: while + for + dicionario + tudo)
# ------------------------------------------------------------
# Contexto:
#   Este e o boss final do Modulo 01. Aqui voce prova que domina
#   TODOS os fundamentos: entrada, conversao, laco, acumulador,
#   decisao, dicionario e validacao. Nada de novo, so tudo junto.
#
# Sua missao (a lenda):
#   A "Python Academy" precisa de um sistema de matriculas. Enquanto
#   houver alunos para cadastrar, o sistema deve, para CADA aluno:
#     1) pedir o nome (nao pode ser vazio - valide!)
#     2) pedir a idade (numero valido)
#     3) pedir 3 notas e calcular a media (use um for + acumulador)
#     4) definir a situacao: media >= 7 Aprovado, senao Reprovado
#     5) guardar tudo em um dicionario e imprimir a ficha do aluno
#   Ao final de cada aluno, perguntar se deseja cadastrar outro.
#   Quando encerrar, informar QUANTOS alunos foram cadastrados.
#
# Regras (validando o Modulo 01 inteiro):
#   - Combine while, for, if/else, dicionario, acumulador e validacao.
#
# Desafio logico (opcional):
#   Ao final, guarde cada ficha (dicionario) dentro de uma LISTA de
#   alunos e mostre quantos foram aprovados no total.
# ============================================================

# --- GABARITO DO PROFESSOR ---
alunos = []            # desafio: guarda todas as fichas
total_aprovados = 0

continuar = "sim"
while continuar.lower() == "sim":

    # 1) nome com validacao (nao pode ser vazio)
    while True:
        nome = input("Nome do aluno >> ").strip()
        if nome != "":
            break
        print("O nome nao pode ser vazio!")

    # 2) idade com validacao de numero
    while True:
        idade_texto = input("Idade >> ")
        if idade_texto.isdigit():
            idade = int(idade_texto)
            break
        print("Digite uma idade valida (numeros).")

    # 3) tres notas com acumulador dentro de um for
    soma = 0.0
    for n in range(1, 4):
        nota = float(input(f"Nota {n} >> "))
        soma = soma + nota
    media = soma / 3

    # 4) decide a situacao
    if media >= 7:
        situacao = "Aprovado"
        total_aprovados = total_aprovados + 1
    else:
        situacao = "Reprovado"

    # 5) monta o dicionario (a ficha) e imprime
    ficha = {
        "nome": nome,
        "idade": idade,
        "media": media,
        "situacao": situacao
    }
    alunos.append(ficha)

    print("--- FICHA DO ALUNO ---")
    for chave, valor in ficha.items():
        print(f"{chave}: {valor}")

    continuar = input("Cadastrar outro aluno? (sim/nao) >> ")

# relatorio final
print("=" * 30)
print(f"Total de alunos cadastrados: {len(alunos)}")
print(f"Total de aprovados: {total_aprovados}")

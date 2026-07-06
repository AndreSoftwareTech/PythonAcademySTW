# ============================================================
# EXERCICIO 50 - "A CALCULADORA A PROVA DE BALAS"
# Base: Aula 50 (Tratamento de erros: try / except)
# ------------------------------------------------------------
# Contexto:
#   Ate os melhores sistemas recebem dados errados. A diferenca e que
#   um programa profissional NAO QUEBRA: ele avisa educadamente e
#   segue em frente. Esse e o papel do try/except.
#
# Sua missao:
#   Peca dois numeros e mostre a divisao do primeiro pelo segundo.
#   Proteja o programa contra DOIS erros:
#     - o usuario digitar algo que nao e numero (ValueError)
#     - o usuario tentar dividir por zero (ZeroDivisionError)
#   Em cada caso, mostre uma mensagem clara em vez de travar.
#
# Regras (validando a Aula 50):
#   - Use try com dois except diferentes.
# ============================================================

# --- GABARITO DO PROFESSOR ---
try:
    a = float(input("Numerador >> "))
    b = float(input("Denominador >> "))
    print(f"Resultado: {a / b:.2f}")

except ValueError:
    print("Erro: digite apenas numeros validos.")

except ZeroDivisionError:
    print("Erro: nao da para dividir por zero.")

print("Obrigado por usar a calculadora!")

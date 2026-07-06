# ============================================================
# MODULO 02 - AULA 11: main.py (ponto de entrada)
# ------------------------------------------------------------
# Repare no import com PONTO: como o arquivo esta dentro da pasta
# 'controller', escrevemos  controller.pessoa_controller.
# Execute a partir desta pasta (aula11):  python main.py
# ============================================================

from controller.pessoa_controller import cadastrar, listar

print(cadastrar("Andre"))
print(cadastrar("Maria"))
print("Pessoas cadastradas:", listar())

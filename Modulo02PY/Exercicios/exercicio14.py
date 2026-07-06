# ============================================================
# EXERCICIO 14 - "O CADERNO BLINDADO (JSON)"
# Base: Aula 14 (Persistencia segura com json)
# ------------------------------------------------------------
# Contexto:
#   json e a forma profissional de salvar dados estruturados
#   (listas e dicionarios) sem os riscos do eval e sem quebrar
#   quando o dado contem virgulas.
#
# Sua missao:
#   Crie funcoes para uma agenda de contatos salva em contatos.json:
#     - adicionar(nome, telefone)  -> guarda um dicionario
#     - listar()                   -> le e devolve a lista de dicts
#   Adicione alguns contatos e liste.
#
# Regras (validando a Aula 14):
#   - Use json.load para ler e json.dump para gravar.
#   - Trate o caso de o arquivo ainda nao existir.
# ============================================================

# --- GABARITO DO PROFESSOR ---
import json

ARQUIVO = "contatos.json"

def _carregar():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def adicionar(nome, telefone):
    contatos = _carregar()
    contatos.append({"nome": nome, "telefone": telefone})
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(contatos, f, ensure_ascii=False, indent=2)

def listar():
    return _carregar()

adicionar("Andre", "48 99999-0000")
adicionar("Maria", "48 98888-1111")
print("Contatos:", listar())

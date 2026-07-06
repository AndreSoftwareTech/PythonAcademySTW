# ============================================================
# EXERCICIO 13 - "O CADASTRO DO BANCO"
# Base: Aula 13 (Cliente com to_dict/from_dict + JSON)
# ------------------------------------------------------------
# Contexto:
#   Objetos vivem na memoria; arquivos vivem no disco. Para
#   persistir clientes, convertemos o objeto em dicionario (to_dict),
#   salvamos em JSON, e reconstruimos com from_dict quando precisarmos.
#
# Sua missao:
#   1) Classe Cliente(titular, numero, saldo, limite) com to_dict()
#      e @classmethod from_dict(cls, dados).
#   2) Funcao cadastrar(cliente): carrega lista do JSON, adiciona
#      cliente.to_dict(), salva de volta.
#   3) Funcao listar(): le o JSON e imprime cada Cliente restaurado.
#
# Regras (validando a Aula 13):
#   - Use json.load/dump (NAO use eval()).
#   - Arquivo: "clientes.json". Se nao existir, comece com lista vazia.
#   - Cadastre pelo menos 2 clientes e liste todos.
#
# Desafio logico:
#   Implemente buscar_por_titular(nome) que devolve o Cliente ou None.
# ============================================================

# --- GABARITO DO PROFESSOR ---
import json

ARQUIVO = "clientes.json"


class Cliente:
    def __init__(self, titular, numero, saldo, limite):
        self.titular = titular
        self.numero = numero
        self.saldo = float(saldo)
        self.limite = float(limite)

    def to_dict(self):
        return {
            "titular": self.titular,
            "numero": self.numero,
            "saldo": self.saldo,
            "limite": self.limite,
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(dados["titular"], dados["numero"], dados["saldo"], dados["limite"])

    def __str__(self):
        return f"{self.titular} | Conta {self.numero} | R$ {self.saldo:.2f}"


def _carregar():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def _salvar(lista):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=2)


def cadastrar(cliente):
    dados = _carregar()
    dados.append(cliente.to_dict())
    _salvar(dados)


def listar():
    for item in _carregar():
        print(Cliente.from_dict(item))


def buscar_por_titular(nome):
    for item in _carregar():
        if item["titular"].lower() == nome.lower():
            return Cliente.from_dict(item)
    return None


cadastrar(Cliente("Andre", "001", 1500.00, 500.00))
cadastrar(Cliente("Maria", "002", 320.50, 200.00))

print("--- Clientes cadastrados ---")
listar()

encontrado = buscar_por_titular("Maria")
print("Busca Maria:", encontrado)
print("Busca Fulano:", buscar_por_titular("Fulano"))

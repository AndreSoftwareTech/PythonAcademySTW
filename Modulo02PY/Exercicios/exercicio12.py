# ============================================================
# EXERCICIO 12 - "O BLOCO DE NOTAS QUE NAO ESQUECE"
# Base: Aula 12 (Persistencia em arquivo txt)
# ------------------------------------------------------------
# Contexto:
#   Dados na memoria somem ao fechar o programa. Gravar em arquivo
#   faz a informacao sobreviver entre as execucoes.
#
# Sua missao:
#   Crie duas funcoes:
#     - salvar_produto(nome): grava um produto no arquivo produtos.txt
#     - listar_produtos(): le e devolve todos os produtos salvos
#   Salve alguns produtos e depois liste-os.
#
# Regras (validando a Aula 12):
#   - Use open() com 'a' para gravar e 'r' para ler.
#   - Use strip() ao ler para remover o \n.
# ============================================================

# --- GABARITO DO PROFESSOR ---
ARQUIVO = "produtos.txt"

def salvar_produto(nome):
    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome}\n")

def listar_produtos():
    produtos = []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                produtos.append(linha.strip())
    except FileNotFoundError:
        pass
    return produtos

salvar_produto("Teclado")
salvar_produto("Mouse")
print("Produtos salvos:", listar_produtos())

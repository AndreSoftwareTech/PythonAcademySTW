# ============================================================
# CAMADA VIEW (Apresentacao / Console)
# ------------------------------------------------------------
# E a UNICA camada que conversa com o usuario: usa input() e print().
# A View le os dados, entrega ao Controller e mostra a resposta.
# Ela NAO conhece regras de negocio e NAO conhece SQL.
# ============================================================

from controller.produto_controller import ProdutoController

controller = ProdutoController()


# ---------- Funcoes auxiliares de leitura segura ----------
# Aqui garantimos apenas o TIPO do dado (numero valido). As regras de
# negocio (preco negativo, nome vazio...) sao verificadas no Service.

def ler_texto(mensagem):
    return input(mensagem)


def ler_int(mensagem):
    while True:
        valor = input(mensagem)
        try:
            return int(valor)
        except ValueError:
            print("  >> Valor invalido. Digite um numero inteiro.")


def ler_float(mensagem):
    while True:
        valor = input(mensagem).replace(",", ".")
        try:
            return float(valor)
        except ValueError:
            print("  >> Valor invalido. Digite um numero (ex.: 9.90).")


# ---------- Acoes do menu ----------

def acao_cadastrar():
    print("\n--- Cadastrar produto ---")
    nome = ler_texto("Nome: ")
    preco = ler_float("Preco: ")
    quantidade = ler_int("Quantidade: ")
    print(controller.cadastrar(nome, preco, quantidade))


def acao_listar():
    print("\n--- Lista de produtos ---")
    produtos = controller.listar()
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for produto in produtos:
            print(produto)


def acao_buscar():
    print("\n--- Buscar produto ---")
    id = ler_int("Digite o id do produto: ")
    print(controller.buscar(id))


def acao_atualizar():
    print("\n--- Atualizar produto ---")
    id = ler_int("Digite o id do produto: ")
    nome = ler_texto("Novo nome: ")
    preco = ler_float("Novo preco: ")
    quantidade = ler_int("Nova quantidade: ")
    print(controller.atualizar(id, nome, preco, quantidade))


def acao_remover():
    print("\n--- Remover produto ---")
    id = ler_int("Digite o id do produto: ")
    print(controller.remover(id))


# ---------- Laco principal do menu ----------

def iniciar():
    opcao = -1
    while opcao != 0:
        print("\n===== LOJA - CADASTRO DE PRODUTOS =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Buscar produto por id")
        print("4 - Atualizar produto")
        print("5 - Remover produto")
        print("0 - Sair")

        opcao = ler_int("Escolha uma opcao: ")

        if opcao == 1:
            acao_cadastrar()
        elif opcao == 2:
            acao_listar()
        elif opcao == 3:
            acao_buscar()
        elif opcao == 4:
            acao_atualizar()
        elif opcao == 5:
            acao_remover()
        elif opcao == 0:
            print("Encerrando o sistema. Ate logo!")
        else:
            print("Opcao invalida. Tente novamente.")

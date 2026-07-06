# ============================================================
# EXERCICIO 13 - "A BIBLIOTECA DIGITAL"
# Base: Aula 13 (CRUD completo em arquivo txt)
# ------------------------------------------------------------
# Contexto:
#   Uma biblioteca precisa cadastrar, listar, atualizar e remover
#   livros - e nao pode perder os dados. Este e o CRUD completo.
#
# Sua missao:
#   Crie as 4 operacoes para livros, salvando em livros.txt com os
#   campos separados por virgula (titulo,autor):
#     - create(titulo, autor)
#     - read()  -> lista de livros
#     - update(titulo, novo_titulo, novo_autor)
#     - delete(titulo)
#   Faca uma demonstracao usando as 4 operacoes.
#
# Regras (validando a Aula 13):
#   - NAO use eval(). Separe/junte os campos com virgula (split/join).
# ============================================================

# --- GABARITO DO PROFESSOR ---
ARQUIVO = "livros.txt"

def create(titulo, autor):
    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{titulo},{autor}\n")

def read():
    livros = []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                livros.append(linha.strip().split(","))
    except FileNotFoundError:
        pass
    return livros

def update(titulo, novo_titulo, novo_autor):
    livros = read()
    encontrou = False
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        for dados in livros:
            if dados[0].lower() == titulo.lower():
                arquivo.write(f"{novo_titulo},{novo_autor}\n")
                encontrou = True
            else:
                arquivo.write(",".join(dados) + "\n")
    return encontrou

def delete(titulo):
    livros = read()
    encontrou = False
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        for dados in livros:
            if dados[0].lower() == titulo.lower():
                encontrou = True
            else:
                arquivo.write(",".join(dados) + "\n")
    return encontrou

# Demonstracao:
create("Dom Casmurro", "Machado de Assis")
create("1984", "George Orwell")
print("Apos cadastrar:", read())
update("1984", "1984 (edicao especial)", "George Orwell")
print("Apos atualizar:", read())
delete("Dom Casmurro")
print("Apos remover:", read())

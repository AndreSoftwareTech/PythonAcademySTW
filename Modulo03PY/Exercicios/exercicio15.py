# ============================================================
# EXERCICIO 15 - "BOSS FINAL: O DIRETOR DA ACADEMIA"
# Base: Aula 15 (Mini projeto: Aluno + CRUD em memoria)
# ------------------------------------------------------------
# Contexto:
#   Este e o boss final do Modulo 03. Voce junta OOP, encapsulamento,
#   propriedades e um mini-sistema com menu: cadastrar alunos, listar
#   e calcular a media geral — tudo em memoria, sem banco de dados.
#
# Sua missao (a lenda):
#   A "Python Academy" precisa de um diretor digital. Implemente:
#     1) Classe Aluno(nome, nota) com atributos privados, property
#        situacao ("Aprovado" se nota >= 7, senao "Reprovado") e __str__.
#     2) Lista global _alunos em memoria.
#     3) cadastrar(nome, nota): valida nota 0-10, cria Aluno, append.
#     4) listar(): retorna a lista (ou mensagem se vazia).
#     5) media_geral(): media das notas ou aviso se ninguem cadastrado.
#     6) Menu interativo com opcoes 1-cadastrar, 2-listar, 3-media, 0-sair.
#
# Regras (validando o Modulo 03 inteiro):
#   - Combine classe, encapsulamento, validacao e while de menu.
#   - Nota invalida deve ser rejeitada com mensagem clara.
#
# Desafio logico (opcional):
#   Opcao extra no menu: contar quantos alunos estao Aprovados.
# ============================================================

# --- GABARITO DO PROFESSOR ---
_alunos = []


class Aluno:
    def __init__(self, nome, nota):
        self.__nome = nome
        self.__nota = float(nota)

    @property
    def nome(self):
        return self.__nome

    @property
    def nota(self):
        return self.__nota

    @property
    def situacao(self):
        return "Aprovado" if self.__nota >= 7 else "Reprovado"

    def __str__(self):
        return f"{self.nome} | Nota {self.nota:.1f} | {self.situacao}"


def cadastrar(nome, nota):
    nota = float(nota)
    if nota < 0 or nota > 10:
        return "Nota invalida! Use um valor entre 0 e 10."
    _alunos.append(Aluno(nome.strip(), nota))
    return f"Aluno {nome} cadastrado."


def listar():
    if not _alunos:
        return "Nenhum aluno cadastrado."
    return _alunos


def media_geral():
    if not _alunos:
        return "Nenhum aluno cadastrado."
    media = sum(a.nota for a in _alunos) / len(_alunos)
    return f"Media geral: {media:.2f}"


def total_aprovados():
    if not _alunos:
        return "Nenhum aluno cadastrado."
    qtd = sum(1 for a in _alunos if a.situacao == "Aprovado")
    return f"Total de aprovados: {qtd}"


def menu():
    opcao = -1
    while opcao != 0:
        print("\n=== ACADEMIA - DIRETOR DIGITAL ===")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Media geral")
        print("4 - Total de aprovados")
        print("0 - Sair")
        opcao = int(input("Opcao >> "))

        if opcao == 1:
            print(cadastrar(input("Nome >> "), input("Nota >> ")))
        elif opcao == 2:
            resultado = listar()
            if isinstance(resultado, str):
                print(resultado)
            else:
                for aluno in resultado:
                    print(aluno)
        elif opcao == 3:
            print(media_geral())
        elif opcao == 4:
            print(total_aprovados())
        elif opcao == 0:
            print("Encerrando... Diretor aprovado no Modulo 03!")
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    menu()

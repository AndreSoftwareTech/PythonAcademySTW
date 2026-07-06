# ============================================================
# EXERCICIO 04 - "DUAS FORMAS DE NASCER"
# Base: Aula 04 (Tres formas de criar uma classe)
# ------------------------------------------------------------
# Contexto:
#   Existem varios jeitos de montar um cadastro de pessoa em Python.
#   Alguns sao seguros (tudo no __init__), outros sao flexiveis mas
#   arriscados (objeto vazio que voce preenche depois). Entender a
#   diferenca evita bugs silenciosos em producao.
#
# Sua missao:
#   Implemente e COMPARE duas abordagens:
#     1) Classe PessoaCompleta com __init__(self, nome, sobrenome, idade, peso)
#        que atribui tudo a self na hora da criacao.
#     2) Classe PessoaVazia com __init__(self) vazio (pass).
#        Depois de criar o objeto, atribua nome, sobrenome, idade e peso manualmente.
#     3) Crie uma instancia de cada classe com os MESMOS dados.
#     4) Imprima os atributos das duas e comente qual abordagem e mais segura.
#
# Regras (validando a Aula 04):
#   - Use snake_case nos nomes dos atributos (nome, sobrenome, idade, peso).
#   - PessoaCompleta: nenhum atributo pode ficar de fora do __init__.
#   - PessoaVazia: atributos entram DEPOIS, com notacao ponto (obj.atributo = valor).
#
# Desafio logico:
#   Tente acessar pessoa_vazia.idade ANTES de atribuir idade.
#   O que acontece? Por que PessoaCompleta nao tem esse problema?
# ============================================================

# --- GABARITO DO PROFESSOR ---
class PessoaCompleta:
    def __init__(self, nome, sobrenome, idade, peso):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = int(idade)
        self.peso = float(peso)


class PessoaVazia:
    def __init__(self):
        pass


pessoa_ok = PessoaCompleta("Carlos", "Mendes", 28, 74.5)

pessoa_manual = PessoaVazia()
pessoa_manual.nome = "Carlos"
pessoa_manual.sobrenome = "Mendes"
pessoa_manual.idade = 28
pessoa_manual.peso = 74.5

print("--- PessoaCompleta (segura) ---")
print(pessoa_ok.nome, pessoa_ok.sobrenome, pessoa_ok.idade, pessoa_ok.peso)

print("--- PessoaVazia (flexivel, mas arriscada) ---")
print(pessoa_manual.nome, pessoa_manual.sobrenome, pessoa_manual.idade, pessoa_manual.peso)

print("Abordagem recomendada: PessoaCompleta — dados obrigatorios desde o nascimento.")

# Desafio: descomente a linha abaixo e veja o AttributeError
# print(PessoaVazia().idade)

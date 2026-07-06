# ============================================================
# EXERCICIO 07 - "PRODUTO COM FACHADA ELEGANTE"
# Base: Aula 07 (Encapsulamento com @property)
# ------------------------------------------------------------
# Contexto:
#   Getters e setters funcionam, mas ficam verbosos: produto.get_preco().
#   O decorador @property permite tratar metodos como ATRIBUTOS — voce
#   escreve produto.preco, mas por baixo dos panos roda validacao.
#   E a forma pythonica de encapsular sem sacrificar legibilidade.
#
# Sua missao:
#   Modele um Produto de loja online com @property:
#     1) Atributos privados: __nome, __preco, __estoque.
#     2) @property nome — somente leitura apos criacao.
#     3) @property preco + @preco.setter — rejeita preco <= 0.
#     4) @property estoque + @estoque.setter — rejeita estoque negativo.
#     5) Metodo disponivel(self) retornando True se estoque > 0.
#     6) __str__ mostrando nome, preco formatado e status de disponibilidade.
#     7) Teste leitura, alteracao valida e tentativa de preco invalido.
#
# Regras (validando a Aula 07):
#   - Use @property e @atributo.setter (nao get_/set_ neste exercicio).
#   - Acesso externo: produto.preco = 99.90 (sem parenteses).
#   - Setters silenciosamente ignoram valores invalidos ou exibem mensagem.
#
# Desafio logico:
#   Por que @property e preferivel a get_preco()/set_preco() em APIs publicas?
# ============================================================

# --- GABARITO DO PROFESSOR ---
class Produto:
    def __init__(self, nome, preco, estoque):
        self.__nome = nome
        self.__preco = float(preco)
        self.__estoque = int(estoque)

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor > 0:
            self.__preco = float(valor)
        else:
            print("Preco deve ser maior que zero.")

    @property
    def estoque(self):
        return self.__estoque

    @estoque.setter
    def estoque(self, valor):
        if valor >= 0:
            self.__estoque = int(valor)
        else:
            print("Estoque nao pode ser negativo.")

    def disponivel(self):
        return self.__estoque > 0

    def __str__(self):
        status = "Disponivel" if self.disponivel() else "Esgotado"
        return f"{self.nome} | R$ {self.preco:.2f} | {status} ({self.estoque} un.)"


produto = Produto("Teclado Mecanico", 349.90, 12)

print(produto)
print("Nome:", produto.nome)

produto.preco = 299.90
produto.estoque = 0
produto.preco = -10          # deve rejeitar

print(produto)

# Desafio: @property mantem a sintaxe limpa (obj.atributo) com validacao por tras.

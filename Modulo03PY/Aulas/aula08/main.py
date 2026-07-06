# ============================================================
# MODULO 03 - AULA 08: MAIN (heranca em acao)
# ============================================================

from contas import PessoaFisica, PessoaJuridica

pf = PessoaFisica("1001", "Ana Costa", "111.222.333-44", 2500.0)
pj = PessoaJuridica("2001", "Tech Solutions LTDA", "12.345.678/0001-99", 50000.0)

print(pf)
print(pj)

# Ambas sao ContaBancaria (heranca), mas com dados diferentes:
print("Tipo PF:", pf.tipo)
print("Tipo PJ:", pj.tipo)

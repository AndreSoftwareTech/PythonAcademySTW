from controller import saudacao, checkin, relatorio, relatorioCliente, update, delete

saudacao()

# pessoa = {}
# pessoa['nome'] = input("Digite seu nome >>")
# pessoa['cpf'] = input("Digite seu cpf >>")
# pessoa['idade'] = input("Digite sua idade >>")
# pessoa['telefone'] = input("Digite seu telefone >>")

# checkin(pessoa)

# pessoa = input("Digite o nome que desja buscar >> ")
# relatorioCliente(pessoa)
# pessoa = {}
# pessoa['nome'] = input("Digite o novo nome: ")
# pessoa['idade'] = input("Digite a nova idade: ")
# update(pessoa)
cliente_find = input("Informe o nome do cliente a ser atualizado: ")
update(cliente_find)

pessoa = input("Informe o nome do cliente a ser deletado: ")
delete(pessoa)
from time import sleep

situacao = "Reprovado"

while situacao == "Reprovado":

#### bloco 1
#variaveis recebendo dados
    nome = input("Digite o Seu Nome >> ")
    sobre_nome = input("Digite Seu Sobre Nome >> ")
    idade = int(input("Digite Sua Idade >> "))

    lista_notas = []

### bloco 2
    for lista in range(0,4):
        nota = float(input("Digite Sua Nota >> "))
        lista_notas.append(nota)

    media = sum(lista_notas) / len(lista_notas)
### bloco 3
    if media < 7:
        situacao = "Reprovado"
        print(f"Infelizmente voce foi { situacao } seu Bobao  sua nota foi {media}")

    if media >= 7:

        for c in range(0, 10):
            print("*")
            sleep(2)
            
        situacao = "Aprovado"
        print("Parabens Voce Foi {} O mundo e pequeno para voce ".format(situacao))
    
        dicionario ={
            "Nome": nome,
            "SobreNome": sobre_nome,
            "Idade": idade,
            "ListaNotas": lista_notas,
            "Media": media,
            "Situacao": situacao
        }
    
        var = input("Voce deseja ter um relatorio completo do aluno\nSim \nNao\n >>")

        if var == "sim":

            print(f'''{dicionario['Nome']} 
            \n{dicionario['SobreNome']} 
            \n{dicionario['Idade']} 
            \n{dicionario['ListaNotas']} 
            \n{dicionario['Media']} 
            \n{dicionario['Situacao']}''')
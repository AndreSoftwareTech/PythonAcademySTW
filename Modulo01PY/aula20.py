nivel = int(input("Digite o seu nível de experiência (entre 1 e 10): "))

if nivel < 1:
    mensagem = "Nível inválido. O nível deve ser entre 1 e 10."
elif nivel <= 3:
    mensagem = "Iniciante. Continue praticando para melhorar suas habilidades."
elif nivel <= 6:
    mensagem = "Intermediário. Você está progredindo bem!"
elif nivel <= 9:
    mensagem = "Avançado. Você é um jogador habilidoso!"
else:
    mensagem = "Mestre. Seu nível de experiência é impressionante!"

print("Mensagem:", mensagem)


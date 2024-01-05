def create(nome):
    
    with open('pessoas.txt', 'a') as arquivo:
        arquivo.write(f'{nome}\n')

def read():
    nomes = []
    with open('pessoas.txt', 'r') as arquivo:
        for name in arquivo:
            name = name.strip()
            nomes.append(name)

    return nomes
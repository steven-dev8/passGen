def write(password: str):
    arquivo = open('genpass.txt', 'a')
    arquivo.write(password + ' ')
    arquivo.close()


def read():
    try:
        arquivo = open('genpass.txt', 'r')
    except:
        arquivo = open('genpass.txt', 'a')
        arquivo = open('genpass.txt', 'r')
    conteudo = arquivo.read()
    arquivo.close()

    return conteudo


def listar(conteudo):
    if ' ' in conteudo:
        lista = conteudo.split(' ')

        print('NUM    PASSWORD')
        for i, j in enumerate(lista):
            print(f'\033[32m{i}      \033[33m{j}\033[0m')
        print('-=' * 28)
    else:
        print('\033[32mAINDA NÃO FORAM GERADA SENHAS\033[0m')

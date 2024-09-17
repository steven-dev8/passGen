import passGen
import menuGen
import listaGen
from time import sleep

print(menuGen.menu_ascii())
menuGen.menu()

while True:
    select = menuGen.quest_menu()

    if select == '1':
        amount = passGen.quest_amount()
        ALPHA = passGen.quest_alpha()
        NUMERIC = passGen.quest_numeric()
        SPECIAL = passGen.quest_special()

        password = passGen.gen_password(amount, ALPHA, NUMERIC, SPECIAL)
        if 'ERRO' in password:
            pass
        else:
            listaGen.write(password)

        print(f'\033[34mSENHA GERADA:\033[0m \033[32m{password}\033[0m')
    elif select == '2':
        menuGen.menu_lista()
        conteudo = listaGen.read()
        listaGen.listar(conteudo)
    
    else:
        print('ENCERRANDO O PROGRAMA...')
        sleep(0.5)
        break

    print()
    sleep(0.5)
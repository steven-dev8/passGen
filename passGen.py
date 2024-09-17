from random import shuffle, choice

ERRO_CODE = '\033[31mERRO: DIGITE APENAS S ou N!!!\033[0m'


def quest_amount():
    while True:
        try:
            quantidade_caracteres = int(input('Digite a quantidade de caracteres para a password: '))
        except:
            print('\033[31mERRO: Digite uma quantidade inteira válida.\033[0m')
        else:
            if quantidade_caracteres >= 4:
                return quantidade_caracteres
            else:
                print('\033[31mERRO: Mínimo de caracteres "4"\033[0m')


def quest_alpha():
    while True:
        alpha = input('Deseja adicionar caracteres alfabéticos? [S/N]: ').upper()[0]

        if alpha == 'S':
            return True
        elif alpha == 'N':
            return False
        else:
            print(ERRO_CODE)


def quest_numeric():
    while True:
        numeric = input('Deseja adicionar caracteres numéricos? [S/N]: ').upper()[0]
    
        if numeric == 'S':
            return True
        elif numeric == 'N':
            return False
        else:
            print(ERRO_CODE)


def quest_special():
    while True:
        special = input('Deseja adicionar caracteres especiais: [S/N]: ').upper()[0]

        if special == 'S':
            return True
        elif special == 'N':
            return False
        else:
            print(ERRO_CODE)


def gen_password(amount: int, alpha: bool, numeric: bool, special: bool):
    alpha_char = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    numeric_char = '0123456789'
    special_char = r"!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    
    if alpha and numeric and special:
        alpha_char = [n for n in alpha_char]
        shuffle(alpha_char)
        numeric_char = [n for n in numeric_char]
        shuffle(numeric_char)
        special_char = [n for n in special_char]
        shuffle(special_char)

        all_caracteres = alpha_char + numeric_char + special_char
        shuffle(all_caracteres)

        gen_pass = [alpha_char[0], numeric_char[0], special_char[0]]

        while len(gen_pass) < amount:
            gen_pass.append(choice(all_caracteres))
            shuffle(all_caracteres)
        
        shuffle(gen_pass)
        
        return ''.join(gen_pass)
    
    elif alpha and numeric:
        alpha_char = [n for n in alpha_char]
        shuffle(alpha_char)
        numeric_char = [n for n in numeric_char]
        shuffle(numeric_char)

        all_caracteres = alpha_char + numeric_char
        shuffle(all_caracteres)

        gen_pass = [alpha_char[0], numeric_char[0]]

        while len(gen_pass) < amount:
            gen_pass.append(choice(all_caracteres))
            shuffle(all_caracteres)
        
        shuffle(gen_pass)
        
        return ''.join(gen_pass)
    
    elif alpha and special:
        alpha_char = [n for n in alpha_char]
        shuffle(alpha_char)
        special_char = [n for n in special_char]
        shuffle(special_char)

        all_caracteres = alpha_char + special_char
        shuffle(all_caracteres)

        gen_pass = [alpha_char[0], special_char[0]]

        while len(gen_pass) < amount:
            gen_pass.append(choice(all_caracteres))
            shuffle(all_caracteres)
        
        shuffle(gen_pass)
        
        return ''.join(gen_pass)
    
    elif numeric and special:
        numeric_char = [n for n in numeric_char]
        shuffle(numeric_char)
        special_char = [n for n in special_char]
        shuffle(special_char)

        all_caracteres = numeric_char + special_char
        shuffle(all_caracteres)

        gen_pass = [numeric_char[0], special_char[0]]

        while len(gen_pass) < amount:
            gen_pass.append(choice(all_caracteres))
            shuffle(all_caracteres)
        
        shuffle(gen_pass)
        
        return ''.join(gen_pass)
    
    elif alpha:
        alpha_char = [n for n in alpha_char]
        shuffle(alpha_char)

        gen_pass = [alpha_char[0]]

        while len(gen_pass) < amount:
            gen_pass.append(choice(alpha_char))
            shuffle(alpha_char)
        
        shuffle(gen_pass)
        
        return ''.join(gen_pass)
    
    elif numeric:
        numeric_char = [n for n in numeric_char]
        shuffle(numeric_char)

        gen_pass = [numeric_char[0]]

        while len(gen_pass) < amount:
            gen_pass.append(choice(numeric_char))
            shuffle(numeric_char)
        
        shuffle(gen_pass)
        
        return ''.join(gen_pass)
    
    elif special:
        special_char = [n for n in special_char]
        shuffle(special_char)

        gen_pass = [special_char[0]]

        while len(gen_pass) < amount:
            gen_pass.append(choice(special_char))
            shuffle(special_char)
        
        shuffle(gen_pass)
        
        return ''.join(gen_pass)
    
    else:
        return '\033[31mERRO: Impossivel gerar senha sem parâmetros verdadeiros.\033[0m'

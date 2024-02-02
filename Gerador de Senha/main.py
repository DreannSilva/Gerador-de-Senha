import random
import string
import os
import time

os.system('clear')
key = True

while key:

    print('\nBem vindo ao Gerador de Senhas 1.0, para continuar escreva a quantidade de caracteres deseja colocar na senha.\n')

    tamanho = int(input(f'Qual a quantidade de caracteres gostaria de ter na senha? '))
        
    def senha(lenght=tamanho):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(lenght))
        return password

    if __name__ == "__main__":
        password = senha()
        print('Gerando senha...')
        time.sleep(0.4)
        print(f'Senha gerada: {password}')

    choice = input('Gostaria de continuar? S ou N: ')

    if choice == "S":
        key = True
    elif choice == "N":
        key = False
    else:
        print('Comando não identificado, encerrando programa...')
        time.sleep(1)
        key = False
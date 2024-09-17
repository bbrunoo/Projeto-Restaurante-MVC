import os

def introduction_menu():
    message = '''
        Sistema Restaurante

        * Cadastrar restaurante - 1
        * Cadastrar clientes - 2
        * Utilitario - 3
        * Sair - 5

    '''
    
    print(message)    
    command = str(input('Comando:'))
    return command


def menu() -> None:
    command = introduction_menu()
    while True:

        if command == '1':
            print("opcao 1")
            input()
        elif command == '2':
            ()
        elif command == '3': 
            ()
        elif command == '5':
            exit()
        else: print('\n Comando nao encontrado!! \n\n')
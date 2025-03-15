import os


def exibir_nome_do_programa():
    print(
        """
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
"""
    )


def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair\n")


def finalizar_app():
    os.system("cls")
    # os.system('clear')
    print("Finalizando o app")


def opcao_errada():
    print("Opção inválida...")
    input("digite uma tecla para poder continuar: ")
    input() #para dar tempo ao usuário
    main()

def cansou():
    input("digite uma tecla para poder sair: ")
    main()

restaurantes = []

def cadastrar_restaurante():
    
    os.system('cls')
    print("Cadastro de novos restaurantes")
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado.')
    print('Digite uma tecla para voltar ao menu principal... ')
    main()

def listar_restaurantes():
    os.system('cls')
    print('Segue a lista: ')
    if len(restaurantes) == 0:
        print('Nenhum restaurante cadastrado ainda')
    for restaurante in restaurantes:
        print(f'{restaurante}')
    print('\nDigite uma tecla para voltar ao menu principal... ')
    main()


def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
       

        if opcao_escolhida == 1:
            print("\nCadastrar restaurante")
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            print("\nListar restaurantes")
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print("\nAtivar restaurante")
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_errada()
    except:
        print("\nTenta mais uma vez...eu sei q vc consegue !")
        opcao_errada()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()

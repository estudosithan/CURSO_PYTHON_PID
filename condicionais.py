import os  # Para importar módulo do sistema que limpa o terminal
import sys  # Para importar módulo do sistema

# os.system("cls") método que limpa o terminal

print("1 - Comer")
print("2 - Estudar")
escolha = int(input("Escolhe patrão: "))

# para "colher" dados string é só deixar o input lá


def finaliza_app(escolha):  # function
    if escolha != 1 and escolha != 2:
        print("Vazando...")
        sys.exit()  # Para utilizar método de sair do sistema do módulo sys


if escolha != 1 and escolha != 2:
    finaliza_app(escolha)

if escolha == 1:
    print(f"Sério ? {escolha} ? Então tá né....😒")
if escolha == 2:
    print(f"Opa ! Bora estudar então 😁")

print(
    escolha == 1
)  # Vai sair false mesmo que o usuário digite 1, pq "escolha" é string e 1 é do tipo int
print(type(escolha))  # mostra que tipo de dado está sendo exibido, no caso str
print(type(1))  # exibe int
print(type(1.1))  # exibe float


def configurar_tempo_foco():
    tempo = int(input("Digite o tempo de foco (25-45 min): "))
    if 25 <= tempo <= 45:
        print("Tempo configurado para", tempo, "minutos.")
    else:
        print("Valor inválido. Configure um tempo entre 25 e 45 minutos.")


configurar_tempo_foco()  # não usa dado externo, fora do escorpo do método, por isso não tem parâmetro

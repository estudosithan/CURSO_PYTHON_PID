
nome = input('Qual o seu nome ?\n')
altura = float(input(f'{nome}, digita sua altura em metros ai patrão: '))
peso = float(input('Digita seu peso ai papis: '))
IMC = peso / altura ** 2
print(f'O IMC de {nome} é: {IMC:.2f}')



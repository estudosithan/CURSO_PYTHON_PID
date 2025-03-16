entrada = input("Fala paizão, você quer continuar ? ")


if entrada == "sim" or entrada == "s":
    print("Voce entrou no sistema")

elif entrada == "não" or entrada == "n":
    print("Voce saiu do sistema")

elif entrada == "sim" or entrada == "s":
    print(
        "É...funciona"
    )  # não vai exibir, por que a primeira condição dele ja foi satisfeita, logo ele sai de todos os loops

else:
    print("Você não digitou uma opção válida")


print("Ehhhh laia")

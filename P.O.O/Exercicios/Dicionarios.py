_dict = {"cidade": "belo Horizonte", "Bairro": "Estoril", "Rua": "Mário Coutinho"}

# print(_dict['cidade'])

tile_anottations = {
    "casa": {"Cidade": "belo Horizonte", "Bairro": "Estoril", "Rua": "Mário Coutinho"},
    "sorvete": "maracujá",
    "refrigerante": "coca-cola",
}
# print(tile_anottations['casa']['bairro'])

# Passando valor de chave encadeada com variável
variavel = tile_anottations["casa"]["Rua"]
print(variavel)
_dict.update({"    Bairro": variavel})
print(_dict)

# Passando valor de chave encadeada sem variável
_dict.update({"Bairro": tile_anottations["casa"]["Rua"]})
print(_dict)

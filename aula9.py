# Aula 9 - Dicionários
# Objetivo: Guardar dados em formato chave:valor

pessoa = {
    "nome": "Júlio",
    "idade": 35,
    "cidade": "Porto"
}

print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

pessoa["idade"] = 36
print("Idade atualizada:", pessoa["idade"])

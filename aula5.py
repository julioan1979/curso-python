# Aula 5 - Condições (if, elif, else)
# Objetivo: Tomar decisões com base em condições

idade = int(input("Qual é a sua idade? "))

if idade < 18:
    print("Você é menor de idade.")
elif idade < 65:
    print("Você é adulto.")
else:
    print("Você é sénior.")

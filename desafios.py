# desafios.py
# Desafios práticos para treinar os conceitos das Aulas 1 a 10

# Aula 1 – print()
# Desafio: Mostrar o teu nome, idade e uma frase favorita
print("Nome: Júlio")
print("Idade: 35")
print("Frase favorita: Nunca pares de aprender.")

# Aula 2 – Variáveis e tipos
# Desafio: Criar variáveis e imprimir uma frase formatada
nome = "Júlio"
idade = 35
altura = 1.78
programador = True
print(f"Olá, sou o {nome}, tenho {idade} anos, {altura}m e gosto de programar? {programador}")

# Aula 3 – Operações matemáticas
# Desafio: Calcular o total de uma compra
preco = 12.5
quantidade = 4
total = preco * quantidade
print("Total da compra:", total)

# Aula 4 – input()
# Desafio: Perguntar o nome e ano de nascimento e calcular a idade
nome = input("Qual é o seu nome? ")
ano_nascimento = int(input("Em que ano nasceste? "))
idade = 2025 - ano_nascimento
print(f"Olá, {nome}! Tens {idade} anos.")

# Aula 5 – Condições
# Desafio: Dizer se a pessoa é menor, adulta ou sénior
idade = int(input("Qual é a sua idade? "))
if idade < 18:
    print("Menor de idade")
elif idade < 65:
    print("Adulto")
else:
    print("Sénior")

# Aula 6 – while
# Desafio: Contar de 1 até um número informado
fim = int(input("Contar até: "))
contador = 1
while contador <= fim:
    print(contador)
    contador += 1

# Aula 7 – for e range
# Desafio: Tabuada de um número
num = int(input("Número para tabuada: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Aula 8 – listas
# Desafio: Criar lista com 5 frutas e mostrar todas
frutas = ["maçã", "banana", "uva", "pera", "laranja"]
for fruta in frutas:
    print("Fruta:", fruta)

# Aula 9 – dicionários
# Desafio: Criar dicionário com informações de uma pessoa
pessoa = {"nome": "Ana", "idade": 28, "cidade": "Porto"}
print(f"{pessoa['nome']} tem {pessoa['idade']} anos e vive em {pessoa['cidade']}.")

# Aula 10 – funções
# Desafio: Criar função para calcular a média de 3 notas
def media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

print("Média:", media(14, 16, 15))

# Peça a idade do usuário com base na idade fornecida, o programa deve
# classificar a pessoa em uma das seguintes categorias:
# Se a idade for menor que 12 anos, imprimir"Criança".
# Se a idade estiver entre 12 e 17 anos (inclusive), imprimir "Adolescente".
# Se a idade estiver entre 18 e 59 anos (inclusive), imprimir "Adulto".
# Se a idade for igual ou superior a 60 anos, imprimir "Idoso".

idade_usuario = int(input("Por favor Digite sua Idade: "))

if idade_usuario < 12:
    print("Você é Criança.")
elif idade_usuario >= 12 and idade_usuario <= 17:
    print("Você é Adolecente.")
elif idade_usuario >= 18 and idade_usuario <= 59:
    print("Você é Adulto.")
else:
    print("Você é Idoso(a).")


# Faça um programa que leia 3 números e informe o
# maior número e o menor.

numero_1 = float(input("Digite o primeiro numero: "))
numero_2 = float(input("digite o segundo numero: "))
numero_3 = float(input("Digite o terceiro numero: "))

maior = numero_1
menor = numero_1

if numero_2 > maior:
    maior = numero_2
if numero_2 < menor:
    menor = numero_2

if numero_3 > maior:
    maior = numero_3
if numero_3 < menor:
    menor = numero_3

print(f"O maior numero é: {maior}, \nE o menor numero é: {menor}.")


# Faça um programa que peça 10 números inteiros,
# calcule e mostre a quantidade de números pares e a
# quantidade de números impares.

quantidade_pares = 0
quantidade_impares = 0

for num in range(1, 11):
    numero = int(input("Digite o {num}º numero: "))

    if numero % 2 == 0:
        quantidade_pares += 1

    else:
        quantidade_impares += 1

print(f"Quantidades de numeros Pares: {quantidade_pares}.")
print(f"Quantidades de numeros Impares: {quantidade_impares}.")


# Faça um programa que peça para n pessoas a sua
# idade, ao final o programa devera verificar se a média
# de idade da turma varia entre 0 e 25, 26 e 60 e maior
# que 60; e então, dizer se a turma é jovem, adulta ou
# idosa, conforme a média calculada.

quantidade_pessoas = int(input("Quantas pessoas a na Turma? \n"))
soma_idade = 0

for n in range(quantidade_pessoas):
    idade = int(input(f"Digite a idade da Pessoa {n+1}: "))
    soma_idade += idade
    media_idade = soma_idade / quantidade_pessoas

if 0 <= media_idade <= 25:
    classificacao = "jovem"

elif 26 <= media_idade <= 60:
    classificacao = "Adulto"

else:
    classificacao = "Idoso"

print(f"A media de idade da turma é {media_idade}.")
print(f"A turma e considerada {classificacao}.")



# Faça um programa que, dado um conjunto de N
# números, determine o menor valor, o maior valor e a
# soma dos valores.

numero_01 = int(input("Digite o primeiro numero: "))
numero_02 = int(input("Digite o segundo numero: "))
numero_03 = int(input("Digite o terceiro numero: "))
maior = numero_01
menor = numero_02

soma = numero_01 + numero_02 + numero_03

if numero_02 > maior:
    maior = numero_02
if numero_02 < menor:
    menor = numero_02

if numero_03 > maior:
    maior = numero_03
if numero_03 < menor:
    menor = numero_03

print(f"O maior numero é: {maior} \nE o menor numero é: {menor}")
print(f"A soma dos numeros: {soma}")




# Gerenciamento de Compras de Produtos
# Você foi contratado para desenvolver um programa simples para
# auxiliar em um processo de compra de produtos. O programa deve
# permitir ao usuário inserir o nome e o preço de vários produtos,
# perguntando se deseja continuar inserindo mais produtos após cada
# entrada. Ao final, o programa deve fornecer um resumo da compra, incluindo:
# A) O total gasto na compra.
# B) A quantidade de produtos que custam mais de R$1000.
# C) O nome do produto mais barato.
# Desenvolva o programa em Python utilizando conceitos de
# entrada/saída de dados, condicionais e laços de repetição.

total_gasto = 0
produtos_acima_1000 = 0
produto_mais_barato = ""
preco_mais_barato = None

while True:
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input(f"Digite o preço de '{nome_produto}': R$ "))

    total_gasto += preco_produto

    if preco_produto > 1000:
        produtos_acima_1000 += 1

    if preco_mais_barato is None or preco_produto < preco_mais_barato:
        preco_mais_barato = preco_produto
        produto_mais_barato = nome_produto

    continuar = input("Deseja continuar inserindo produtos? (S/N): ").strip().upper()
    if continuar == "N":
        break

print("\n==== Resumo da Compra ====")
print(f"Total gasto: R$ {total_gasto:.2f}")
print(f"Quantidade de produtos acima de R$1000: {produtos_acima_1000}")
print(f"Produto mais barato: '{produto_mais_barato}' custando R$ {preco_mais_barato:.2f}")

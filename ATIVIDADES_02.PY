# Crie um conjunto vazio chamado frutas e adicione as
# seguintes frutas a ele:"maçã","banana"uva "laranja" e "morango". 
# Em seguida, imprima o conjunto.

frutas = {"maçã", "banana", "uva", "laranja", "morango"}
print(frutas)

# Verifique se a fruta
# "banana"está presente no conjunto
# frutas e imprima o resultado.

if "banana" in frutas:
    print("a fruta banana foi encontrada.")
else:
    print("fruta nao encontrada.")


# Crie um conjunto chamado frutas_vermelhas e adicione
# as seguintes frutas a ele:"morango","cereja"e"framboesa". 
# Em seguida, imprima o conjunto.

frutas_vermelhas = {"morango", "cereja", "framboesa"}
print(frutas_vermelhas)


# Remova a fruta"cereja" do conjunto frutas_vermelhas e
# imprima o conjunto atualizado.

frutas_vermelhas.remove("cereja")
print(frutas_vermelhas)


# Crie dois conjuntos, A e B, e realize a união dos dois
# conjuntos.

A = {"sofar", "geladeira", "gelagua"}
B = {"jet", "carro", "casa", "moto",}

print(A.union(B))


# Crie um programa que recebe dois conjuntos e exibe a
# interseção deles.

conjunto_01 = set(input("digite os elementos do primeiro conjunto: "))
conjunto_02 = set(input("digite os elementos do sengundo conjunto: "))

interacao = conjunto_01.intersection(conjunto_02)

print("as interacões dos conjuntos é:", interacao)


# Escreva um programa que receba duas listas e calcule
# a união dos elementos únicos dessas listas, usando
# conjuntos.

lista_01 = set(input("digite os elementos da primeira lista: "))
lista_02 = set(input("digite os elementos da segunda lista: "))

print("A união dos elementos unicos das duas listas é:", lista_01.union(lista_02))


# Escreva um programa que EXIBA um dicionário contendo
# informações de pessoas (nome, idade) e exiba essas
# informações.

cadastrados = [
    {
    "nome": "felipe",
    "idade": 25},


{   "nome": "marcyele",
    "idade": 23}
]

print(cadastrados)


# Escreva um programa que percorra as chaves e valores
# de um dicionário separadamente e os exiba.

dados = {
    "nome": "celia",
    "idade": 50,
    "cidade": "Fortaleza",
    "profissão": "Decoradora"
}

print("Chaves:")
for chave in dados.keys():
    print(chave)

print("\nValores:")
for valor in dados.values():
    print(valor)


# Desenvolva um programa que recebe um dicionário, uma
# chave e um valor como entrada e adiciona a chave e o
# valor ao dicionário, atualizando o valor se a chave já
# existir.

dicionario = {
    "nome": "Felipe",
    "idade": 25,
    "cidade": "fortaleza"
}

chave = input("digite a chave que deseja adicionar: ")
valor = input("digite o valor da chave adicionada: ")

dicionario[chave] = valor

print("O valor do dicionario atualizado:", dicionario)


# Escreva um programa que recebe um dicionário e uma
# lista de chaves como entrada e verifica se todas as
# chaves da lista existem no dicionário. A função deve
# retornar True se todas as chaves existirem e False caso
# contrário.

dicionario = {'a': 1, 'b': 2, 'c': 3}
chaves = ['a', 'b', 'c']

resultado = all(chave in dicionario for chave in chaves)

print(resultado)  

chaves_faltando = ['a', 'd', 'c']
resultado_faltando = all(chave in dicionario for chave in chaves_faltando)

print(resultado_faltando)


# Crie um programa que simule um sistema de votação. O
# programa deve permitir que os eleitores escolham entre
# opções de eleitores e conte os votos para cada opção.
# Use um dicionário para armazenar os resultados da
# votação, onde as chaves são as opções e os valores são o
# número de votos para cada opção. O programa deve
# permitir que os eleitores votem, encerre a votação e exiba
# os resultados finais. Use While True e pare o programa
# somente se o usuário digitar o número 0 e exiba os
# resultados finais.

opcoes = {
    1: "felipe",
    2: "marcyele",
    3: "sergio"
}

resultados = {1:0, 2:0, 3:0, }

while True:
    print("\nsitema de votação")
    print("escolha uma opção para votar:")

    for numero, opcao in opcoes.items():
        print(f"{numero} - {opcao}")
    print("0 - encerra a votação")

    voto = int(input("digite o numero da opção desejada: "))

    if voto == 0:
        print("\nvotação encerrada!")
        break

    if voto in resultados:
        resultados[voto] += 1
        print(f"voce votou em {opcoes[voto]}")
    else:
        print("opção invalida! tente novamente.")

print("\nresultados finais")
for numero, opcao in opcoes.items():
    print(f"{opcao}: {resultados[numero]} votos")


# Crie um dicionário que relacione nomes de alunos às suas
# notas em uma disciplina. Calcule a média das notas e
# exiba-a.

notas = {
    "Ana": 7.5,
    "Bruno": 8.0,
    "Carlos": 6.5,
    "Diana": 9.0,
    "Eduardo": 7.0
}

media = sum(notas.values()) / len(notas)
print(f"A média das notas dos alunos é: {media:.2f}")


# Crie um programa que receba uma lista de números e
# remova todas as duplicatas usando um conjunto (set). Em
# seguida, exiba a lista original e a lista sem duplicatas.

lista_original = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 8, 9]
lista_sem_duplicatas = list(set(lista_original))

print("Lista original:", lista_original)
print("Lista sem duplicatas:", lista_sem_duplicatas)


# Crie um programa que realize a união de múltiplos
# conjuntos e exiba o conjunto resultante.

conjunto_01 = {1, 2, 3, 4, 5, 6}
conjunto_02 = {12, 32, 34, 65}

conjuntos_unidos = conjunto_01 | conjunto_02

print("a uniao dos conjuntos:", conjuntos_unidos)



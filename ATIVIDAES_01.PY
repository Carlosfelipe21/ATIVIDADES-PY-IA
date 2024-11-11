# Faça a definição de uma lista contendo os números de 1
# até 5. Finalmente, utilize o print() para exibir os valores
# da lista.

lista_de_numeros = (1, 2, 3, 4, 5)

for numero in lista_de_numeros:
    print(numero)


# Faça a definição de uma lista contendo as vogais.
# Finalmente, utilize o print() para exibir os valores da lista.

lista_de_vogais = ("a", "e", "i", "o", "u")

for lista in lista_de_vogais:
    print(lista)


# Defina uma lista com 5 itens que tenha, pelo menos, 3
# classes diferentes. Utilize o print() para exibir o
# terceiro elemento dessa lista.

itens_selecionados = ("chave", "bola", "caneta", "esqueiro", "celular")
print(itens_selecionados[2])


# Crie uma tupla para representar as informações de três
# palestrantes, cada uma contendo o nome, o tema da
# palestra e a instituição à qual estão vinculados.
# Exiba na tela as informações do terceiro palestrante,
# incluindo nome, tema da palestra e instituição.

lista_de_palestrante = (
    ("Luan", 
    "Logica da Programação", 
    "Infinity school"),

    ("matheus"
    "inglês"
    "farias brito"),

    ("marcyele"
    "arquitetura"
    "UFMG")
)

print(lista_de_palestrante[2])


# Suponha que você está gerenciando uma competição esportiva e tem
# uma lista de tuplas representando os resultados das equipes em
# diferentes modalidades. Cada tupla contém o nome da equipe, seguido
# por uma lista de pontuações obtidas em cada rodada da competição.

# 1.Calcule a média das pontuações de cada equipe e armazene esses
# valores em uma nova lista chamada medias.
# 2.Ordene a lista medias em ordem decrescente.
# 3.Crie uma nova lista chamada classificacao que contém tuplas, onde
# cada tupla contém o nome da equipe e sua média de pontuações.
# 4.Exiba na tela a classificação final das equipes, mostrando o nome da
# equipe e sua média, da equipe com a pontuação mais alta para a
# mais baixa.

resultados_das_equipes = [
    (   "UZ INSANOS"
        "RANKING: 500"
        "PONTOS: 80")

    (   "KING COBRAS"
        "RANKING: 350"
        "PONTOS: 60")

    (   "REBELDES DA NOITE"
        "RANKING: 600"
        "PONTOS: 78")
]

medias = []
for equipes, ranking, pontuacoes in resultados_das_equipes:
    media = pontuacoes
    media.append((equipes,  media))
medias.sort(key=lambda x: x[1], reverse=True)

print("Classificação Final:")
for equipe, media in medias:
    print(f"{equipe}: Média de Pontos = {media}")

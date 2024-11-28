# Crie uma função que receba um nome e imprima uma
# saudação personalizada.

def saudacao(nome):
    return nome
nome_saudacao = f"Ola meu nome é {saudacao(nome="Felipe")} e estou amando Programação"
print(nome_saudacao)



# Crie uma função que receba um horário e imprima
# "Bom dia!" "Boa tarde!" ou "Boa noite!" conforme o horário.

def horario(hora):
        if hora < 0 or hora > 23:
            return "Horario Invalido"
        elif hora >= 5 and hora <= 11:
            return "Bom Dia!"
        elif hora >= 12 and hora <=17:
            return "Boa Tarde!"
        else:
            return "Boa Noite"
        
hora_digitada = horario(hora=14)
print(hora_digitada)



# Crie uma função que receba dois números e retorne a
# soma deles.

def somarnumeros(num1, num2):
     return num1 + num2
numeros = f"A soma dos numeros é {somarnumeros(num1=5, num2=5)}"
print(numeros)



# Crie uma função que receba dois números e retorne a
# subtração do primeiro pelo segundo.

def subtrairnumeros(numero1, numero2):
     return numero1 - numero2
numeros = f"A subtração dos numeros é: {subtrairnumeros(numero1=25, numero2=15)}"
print(numeros)



# Crie uma função que receba dois números e retorne a
# multiplicação deles.

def multiplicanumeros(num1, num2):
     return num1 * num2
numero = f"A multiplicação dos numeros é: {multiplicanumeros(num1=3, num2=8)}"
print(numero)



# Crie uma calculadora com opções de soma, multiplicação,
# subtração, divisão e sair.
# (Ela deverá funcionar infinitamente, até que o usuário decida sair da calculadora.)
# Utilize funções de rotina para cada operação e funções de unidade lógica para
# realizar os cálculos.

# Dica:
# Utilize de condicionais e Laços de Repetição para realizar esse
# exercício.

def calculadora(numero1, numero2):
    while True:
        menu = input("""
        1 - Somar
        2 - Multiplicar
        3 - Subtrair
        4 - Dividir
        5 - Sair
        Informe a opção escolhida: """)

        match menu:
            case "1":
                print(f"Resultado da soma: {numero1 + numero2}")
            case "2":
                print(f"Resultado da multiplicação: {numero1 * numero2}")
            case "3":
                print(f"Resultado da subtração: {numero1 - numero2}")
            case "4":
                if numero2 == 0:
                    print("Erro: Divisão por zero não é permitida.")
                else:
                    print(f"Resultado da divisão: {numero1 / numero2}")
            case "5":
                print("Saindo da calculadora. Obrigado!")
                break
            case _:
                print("Opção inválida. Tente novamente.")

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
calculadora(numero1, numero2)

               
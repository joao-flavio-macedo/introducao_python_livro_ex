# Escreva um programa que leia dois numeros. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores
# de soma e subtraçao para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas
# de um deles. Assim, 4x5 = 5+5+5+5 = 4+4+4+4+4

primeiro_numero = int(input("Informe o primeiro número:"))
segundo_numero = int(input("Informe o segundo número:"))
numeros = []

#print(f"{primeiro_numero}x{segundo_numero}={primeiro_numero*segundo_numero}")
for count in range(primeiro_numero):
    numeros += [segundo_numero]

print(f"A multiplicação é a soma sucessiva de: {numeros}")

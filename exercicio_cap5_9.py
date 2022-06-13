# Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão.
# inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular 
# o resultado. Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes que podemos
# retirar o divisor do dividendo. Logo, 20/4 =5, uma vez que podemos subtrair 4 cinco vezes de 20.
primeiro_numero = int(input("Informe o primeiro número:"))
segundo_numero = int(input("Informe o segundo número:"))
iterador = primeiro_numero
str = []
print(f"O resultado da divisão de {primeiro_numero} por {segundo_numero} é =", primeiro_numero//segundo_numero)
while segundo_numero <= iterador:
    iterador -= segundo_numero
    str += [segundo_numero]
print(f"A divisão é a subtração sucessiva de {segundo_numero} do total de {primeiro_numero}: {str}")

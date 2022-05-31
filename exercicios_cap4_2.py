#Escreva um programa que leia três numeros e que imprima o maior e o menor.
from os import system
system('cls')

primeiro = int(input("Informe o primeiro número:"))
segundo = int(input("Informe o segundo número:"))
terceiro = int(input("Informe o terceiro número:"))
maior = primeiro
menor = primeiro

if segundo > maior:
    maior = segundo
if terceiro > maior:
    maior = terceiro

if segundo < menor:
    menor = segundo
if terceiro < menor:
    menor = terceiro

print(f"O maior número:{maior}")
print(f"O menor número:{menor}")
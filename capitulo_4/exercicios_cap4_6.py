# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
#  Você deve poder calcular soma(+), subtração (-) multiplicação(*) e divisão (/).
#  Exiba o resultado da operação solicitada.
from os import system
system('cls')
primeiro = int(input("Informe o primeiro número:"))
segundo = int(input("Informe o segundo número:"))
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
operacao = input("Informe qual operação você gostaria de executar:")

if operacao == '1':
    print('Soma: {} + {} = {}'.format(primeiro, segundo, primeiro+segundo))

if operacao == '2':
    print('Subtração: {} - {} = {}'.format(primeiro, segundo, primeiro-segundo))

if operacao == '3':
    print('Multiplicação: {} * {} = {}'.format(primeiro, segundo, primeiro*segundo))

if operacao == '4':
    print('Divisão: {} / {} = {}'.format(primeiro, segundo, primeiro/segundo))
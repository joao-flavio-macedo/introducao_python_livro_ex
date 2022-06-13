#Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa, o salário e a quantidade de anos a pagar. 
#O valor da prestação mensal não pode ser superior a 30% do salário.
#Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.
from os import system
system('cls')
valorDaCasa = float(input("Qual é o valor da casa desejada pelo cliente:"))
valorSalario = float(input("Qual é o valor do salário Bruto?:"))
quantidadeAnos = int(input("Quantidade de anos a pagar:"))
quantidadeMeses = quantidadeAnos * 12
valorFinanciamentoMes = valorDaCasa / quantidadeMeses
if valorFinanciamentoMes > (valorSalario * 0.3):
    print("O valor do financiamento não pode ultrapassar 30% do salário!")
else:
    print(f"A prestação mensal do financiamento:{valorFinanciamentoMes}")




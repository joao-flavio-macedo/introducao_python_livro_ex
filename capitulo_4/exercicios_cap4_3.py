#Escreva um programa que pergunte o salário do funcionário
#  e calcule o valor do aumento.Para salários superiores a
#  R$1.250,00, calcule
#um aumento de 10%. Para os inferiores ou iguais, de 15%.
from os import system
system('cls')
salarioFuncionario = float(input("Qual é o salário do funcionário:"))
if salarioFuncionario > 1250:
    valorAumento = salarioFuncionario + salarioFuncionario * 0.1
valorAumento = salarioFuncionario + salarioFuncionario * 0.15
print(f"Salário do funcionário com o aumento:{valorAumento}")



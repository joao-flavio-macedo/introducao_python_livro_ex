#Faça um programa que calcule o aumento de salário. Ele deve solicitar o valor do salário e a porcentagem do aumento.
#Exiba o valor do aumento e do novo salário.
valorDoSalario = float(input("Insira o valor do Salário:"))
porcentagemAumento = float(input("Insira a quantidade de horas:"))
calculoAumento = valorDoSalario + (valorDoSalario * (porcentagemAumento/100))
print(f"Salário com aumento:{calculoAumento}")
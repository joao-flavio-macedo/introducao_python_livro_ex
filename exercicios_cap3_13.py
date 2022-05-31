#Escreva um programa que converta uma temperatura digitada em C em F. A fórmula para essa conversão é: F=((9xC)/5)+32

Celsius = float(input("Insira a temperatura em Celsius:"))
Fahrenheit = ((9*Celsius)/5)+32
print(f"Temperatura em Fahrenheit:{Fahrenheit}")
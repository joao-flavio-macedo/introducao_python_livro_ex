#Escreva um programa que pergunte a distância que um passageiro deseja percorrer em KM.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até de 200KM e R$ 0,45 para viagens mais longas.
from os import system
system('cls')

distanciaPassageiro = int(input("Qual a distância a ser percorrida:"))
if distanciaPassageiro <= 200:
    precoPassagem = distanciaPassageiro * 0.5
precoPassagem = distanciaPassageiro * 0.45
print(f"O preço da passagem para a distância percorrida:{precoPassagem}")



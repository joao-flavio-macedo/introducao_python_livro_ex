#Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80KM/h,
#  exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por km acima de 80km/h
from os import system
system('cls')
calculoMulta = 0
perguntaVelocidade = int(input("Digite a velocidade do carro:"))
if perguntaVelocidade > 80:
    print("Carro Multado!")
    calculoMulta = (perguntaVelocidade - 80) * 5
    print(f"Valor da Multa em R$:{calculoMulta}")
print("Carro dentro da Velocidade")




# Escreva um programa que leia dois números e que eprgunte qual operação você deseja realizar. Você deve poder calcular soma(+), subtração (-)
# multiplicação(*) e divisão (/). Exiba o resultado da operação solicitada.



#Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de KWH consumida e o tipo de
#instalação: R para residências, I para Indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.

#tipo            Faixa(KWH)         Preço
#Residencial     Até 500            R$ 0,40
#                Acima de 500       R$ 0,65 
#Comercial       Até 1000           R$ 0,55
#                Acima de 1000      R$ 0,60
#Industrial      Até 5000           R$ 0,55
#                Acima de 5000      R$ 0,60




#Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de KWH consumida e o tipo de
#instalação: R para residências, I para Indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.

#tipo            Faixa(KWH)         Preço
#Residencial     Até 500            R$ 0,40
#                Acima de 500       R$ 0,65 
#Comercial       Até 1000           R$ 0,55
#                Acima de 1000      R$ 0,60
#Industrial      Até 5000           R$ 0,55
#                Acima de 5000      R$ 0,60
from os import system
system('cls')

quantidadeKWH = int(input("Qual é a quantidade de KW/H consumida:"))
print("R - Residencial")
print("I - Industrial")
print("C - Comercial")
tipoInstalacao = input("Selecione o tipo de instalação:")

if tipoInstalacao == 'R':
    if quantidadeKWH <= 500:
        print('Residencial:{}'.format(quantidadeKWH*0.40))
    else:
        print('Residencial:{}'.format(quantidadeKWH*0.65))

if tipoInstalacao == 'I':
    if quantidadeKWH <= 1000:
        print('Industrial:{}'.format(quantidadeKWH*0.55)) 
    else:
        print('Industrial:{}'.format(quantidadeKWH*0.60)) 
                
if tipoInstalacao == 'C':
    if quantidadeKWH <= 5000:
        print('Industrial:{}'.format(quantidadeKWH*0.55)) 
    else:
        print('Industrial:{}'.format(quantidadeKWH*0.60)) 
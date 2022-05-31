#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado pelo usuário, assim como a quantidade
#de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado

quantidadeKM= float(input("Informe a quantidade de Kilometros percorridos:"))
quantidadeDIAS= int(input("Informe a quantidade de dias utilizados:"))

precoQuantidadeKM= quantidadeKM * 0.15
precoQuantidadeDIAS= quantidadeDIAS * 60
precoApagar = precoQuantidadeKM + precoQuantidadeDIAS
print(f"Total a pagar:{precoApagar}")

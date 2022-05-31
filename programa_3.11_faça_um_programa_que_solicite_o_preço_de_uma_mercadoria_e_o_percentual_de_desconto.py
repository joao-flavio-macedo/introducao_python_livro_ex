#Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
#Exiba o valor do desconto e o preço a pagar
precoMercadoria = float(input("Informe o preço de mercadoria:"))
percentualDesconto = float(input("Informe o percentual de desconto:"))
valorDesconto = precoMercadoria * (percentualDesconto/100)
precoApagar = precoMercadoria - valorDesconto
print(f"Valor do Desconto:{valorDesconto}")
print(f"Preço a pagar:{precoApagar}")
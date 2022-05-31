#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros
#fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro,
#e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

quantidadeDeCigarros = int(input("Informe a quantidade de cigarros:"))
quantidadeDeAnos = int(input("Informe por quantos anos já fumou:"))
quantidadeTotal = (quantidadeDeAnos * 365)*quantidadeDeCigarros
diasPerdidos = (((quantidadeTotal * 10)/60)/24)
print(f"Dias perdidos de vida:{diasPerdidos}") 
# Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada
# em vez de começar com 1 e 10

mult = int(input("informe o múltiplo:"))
count = int(input("informe o inicio da multiplacação:"))
limite = int(input("informe o limite da multiplicação:"))
while count <= limite:
    print (f"{mult} x {count} = {count*mult}")
    count += 1
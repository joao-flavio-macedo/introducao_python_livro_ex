# Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário
# mas dessa vez, apenas os números ímpares

count = 1
numero = int(input("Digite um número maior do que UM:"))
while count <= numero:
    if count % 2 == 1:
        print(count)
    count += 1

#count = 10
#while count >= 0:
#    print(count)
#    count -= 1
#    if count < 0:
#        print("FOGO!") 
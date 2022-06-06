# Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada

# count = 1
# while count <= 10:
#     print(count*3)
#     count += 1

mult = int(input("informe o múltiplo:"))
count = 1
while count <= 10:
    print (f"{mult} x {count} = {count*mult}")
    count += 1
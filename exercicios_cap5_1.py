# Faça um programa para escrever a contagem regressiva do lançamento de um foguete
# O programa deve imprimir 10,9,8...1,0 e fogo! na tela.

count = 10
while count >= 0:
    print(count)
    count -= 1
    if count < 0:
        print("FOGO!") 
#Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
#esperada para a viagem

distanciaAPercorrer = float(input("Insira a distância a percorrer:"))
velocidadeMedia = float(input("Insira a velocidade média pretendida (KM/h):"))
TempoDeViagem = distanciaAPercorrer/velocidadeMedia

print(f"Tempo de Viagem(h):{TempoDeViagem}")

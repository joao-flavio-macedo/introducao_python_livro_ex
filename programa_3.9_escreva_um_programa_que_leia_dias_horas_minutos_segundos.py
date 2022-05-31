dias = int(input("Insira a quantidade de dias:"))
horas = int(input("Insira a quantidade de horas:"))
minutos = int(input("Insira a quantidade de minutos:"))
segundos = int(input("Insira a quantidade de segundos:"))

diasPhorasPsegundos = dias*24*(60**2)
horasPsegundos = horas*(60**2)
minutoPsegundos = minutos*60

totalSegundos = segundos + diasPhorasPsegundos + horasPsegundos + minutoPsegundos
print(f"Total de Segundos:{totalSegundos}")

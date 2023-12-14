# Escribe un programa que pregunte al usuario por el número de horas trabajadas y 
# el coste por hora.Después debe mostrar por pantalla la paga que le corresponde

horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))

paga = lambda horas,coste: horas*coste

print("Tu paga es", paga(horas,coste))
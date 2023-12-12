print("Programa que carga calificaciones")

x=1
AU=[]
DE=[]
SA=[]
NA=[]

student=[]
calification=[]

for x in range(1,4):
    est=input(f"Name of the student {x}:")
    student.append(est)
    cal=input(f"Student's {x} calification:")
    calification.append(float(cal))

    if float(cal) == 10:
        AU.append(cal)
    elif float(cal) == 9:
        DE.append(cal)
    elif float(cal) == 8:
        SA.append(cal)
    else:
        NA.append(cal)
y=0 

for x in range(3):
    y=y+1
    print(f"{y}", student[x],calification[x])
print("AU",len(AU))
print("DE",len(DE))
print("SA",len(SA))
print("NA",len(NA))

# imprimir alreves la palabra sin funciones ya definidas

word="Hola mundo"

def alrevesW(word):
   
    alrv=""
   
    for i in word[::-1]:
   
        alrv=alrv+i
   
    print(alrv)

alrevesW(word)
print(word[::-1])
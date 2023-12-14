# Dada una palabra buscarla en una frase y devolver cuantas veces aparece
frase="En, la escuela enseñan en 2 pies"
frase=frase.lower().replace(","," ")

word="EN"
word=word.lower()

def buscador(frase,word):
    repetidas=0
    listWords=frase.split(" ")

    for i in listWords:
        if i == word:
             repetidas=repetidas+1

    if repetidas==0:
        print("No se encuentra en la frase")
    #return repetidas
    else:
        print("Repetidos:",repetidas)

buscador(frase,word)
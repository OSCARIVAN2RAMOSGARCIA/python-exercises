#----------Mayor a menor---------------------------------
def  nth_smallest(a,n):             # a = nombre de la lista

    b=len(a)-1         # menos 1 porque siempre comparamos 2 valores adyacentes.

    for x in range(b):

        for i in range(b-x):

            if a[i]<a[i+1]:

                a[i],a[i+1]=a[i+1],a[i]

    return a[i]
    
a=[32,5,3,6,7,54,87] 

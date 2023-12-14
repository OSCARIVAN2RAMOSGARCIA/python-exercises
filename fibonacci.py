# 67. Escribe un programa para producir la serie Fibonacci en Python.

def fibonacci(n):
    result=[]
    a=1
    b=1
    if n>=0:
        result=result+[0]
       
    if n>=1:
        result=result+[1]    
     
    if n>=2:
        result=result+[1]

    for i in range(n-3):
        total = a + b
        b=a
        a= total
        result=result+[total]
    print(result)
         
fibonacci(12)

result={}
dict=input("Teclea numeros: ")

def countEorO(dict):
      
    even = 0
    odd = 0
      
    for i in dict:
        
      if int(i) % 2 == 0:
        even = even + 1
      else:
        odd = odd + 1
    result["Even"]=even
    result["Odd"]=odd

try:
    int(dict)
    countEorO(dict)
    print(result)
    
except ValueError:
    print(False)
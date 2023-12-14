class Person:
    def __init__(self,id):
        self.id=id

obama=Person(120)

obama.__dict__['age']=49

print(obama.age + len(obama.__dict__))
print(len(obama.__dict__))
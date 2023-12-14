print("Press 1 if you want to continue with the login\n")

answer=input(f"Enter option:")

while float(answer)!=1:
    answer=input(f"Enter option:")

if(float(answer)==1):
    print("Login")
    username=input("Enter username:")
    password=input("Enter password:")

    while username!="Visita" or password!="Visita":
        print("Try again, incorrect username or password ")
        username=input("Enter username:")
        password=input("Enter password:")
    
    print("Welcome Vista")
    name=input("What's your name?:")
    age=input("How old are you?:")
    print(f"{name} is {age} years old")

else:
     print("No valid option")
    
       

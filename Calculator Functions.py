

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print (f"{e}")
        
ch = input("Enter choice: \n1.add\n2.subtract\n3.multiply\n4.divide\n")
n= int(input("Enter first number: "))
m= int(input("Enter second number: "))

match ch:
    case '1':
        print(add(n,m))
    case '2':
        print(subtract(n,m))
    case '3':
        print(multiply(n,m))
    case '4':
        print(divide(n,m))
        


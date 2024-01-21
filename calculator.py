
#calculator program

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b


a= int(input())
print("select an operation: + , - , * , / ")
choice = str(input())
b= int(input())



match choice:
    case '+': print(a, '+' ,b , '=', add(a,b))
    
    case '-': print(a, '-' ,b , '=', sub(a,b))
        
    case '*': print(a, '*' ,b , '=', mul(a,b))
        
    case '/': print(a, '/' ,b , '=', div(a,b))
    
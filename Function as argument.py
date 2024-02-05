

def need(fun,n):
    return fun(n)
    

def square(n):
    return n*n

def cube(n):
    return n*n*n

n = int(input("Enter 'n' value: "))
print("Enter",n,"values")
list1 = []
for i in range(n):
    lt1 = int(input())
    list1.append(lt1)
   
for func in list1:
    print(need(square, func))  
    print(need(cube, func))    

    

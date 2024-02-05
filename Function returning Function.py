

def val(square, n):
    return square(n)
#return square function from a random function

def square(n):
    return n*n


n=int(input("Enter a number: "))
print(val(square,n))


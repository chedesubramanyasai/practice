print("Enter number:")
fact = int(input())

if fact<0:
    print('Enter valid number')

factorial = 1
while fact>0:
    factorial = fact * factorial
    fact-=1
    
print('Factorial is ',factorial)
    
    
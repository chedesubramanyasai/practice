

print('C: need Celcius\nF: need Fahrenheit')
ch= str(input())
print('Enter degrees:')
val=float(input())
Fahrenheit = float(((9/5)*val) + 32)
celcius = float((5/9)*(val - 32))

match ch:
    case 'C': print('\nC -> F:',round(celcius,1))
    case 'F': print('\nF -> C:',round(Fahrenheit,1))
    
    
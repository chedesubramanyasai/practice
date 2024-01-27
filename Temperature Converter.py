


def temperature_converter(val,unit = 'C'):
    if unit == 'C':
        Fahrenheit = float(((9/5)*val) + 32)
        print(round(Fahrenheit,1))
    else:
        celcius = float((5/9)*(val - 32))
        print(round(celcius,1))


print('C: need Celcius\nF: need Fahrenheit')
ch= str(input())
print('Enter degrees:')
temp=float(input())

temperature_converter(temp, ch)

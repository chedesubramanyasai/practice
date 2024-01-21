try: 
    a=int(input())
    ch=str(input())
    b=int(input())
    
    match ch:
        case '+':
            print('sum is ',a+b)
        case '-':
            print('diff is ',a-b)
        case '*':
            print('mul is ',a*b)
        case '/':
            print('div is ',a/b)
        
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"An error occurred: {e}")
    
    
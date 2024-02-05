

def counter():
    count = 0
    def counted():
        nonlocal count
        count = count+1
        return count
    
    return counted
    
func = counter()
print(func())
print(func())
print(func())
print(func())

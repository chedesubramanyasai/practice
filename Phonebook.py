phonebook = {}

for i in range(2):
    name = input("Enter name: ")
    contact = input("Enter contact num: ")
    phonebook[name] = contact
    

print("1. add contact     2. update contact     3. search contact")
ch = int(input())

match ch:
    case 1: 
        name = input("Enter name: ")
        phonebook[name]=input("Enter contact num: ")
            
    case 2: 
            name=(input("Enter a name to update contact: "))
            phonebook[name] = input("Enter contact num: ")
            
    case 3: 
            name = input("enter name for required contact: ")
            print(phonebook[name]," is the contact num")



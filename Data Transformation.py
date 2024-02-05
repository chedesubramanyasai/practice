list2 = [41,43,45,47,49]

list1 = list(map(lambda x: (x * ((9/5)) + 32),list2))
list3 = list(map(lambda x: x*x , list2))
print("List after converting to Fah using lambda functions: ",list1)
print("\n")
print("Squares of list using lambda: ",list3)

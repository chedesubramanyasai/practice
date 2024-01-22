
list = []

print("print number of elements: ")
n = int(input())
print("print ",n,"elements: ")
for i in range(0,n):
    val= int(input())
    
    list.append(val)
    
print("sum of elements in list is :",sum(list))

#----------------------------------------------#


l = [1,2,3,4]
t = [5,6,7,8]

print("after merging two lists: ",l+t)



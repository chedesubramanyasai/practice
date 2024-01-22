

l_names = ["subbu","sai","ram"]

for i in l_names:
    print("Hello, ",i,"!")

    

#----------------------------------
   


def is_even(n):
    if n%2==0:
        return 1
    else:
        return 0


even=[]
nums = [1,3,4,7,5,6,8,9,2]

for i in nums:
    if is_even(i):
        even.append(i)

print("Even numbers in the list: ",even)

def generate_bill(print_bill = None, *args, **kwargs):
   su=0
#   print(kwargs)
   for key, val in kwargs.items():
       if key!= 'print_bill':
           su= su + int(val)
       if print_bill==True:
           print("\nItem name: ", key," Cost: ",val)
   print("\n\nTotal cost: ",su)
     

generate_bill('awe','pri',c1 = 42,c2 = 56)
generate_bill(True, 'sai','rams',a = 25, b = 47)



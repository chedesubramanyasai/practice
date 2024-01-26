

student_scores= {1:49,2:59,3:85}


res = sum([key for key in student_scores])
vals = 0 
for i in student_scores:
    vals = vals+student_scores[i]

# printing result
print("Dict values sum: " + str(res),':',str(vals))


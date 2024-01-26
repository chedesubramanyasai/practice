


colors = {'apple':'red', 'banana':'yellow', 'grape':'purple', 'cherry':'red', 'guava':'yellow'}

group = {}

for key, value in colors.items():
    if value not in group:
        group[value] = [key]
    else:
        group[value].append(key)
        
        
print(str(group))

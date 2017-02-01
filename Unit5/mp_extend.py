#Worked With TK
original_list = [1,2,3]
extended_list = [4,5,6]
x= original_list
y = extended_list

def extend(x,y):
    for item  in y:
        x.append(item)

extend(x,y)
print(x)
print(y)
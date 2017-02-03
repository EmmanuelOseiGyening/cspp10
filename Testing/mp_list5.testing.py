original = [1,2,3,4,5,6,5,3,5,6,7]
target = 5

def remove_all(original,target):
    for target in original:
        if original == target:
            original.remove(target)

remove_all(original,target)
print (original)
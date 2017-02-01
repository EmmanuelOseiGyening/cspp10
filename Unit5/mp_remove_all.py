original = [1,2,3,4,5]
target = 1

def remove_all(original,target):
    for number in range(len(original)):
        if original[number] == target:
            original.remove(target)


remove_all(original,target)

print(original)
    
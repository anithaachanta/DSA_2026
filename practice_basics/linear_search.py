def linear_search(num,target):
    for i in range(len(num)):
        if num[i]==target:
            return i
    return -1
num=[10, 25, 7, 40, 15]

print(linear_search(num, 40))

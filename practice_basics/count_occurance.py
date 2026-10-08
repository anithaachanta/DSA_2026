def count_occurrences(numbers, target):
    count=0
    for i in numbers:
        if i==target:
            count+=1
    return count

numbers = [2, 5, 2, 8, 2, 7, 5]
target = 2

print(count_occurrences(numbers,2))

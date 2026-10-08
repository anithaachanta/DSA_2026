def first_even(numbers):
    for i in range(len(numbers)):
        if numbers[i]%2==0:
            return i
            
    return -1
numbers = [12, 5, 18, 3, 25, 7]
print(first_even(numbers))

##def max_index(n):
##    max_val=n[0]
##    max_ind=0
##    for i in range(len(n)):
##        if n[i]>max_val:
##            max_val=n[i]
##            max_ind=i
##    return max_ind
##    
##n=[4, 12, 7, 25, 9]
##print(max_index(n))
##            
    
##==>min index

def min_index(n):
    min_val=n[0]
    min_ind=0
    for i in range(len(n)):
        if n[i]< min_val:
            min_val=n[i]
            min_ind=i
    return min_ind
n=[12, 7, 25,4, 9]
print(min_index(n))

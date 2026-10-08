"""brute force for largest element  o(nlog n)"""

##
##n=[10,20,30,4]
##s=sorted(n)
##print(s[-1])

"""optimization o(n)"""

n=[10,4,40,30,2]
largest=n[0]
for num in n:
    if num >largest:
        largest=num
print(largest)
    

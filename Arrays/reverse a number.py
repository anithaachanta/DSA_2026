
"""reverse a number brute force"""
##n=[1,2,3,4]
##rev=[]
##for i in range(len(n)-1,-1,-1):
##    rev.append(n[i])
##print(rev)

"""optimzation two pointer o(n) """
n=[1,2,3,4,5]
left=0
right=len(n)-1
while left<right:
    n[left],n[right]=n[right],n[left]
    left+=1
    right-=1
print(n)
    

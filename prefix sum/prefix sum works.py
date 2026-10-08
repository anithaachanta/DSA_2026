""" generally a prefix sum adding number in an array elements
like [1,2,3,4,5]
1
1+2=3
1+2+3=6
-----

burte force

"""
##arr=[1,2,3,4]
##prefix=[]
##sum_arr=0
##for i in arr:
##    sum_arr+=i
##    prefix.append(sum_arr)
##print(prefix)

#using prefix sum
##
##arr=[1,2,3,4,5]
##
##prefix=[0]*len(arr)
##prefix[0]=arr[0]
##for i in range(1,len(arr)):
##    prefix[i]=prefix[i-1]+arr[i]
##print(prefix)


"""range sum quary"""
arr=[1,2,3,4,5]
prefix=[0]*len(arr)

prefix[0]=arr[0]

for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]+arr[i]

left=1
right=3

if left==0:
    print(prefix[right])
else:
    print(prefix[right]-prefix[left-1])
          





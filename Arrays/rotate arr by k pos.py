arr=[1,2,3,4,5,6,7]

k=3
n=len(arr)
k=k%n
arr[:]=arr[-k:]+arr[:-k]
print(arr)

""" k%n means if there are k=12 then array [2,3,4,5,6,7,1]
ex:[7,1,2,3,4,5,6]
[7,6,1,2,3,4,5]
[5,6,7,1,2,3,4]
[4,5,6,7,1,2,3]
[3,4,5,6,7,1,2]
[2,3,4,5,6,7,1]-->6
[1,2,3,4,5,6,7]
[7,1,2,3,4,5,6]
[7,6,1,2,3,4,5]
[5,6,7,1,2,3,4]
[4,5,6,7,1,2,3]
[3,4,5,6,7,1,2]
[2,3,4,5,6,7,1]--->12 but both are same
that why we use k=k%len(arr) so 6%7=1

"""

left=0
right=len(nums)-1
while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        return mid
    left=mid+1
    right=mid-1
print([left,right])

nums=[1,0,3,4,0,6]

i=0
n=len(nums)
for j in range(n):
    if nums[j]!=0:
        nums[j],nums[i]=nums[i],nums[j]
        i+=1
print(nums)

        

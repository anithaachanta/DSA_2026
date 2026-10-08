arr=[1,2,3,4,5]

last=arr[-1]  #saving last elemt
for i in range(len(arr)-1,0,-1):  # runs for last to first like rverse 
    arr[i]=arr[i-1] #arr become arr[i]=5 arr[i-1]=5 means [1,2,3,4,4] until
                    #[1,1,2,3,4] then 
    
arr[0]=last  #repalce last at first position
print(arr)

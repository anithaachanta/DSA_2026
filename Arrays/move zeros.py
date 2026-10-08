n=[0,1,0,3,12]
temp=[]
for i in n:
    if i!=0:
        temp.append(i)
zeros=len(n)-len(temp)

##for i in range(zeros):
##    temp.append(0)
temp.extend([0]*zeros)
print(temp)



##
##n=[0,1,0,3,12]
##j=0
##for i in range(len(n)):
##    if n[i]!=0:
##        n[i],n[j]=n[j],n[i]
##        j+=1
##print(n)

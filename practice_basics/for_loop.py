##numbers=[10,20,30,40]
##for i in range(0,len(numbers)):
##    print(numbers[i])

#--->indexing

##num=[5, 8, 12, 20, 25]
##
##print(num[1])
##print(num[4])


#--->and vs or

##a = 20
##b = 15
##c = 18
##if a>b and a>c:
##    print("a is largest")
##elif b>c and b>a:
##    print("b is largest")
##else:
##    print("c is largest")


#initilize

##n = 12345
##count=0
##while n > 0:
##    digit = n % 10
##    count += 1
##    n //= 10
##
##print(count)

##
##def count_digits(n):
##    count=0
##    while n>0:
##        digit=n%10
##        count+=1
##        n//=10
##    return count



##n=[2,4,6,14,7,16]
##for i in n:
##    if i>10:
##        print(n[i])
##        
##






n=[3,-4,2,-7,0,4,0,9]
pos,neg,zero=0
for i in range(len(n)):
    if i>0:
        pos+=1
        print("psoitive=",pos)
    elif i<0:
        neg+=1
        print("negative=",neg)
    elif i==0:
        zero+=1
        print("zero=",zero)
        
        

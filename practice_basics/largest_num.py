n=[4,7,2,5,3,6]
largest=n[0]
for i in n:
    if i>largest:
        largest=i
print(largest)


1. 
def is_pos_nev(n):
    if n>0:
        return postive 
    elif n<0:
        return negative
    else:
        return zero

2.
n=[2,6,4]
largest=n[0]
for i in range(0,n+1):
    if i>largest:
        largest=i
print(i)


sec 2 
4.
n=100 
for i in range(1,n+1):
    print(i)
5.
n=50
for i in range(1,n+1):
    if i%2==0:
        print(i)
6.
n=5 
sum=0
for i in range(n+1):
    sum+=i
print(sum)

7.
n=90
count=0
for i in range(1,n+1):
    if n%3==0:
        count+=1
print(count)

8.

n=5
for i in range(1,11):
    print(f"{n} X {i} ={n*i}")

sec3

n=58321
while n>0:
    digit=n%10
    count+=1
    n=n//10
print(count)

10.

n=583
sum=0
while n>0:
    d=n%10
    sum+=d
    n=n//10
print(sum)

11.
n=12345
sum=0
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
print(rev)

n=[3,7,4,15,8,20]
for i in range(0,len(n)):
    if i>10:
        print(i)

n=[-2, 5, 0, 7, -1, 0, 3]
pos=0
neg=0
zero=0
for i in range(0,len(n)):
    if i>0:
        pos+=1
        print("positive=",pos)
    elif i<0:
        neg+=1
        print("Negative=",neg)
    else:
        zero+=1
        print("zero=",zero)


num=[10, 5, 20, 8, 15]
largest=num[0]
sec_largest=num[1]
if sec_largest>largest:
    largest,sec_largest=sec_largest,largest
for i in range(2,len(num)):
    if num[i]>largest:
        sec_largest=largest
        largest=num[i]
    elif num[i]>sec_largest:
        sec_largest=num[i]
print(sec_largest)


num=[1, 2, 3, 5, 6]
n=len(num)+1
total=0
for i in range(0,n+1):
    total+=i
for i in num:
    total-=i
print(total)


    











##n=[3,20,5,70]  #o (nlogn)
##n.sort()
##print(n[-2])

"""optimal o(n)"""
arr=[4,5,8,6]
largest=second=-1
for num in arr:
    if num>largest:
        second=largest
        largest=num
    elif num>second and num!=largest:
        second=num
print(second)


"""
1sr iteration
 4>-1-True
 second=-1
 largest=4

 5>4-true
 second=4
 largest=5

 8>5->True
 second=5
 largest=8

 6>8-flase
elif
 6>5 and 6!=8
 second=num
 8=6
 print(second)
 """
 

n = int (input("enter the number:"))
a=0
b=1
sum=0
count=0
for i in range(0,n+1):
    print(sum,end=" ")
    count+=1
    a=b
    b=sum
    sum=a+b

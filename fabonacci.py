f=int(input("enter the number range : "))
a,b=0,1
sum=0
if f<0:
    print("please enter values greater than zero ")
else:
    for i in range(0,f):
        print(sum,end=" ")
        a=b
        b=sum
        sum=a+b
        

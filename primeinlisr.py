n=int(input("enter number :"))
def prime():
    list=[]
    for i in range(2,n):
        if i==0 or i==1:
            continue
        else:
            for j in range(2,int(i/2)+1):
                if(i%j==0):
                    break
                else:
                    list.append(i)
    return list
l1=prime()
if(len(l1)==0):
    pass
else:
    print(l1)                

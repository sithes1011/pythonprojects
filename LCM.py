
x=int(input("enter the first number"))
y=int(input("enter the second number"))
if x<y:
    min=x
else:
    min=y
while(1):#1=true,0=false
    if (min%x==0)and(min%y==0):
        print("LCM is",min)
        break
    min+=1

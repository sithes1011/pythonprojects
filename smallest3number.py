a=int(input("enter the 1st number"))
b=int(input("enter the 2nd number"))
c=int(input("enter the 3rd number"))
if a<b and a<c:
    smallest=a
elif b<a and b<c:
    smallest=b
else:
    smallest=c
print("the smallest number between",a,b,c,"is",smallest)
n=int(input("how many terms?"))
n1=0
n2=1
count=2
#if n<=0:
   # print("please enter a positive integer")
#elif n==1:
    #print("fibonacci sequence")
    #print(n1)
#else:
    #print("fibonacci sequence:")
print(n1,",",n2,end=",")
while count<n:
    nth=n1+n2
    n1=n2
    n2=nth
    print(nth,end=",")
    count+=1

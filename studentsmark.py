class student:
    def __init__ (self):
        self.name=""
        self.tam=0
        self.eng=0
        self.math=0
        self.phy=0
        self.chem=0
        self.com=0
    def getdata(self):
        print("-----------------------------------------------------------------------------")
        self.name=(input("Enter The Student Name :"))
        self.tam=(int(input("Enter The Tamil Mark :")))
        self.eng=(int(input("Enter The English Mark :")))
        self.math=(int(input("Enter The Maths Mark :")))
        self.phy=(int(input("Enter The Physics Mark :")))
        self.chem=(int(input("Enter The Chemistry Mark :")))
        self.com=(int(input("Enter The Computerscience Mark:")))
    def display(self):
        print("-----------------------------------------------------------------------------")
        print("Name :",self.name)
        print("Tamil :",self.tam)
        print("English :",self.eng)
        print("Maths :",self.math)
        print("Physics :",self.phy)
        print("Chemistry :",self.chem)
        print("Computerscience",self.com)
        print("Total Marks :",self.tam+self.eng+self.math+self.phy+self.chem+self.com,"/600") 
store=[]
go=1
while go==1:
    choice=int(input("1. To Add Student Details\n2. To Display Student Details\nEnter Your Choice :"))
    if choice==1:
        g=int(input("How Many Of The Student Details You To Be Add :"))
        for x in range(g):
            s=student()
            s.getdata()
            store.append(s)
    elif choice==2:
        for i in store:
            i.display()
    else:
        print("invaild response")
    print("-----------------------------------------------------------------------------")
    go=int(input("Choose Any One\n1.To See More\n2.Exit\nEnter Your Choice :")) 
print("-------------------------------------Thank You----------------------------------")      

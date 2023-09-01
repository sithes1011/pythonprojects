class library:
    def __init__ (self):
        self.book=""
        self.author=""
    def getdata(self):
        self.book=input("enter the bookname :")
        self.author=input("enter the authorname :")
    def display(self):
        print("name of the book :",self.book)
        print("name of the author :",self.author)
books=[]
ch='yes'
while ch=='yes':
    print("choose any option\n1.To add book\n2.To see the books")
    choice=int(input("enter your choice :"))
    if choice==1:
        L=library()
        L.getdata()
        books.append(L)
    elif choice==2:
        for i in books:
            i.display()
    else:
        print("invalid input")       
    ch=input("do you want to add books enter yes")
        

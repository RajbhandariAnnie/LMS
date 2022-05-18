import ListBook
def Returnbooks():
    global data
    name=input("Enter the first name of the borrower: ")
    borrow="Borrow-"+name+".txt"
    try:
        with open(borrow,"r") as f:
            lines=f.readlines()
            lines=[borrow.strip("$") for borrow in lines]
    
        with open(borrow,"r") as f:
            data=f.read()
            print(data)
    except Exception:
        print("The name of borrower is incorrect")
        Returnbooks()
    
    b="Return-"+name+".txt"
    with open(b,"w+")as f:
        f.write("                Library Management System \n")
        f.write("                   Returned By: "+ name+"\n")
        f.write("    Date: " + "    Time:"+  "\n\n")
        f.write("S.N.\t\t BookName \t\t price \n")
    total=0.0
    for i in range(len(ListBook.BookName)):
        if ListBook.BookName[i] in data:
            with open(b,"a") as f:
                f.write(str(i+1)+"\t\t"+ListBook.BookName[i]+"\t\t$"+ListBook.price[i]+"\n")
                ListBook.quantity[i]=int(ListBook.quantity[i])+1
            total+=float(ListBook.price[i])
            
    print("\t\t\t\t\t\t\t"+"$"+str(total))
    print("Is the return date of the book expired? Press Y for Yes and N for No.")
    stat=input()
    if(stat.lower()=="y"):
        print("How many days are you late to return the book?")
        day=int(input())
        fine=2*day
        with open(b,"a")as f:
            f.write("\t\t\t\t\tFine: $"+ str(fine)+"\n")
        total=total+fine
    
    print("Final Total: "+ "$"+str(total))
    with open(b,"a")as f:
        f.write("\t\t\t\t\tTotal: $"+ str(total))
    
    with open("book.txt","w+") as f:
        for i in range(len(ListBook.BookName)):
            f.write(ListBook.BookName[i]+","+ListBook.AuthorName[i]+","+str(ListBook.quantity[i])+","+"$"+ListBook.price[i]+"\n")

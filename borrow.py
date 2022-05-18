import ListBook
def BorrowBook():
    success=False
    while(True):
        FirstName=input("Enter first name of borrower:")
        if FirstName.isalpha():
            break
        print("enter input alphabet from A-Z")
    while(True):
        LastName=input("Enter last name of borrower:")
        if LastName.isalpha():
            break
        print("enter input alphabet from A-Z")
    d="Borrow-"+FirstName+".txt"
    with open(d,"w+")as f:
        f.write("        Library Management System \n")
        f.write("         Borrowed by:" + FirstName+""+LastName+"\n")
        f.write("Date:"+ ListBook.getDate()+" Time:"+ ListBook.getTime()+"\n\n")
        f.write("SN.\t\t BookName \t AuthorName \n")

    while success==False:
        print("Select an option below:")
        for i in range(len(ListBook.BookName)):
            print("Enter",i,"to borrow any book",ListBook.BookName[i])

        try:
            b=int(input())
            try:
                if(int(ListBook.quantity[b])>0):
                    print("Book is available")
                    with open(d,"a")as f:
                        f.write("1 \t\t"+ListBook.BookName[b]+"\t\t"+ListBook.AuthorName[b]+"\n")

                    ListBook.quantity[b]=int(ListBook.quantity[b])-1
                    with open("book.txt","w+") as f:
                        for i in range(len(ListBook.BookName)):
                            f.write(ListBook.BookName[i]+","+ListBook.AuthorName[i]+","+str(ListBook.quantity[i])+","+"$"+ListBook.price[i]+"\n")


                    #multiple book borrowing code
                    loop=True
                    count=1
                    while loop==True:
                        choice=str(input("Would you like to borrow more books? However you cannot borrow same book twice. Press y for yes and n for no."))
                        if(choice.upper()=="Y"):
                            count=count+1
                            print("Please select an option below:")
                            for i in range(len(ListBook.BookName)):
                                print("Enter", i, "to borrow book", ListBook.BookName[i])
                            a=int(input())
                            if int(ListBook.quantity[a])>0:
                                print("Book is available")
                                with open(d,"a") as f:
                                    f.write(str(count) +". \t\t"+ ListBook.BookName[b]+"\t\t  "+ListBook.AuthorName[b]+"\n")

                                ListBook.quantity[a]=int(ListBook.quantity[a])-1
                                with open("book.txt","w+") as f:
                                    for i in range(len(ListBook.BookName)):
                                        f.write(ListBook.BookName[i]+","+ListBook.AuthorName[i]+","+str(ListBook.quantity[i])+","+"$"+ListBook.price[i]+"\n")
                                        success=False
                            else:
                                loop=False
                                break
                        elif (choice.upper()=="N"):
                            print ("Thank you for borrowing books from us")
                            print("")
                            loop=False
                            success=True
                    else:
                        print("Please choose correct option")
                else:
                    print("Book is not available")
                    BorrowBook()
                    success=False
            except IndexError:
                print("")
                print("Please choose book according to their number.")
        except ValueError:
            print("")
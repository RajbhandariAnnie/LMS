import ListBook
import borrow
import Returnbooks

def start():
    while(True):
        print("You're welcomed to the Library Management System")
        print("----------------------")
        print("Enter 1 to display")
        print("Enter 2 to borrow a book")
        print("Enter 3 to return a book")
        print("Enter 4 to exit")
        try:
            decision=int(input("Select an option given below:")) 
            print()
            if(decision==1):
                with open("book.txt","r")as f:
                    lines=f.read()
                    print(lines)
                    print()

            elif(decision==2):
                ListBook.ListBook()
                borrow.BorrowBook()
            elif(decision==3):
                ListBook.ListBook()
                Returnbooks.Returnbooks()
            elif(decision==4):
                print("Thank you so much for using our Library Management System")
                break
            else:
                print("Please select a valid option")
        except ValueError: 
            print("Please input as suggested")
start()


        

 


 

  

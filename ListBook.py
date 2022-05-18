import datetime
def ListBook():
   global BookName
   global AuthorName
   global quantity
   global price
   BookName=[]
   AuthorName=[]
   quantity=[]
   price=[]
   with open("book.txt","r")as f:
      lines=f.readlines()
      lines=[x.strip('\n')for x in lines]
      for i in range(len(lines)):
         ind=0
         for a in lines[i].split(','):
            if(ind==0):
               BookName.append(a)
            elif(ind==1):
               AuthorName.append(a)
            elif(ind==2):
               quantity.append(a)
            elif(ind==3):
               price.append(a.strip("$"))
            ind+=1

def getDate():
   
   last=datetime.datetime.now()
   #print("Date:",now().Date())
   return str(last.date())


def getTime():
   
   last=datetime.datetime.now()
   #print("Time:",now().Time())
   return str(last.time())
      

 

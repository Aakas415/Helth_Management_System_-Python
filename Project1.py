def getdate():
    import datetime
    return datetime.datetime.now()

import datetime   
def gettime():
    return datetime.datetime.now()


def take(k):
    if k==1:
        c=int(input("Enter 1 For Exirecise And 2 For Food.\n"))
        
        if(c==1):
            value = input("Type here: ")
            with open("Aakash_E.txt","a") as am:
                am.write(value+"\n")
                print("Writen Succesful..!")
        
        elif(c==2):
            value = input("Type here: ")
            with open("Aakash_F.txt", "a") as am:
                am.write(value+"\n") 
                print("Writen Succesful..!")

    elif k==2:
        c=int(input("Enter 1 For Exirecise And 2 For Food. \n"))
        if(c==1):
            value = input("Type here: ")
            with open("Jessy_E.txt","a") as j:
                j.write(value+"\n")
                print("Writen Succseful..!")

        elif(c==2):
            value=input("Type here: ")
            with open("Jessy_F.txt","a") as j:
                j.write(value+"\n")
                print("Writen Succesful..!")
        else:
            print("Plese enter valid details 1-Aakash and 2-Jessy.\n")

def retrive(k):
    if(k==1):
        c=int(input("Enter 1 for Exirecise and 2 for Food.\n")) 
        if(c==1):
            with open("Aakash_E.txt") as am:
                for i in am:
                    print(i,end="")
        elif(c==2):
            with open("Aakash_F.txt") as j:
                for i in j:
                    print(i,end="")
    elif(k==2):
        if(c==1):
            with open("Jessy_E.txt") as j:
                for i in j:
                    print(i,end="")
        elif(c==2):
            with open("Jessy_F.txt")as j:
                for i   in j:
                    print(i,end="")
        else:
            print("Plz Enter Valid details(Aakash or Jessy)")

print("....... HELTH MANAGEMENT SYSTEM .......")
a = int( input("\nEnter \n1-Log  \n2-Retrive\n"))
print("....... HELTH MANAGEMENT SYSTEM .......")
if(a==1):
    b = int(input("Enter \n\t1-Aakash \n\t2-Jessy\n"))
    take(b)
else:
    b= int(input("Enter \n\t1-Aakash \n\t2-Jessy\n"))
    retrive(b)
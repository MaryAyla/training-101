#tells python to execute a certain statement or block of statement until a condition is false
i=0
numbers={0,1,2,3,4,5}


#while len(numbers)>0:
   # print(numbers)
    #numbers.pop()
    #i<10
    #print(i)
#i= i+1
#while i<10:
    #print("Mwende")
    #i=i+1

password_saved="1234"

password=input("enter your password")
tries=0
while password != "1234" and tries <3:
 password=input("please enter the correct password")

tries +=1
if tries>=3:
    print("pin blocked")
else:

        print("hurray correct password entered")




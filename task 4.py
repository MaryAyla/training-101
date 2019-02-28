number= int(input("put a number"))
modullus= number %2

if modullus==0:
 print("this is an even number:", number)
elif number%2 !=0:
    print("this is an odd number", number)
elif number %4==0:
 print("this ia a multiple of 4:", number)
else:
    print("invalid")
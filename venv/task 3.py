#write a program that takes a list of numbers (for example,a=[5,10,15,20,25] and makes a new list of only the first and last
#elements of the given list.For practise write this code inside a function

def list_number(list):
    x=[list[0],list[-1]]
    return x
list=[]
for i in range (10):
    list.append(i)
    i+=1
    print("first and the last number in the list is: {} ".format(list_number(list)))




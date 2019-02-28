def large(x):
    x.sort()
    largest=x[-1]
    return largest
x=int(input("enter the first number"))
y=int(input("enter the second number"))
z=int(input("enter the third number"))

vars=[x,y,z]
print("the largest {}".format(large(vars)))
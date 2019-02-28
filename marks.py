sub1=int(input("Enter the marks of Maths:"))
sub2=int(input("Enter the marks of Eng:"))
sub3=int(input("Enter the marks of Kis:"))
sub4=int(input("Enter the marks of Scie:"))
sub5=int(input("Enter the marks of SSr:"))

average=int(sub1+sub2+sub3+sub4+sub5)/5
if average>=90 and average<=100:
    print("A")
elif average>=70 and average<=80:
    print("B")
elif average >= 60 and average <= 70:
    print("C")
elif average >= 50 and average <= 60:
    print("D")
else:
    print("Fail")



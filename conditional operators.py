marks= int(input("enter your marks\n"))
#if marks >= 350:
   # print("congratulations you have qualified")
#else:
    #print("sorry you have failed")
#grading system
average=marks/5
if average >=80 and average <=100:
    print("A")
elif average>=70 and average <80:
    print("B")

elif average >= 60and average < 70:
    print("C")

elif average >=50 and average < 60:
    print("D")
else:
    print("null")


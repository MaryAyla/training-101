#implement a functuin that takes as input three variables,and returns the largest of the three.Do this without using
# the pythonmax () function.
def large_var(x):
    var=[J,K,L]
    var.sort()
    largest=var[-1]
    return largest
J=int(input("please enter variable1: \n"))
K=int(input("please enter variable2: \n" ))
L=int(input("please enter variable3: \n"))
var= [J,K,L]
var.sort()

print("the largest variable is  {}".format(var[-1]))

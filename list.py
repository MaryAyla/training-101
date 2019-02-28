emptyString=" "
print(type(emptyString))
myFirstNumber=0
emptylist=[]
noiseMakers=["Brian" ,"Mike",9,True,emptyString]

daysoftheweek=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(daysoftheweek)
print (len (daysoftheweek))

#list indexing
print(daysoftheweek[2])
print(daysoftheweek[3:3])
#reverse in strings
details=["Mwende", 60, "caroline@gmail.com", "location"]
age=details[1]
location=details[3]

reverse=details[-3:3]
print("reverse",reverse)
numbers=[0,1,2,3,4,5,6,7,8,9,10]
subnum=numbers[-3:-1]
print(subnum)
print(daysoftheweek)
#appending adds to the last value of the list
daysoftheweek.extend(numbers)
print(daysoftheweek)
#extending a list
list1=[0,1]
list2=[2,3]
list3= list1+list2
list1.extend(list2)
print(list1)

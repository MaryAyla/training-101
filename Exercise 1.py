sentence = "the dog finished the pie"

#write a python program to answer below questions
#1.how many words are in the string
test_string = "the dog finished the pie"
print ("The original string is : " + test_string)
res = len(test_string.split())
print ("The number of words in string are : " +  str(res))

#2. what is the length of string sentence
print (len (sentence))
#3.how many times does 'dog' appear
print(sentence.count("dog"))
#4.write a new string similar to sentence except all letters are capital
print(sentence.upper())



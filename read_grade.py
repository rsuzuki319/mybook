import os

inputr=open("my_grade.txt")

print ("read all content to a string")
s=inputr.read()

print (s)

inputr.close()	
#read N bites
print ("read N bites")
inputr=open("my_grade.txt")

ss=inputr.read(20)
print (ss)

inputr.close()

print ("read line by line")
inputr=open("my_grade.txt")

sss=inputr.readline()
print (sss)
inputr.close()
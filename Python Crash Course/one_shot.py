

#Python :

x = 5
y = "apple"
z = 3.14
print(x,y,z)


x = "Hell World"
print(x.upper())

#1. List 2. Tuples 3.Sets 4.Dictionaries

list1 = ["apple","Mango"]
list1.append("Orange")
list1.remove("apple")
list1.sort()
print(list1)

tuple1 = tuple(list1)
print(tuple1)
x = list(tuple1)
x.insert(1,"kiwi")
tuple1 = tuple(x)
print(tuple1)

set1 = set(tuple1)
set1.add("orange")
print(set1)


dict1 = {"fruits":["mango","orange","apple"],"year":2015}
x= dict1.values()
dict1['color'] = "Red"
dict1.pop("year")
print(x)

num = int(input())
if num%2 ==0:
    print("Number is even")
    
else :
    print("odd")
    
    
i = 1
while i<17:
    print(i)
    i+=1
    
    
num  = 5
for i in range(num):
    print(5*i)
    
def add(num1,num2):
    sum = num1 +num2
    return sum

print(add(14,90))


def greet(name):
    print("Hello ,how are you",name)
    
greet("mohit")


try:
    print(x)
except Exception as e:
    print("inside")
    
    
    
#File Handling:
# f = open("Data.txt","w+")
# f.close() 

# f = open("data.txt","a")
# f.write("This is a test")
# f.close()

f = open("data.txt","r")
print(f.read())
f.close()

import os
os.remove("Data.txt")

import datetime
from time import sleep

while True:
    time = datetime.datetime.now()
    print(time)
    sleep(6)

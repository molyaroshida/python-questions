#!/usr/bin/env python
# coding: utf-8

# # if elif else conditonal statements

# In[24]:


# Positive, Negative, or Zero
#Write a program that takes a number as input and prints whether it is positive, negative, or zero.


# In[2]:


num = int(input('enter the  number '))


# In[3]:


if num>=0:
    if num==0:
        print("its zero")
    else:
        print("its positive")
else:
    print("its negative")


# In[ ]:


Even or Odd
Write a program that takes an integer as input and determines whether it is even or odd.


# In[8]:


num = int(input('enter the  number '))


# In[9]:


if num>=0:
    if num!=0:
        print("its odd")
    else:
        print("its even")


# In[ ]:





# In[1]:


age = input("enter your age ")
name = input("enter your name ")
print(f"Asalamu alaikum , your name is {name} , and your age is {age}")

# have used . format funnction


print("Enter the first number ")
n1 = input()
print("Enter the first number ")
n2 = input()
print("sum of these teo numbers are", int(n1) + int(n2))


# In[2]:


#please  dont remove
"""this is a multi line comment"""
"""this is 
a multi line comment"""
print('hello worl' , end =" subbhanallah ")                               # we can also add two print statements in one row as well
print("alhamdulilallah mashallah")                                        # default end is a new lline character
print('molya roshida "," salam')                                          # anotheer way of method of adding print statement


# variables ==placeholder where we can store our data
var1 = "hello world"  # string
var2 = 5    # integer
var3 = 36.7 # float
var4 = 'asalamu alaikum'
print(var1 + var4)
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var1 + var4))                                   # always remember that string and int will never concinated/
                                                           # it should be both string then only it will be concinate
print(type(var1 + var4))
print(type(var2 + var3))

# typecasting
var5 = "54"
var6 = "32"
print(var5 + var6)   # string
print(int(var5 )+int(var6))
print(10*"hello")
"""string()
int()
float()"""
print(10*"hello\n")                                       # \ == new line character






#string#
my_str = "aslamu alaikum"
print(my_str)

















# In[4]:


print("what is your age?")
age = int(input("enter your age"))
if age<18:
    print("you are not eligible for driving")

elif age==18:
    print("come physically and then we will decide acording to your fittness")
    
else:
    print("yes you are eligible for driving")


# In[6]:


print("what is your age?")
age = int(input("enter your age"))

if age>18:
     print("yes you are eligible for driving")
elif age==18:
     print("come physically and then we'll decide acording to your fittness")
else:
     print("you are not eligible for driving")


# In[9]:


age = input("enter your age ")
name = input("enter your name ")
print(f"Asalamu alaikum , your name is {name} , and your age is {age}")


# In[10]:


print("Enter the first number ")
n1 = input()
print("Enter the first number ")
n2 = input()
print("sum of these teo numbers are", int(n1) + int(n2))


# In[19]:


#design a calculator which will correctly solve all the problems except 45*3 = 555, 54+9 = 77, 56/6 = 4
  #your program should take operatoers and the two numbers as input from the user and then return the result
# faulty calculator    
    


# In[2]:


print("welcome to the best calculator for your maths test")
print("enter the first number")
num1=int(input())
print("enter the second number")
num2=int(input())
operator = input()

if num1==45 and num2==3 and operator=="*":
    print('the answer is 555')
elif num1==54 and num2==9 and operator=='+':
    print("the answer is 77")
elif num1==56 and num2==6 and operator=='/':
    print("the answer is 4")
else:
    if operator=="+":
        print(num1+num2)
    if operator=="-":
        print(num1-num2)
    if  operator=="*":
        print(num1*num2)
    if operator=="/":
        print(num1/num2)
        
        
        


# In[ ]:


connect internet 
n click windows 
settings 
windows update
advance click 
optinal updates
name will be therre and check in (tick)
download


# In[1]:


num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1>=num2 and num1>num3:
    print("num1 is the largest")
elif num2>num1 and num2>num3:
    print("num2 is the largest")
else:
    print("num3 is the largest")
   


# In[ ]:





# In[ ]:





# # Assignment- 1

# In[1]:


#1.Checking if a number is positive, negative, or zero


# In[6]:


num = int(input())


# In[7]:


if num>=0:
    if num==0:
        print("its zero")
    elif num>0:
        print("its postive")
else:
    print("its negative")
    
        
    


# In[8]:


#3: Determining the largest of three numbers


# In[3]:


num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1>=num2 and num1>num3:
    print("num1 is the largest")
elif num2>num1 and num2>num3:
    print("num2 is the largest")
else:
    print("num3 is the largest")
#print("The largest number among these {k}".format(k = largest))


# In[10]:


# 4: Checking eligibility for voting


# In[14]:


age = int(input("enter your age "))


# In[15]:


if age>18:
    print("you are eligible for voting")
    print("you have rights to vote as a citizen of the country")
else:
    print("you are not eligible for voting as you are below 18")
    


# In[ ]:





# In[16]:


## 5: Triangle Type Write a program that takes the 
#lengths of three sides of a triangle as input and determines whether it's an equilateral, isosceles, or scalene triangle.


# In[3]:


a = int(input("Enter the first number "))
b = int(input("Enter the second number "))
c = int(input("Enter the third number "))


# In[4]:


if a==b==c:
    print("Triangle is a equilateral triangle")
elif a==b or a==c or b==a or b==c:
    print("Triangle is a Isosceles trianlge")
else:
    print("Trianlge is a scalane trianlge")


# In[5]:


#6: Temperature Conversion
#Write a program that converts a temperature from Celsius to Fahrenheit or vice versa based on user input.


# In[2]:


#7: Grade Calculation
#Write a program that takes a student's score as input and outputs their corresponding grade.


# In[7]:


scores = int(input("Enter the scores i.e obtained by the students: "))


# In[15]:


print("Enter the scores i.e obtained by the students: ")

if scores>=90:
    print("Grade: o")
elif scores>=80 and scores<=90:
    print("Grade : A+")
elif scores>=70 and scores<=80:
    print("Grade: A")
elif scores>=60 and scores<=70:
    print("Grade: B+")
elif scores>=50 and scores<=60:
    print("Grade: B")
elif scores>=40 and scores<=50:
    print("Grade: C+")
elif scores>=30 and scores<=40:
    print("Grade: C")
else:
    print("fail")
    
    


# In[ ]:





# In[17]:


#8: Login System
#Create a simple login system where the user needs to input a username and password. 
#Allow access if both the username and password match predefined values.


# In[ ]:





# In[20]:


username = input("Enter the username to be given:")

password = input("Enter the password to be given:")



# In[31]:


if users():

    if username in users and users[username]==password:
        print("login successful")
    else:
        print("invalid username of password, please try again")


# In[ ]:





# In[32]:


#9: Divisibility Check
#Write a program that checks if a number is divisible by both 3 and 5, only by 3, only by 5, or not by either.


# In[49]:


num = int(input())
if num%3==0 and num%5==0:
    print('num is divisible by both 5 & 3')
elif num%3==0 and num%5!=0:
    print('num is divisible by 3')
elif num%3!=0 and num%5==0:
    print('num is divisible by 5')
else:
    print('num is not divisible')


# In[ ]:





# # Assignment - 2

# In[50]:


#Example 1: Countdown
#Write a program that takes a positive integer as input and counts down from that number to 1.



# In[1]:


i = int(input("Enter your positive integer: "))


# In[2]:


if i>=1:
    while(i>=1):
        print(i)
        i-=1


# In[1]:


#Example 5: Number Guessing Game
#Create a number guessing game where the program generates a random number between 1 and 100, and 
#the user needs to guess it.


# In[4]:


guess = int(input("Enter the guessing number to be guessed between 1 and 100: "))


# In[6]:


#number = random.randrange(1 and 100)
while guess!=number:
    if guess<number:
        print("You need to guess higher , please try again")
    else:
        print("You need to guess lower, please try again")
        
print("You guessed the number corretly")        
        
    


# In[2]:


import random 

number = random.randint(1,100)
guess = 0

#guess = int(input("Enter guess: "))

while guess!= number:
    guess = int(input("Enter guess: "))
    if (guess<number):
         print("Guess higher")
    elif guess>number:
         print("Guess lower")
    else:
        print("congratulations You won")
        


# In[ ]:





# In[4]:


print("The sum of two digits are: ")
a = int(input("Enter your digit: "))
print("The sum of two digits are: ")
b = int(input("Enter your digit: "))

sum_ = 0
while(sum_!=0):
    digits = number%10


# In[ ]:


correct_password = "shahida"
guess = input("pleae guess the password: ")

while guess!=correct_password:
    digits = number%10
    guess = input("pleae guess the password: ")
    print("incoreect password, please try again")


# In[6]:


num = int(input())
if num%3==0 and num%5==0:
    print('num is divisible by both 5 & 3')
elif num%3==0 and num%5!=0:
    print('num is divisible by 3')
elif num%3!=0 and num%5==0:
    print('num is divisible by 5')
else:
    print('num is not divisible')


# In[ ]:





# In[ ]:





# In[ ]:





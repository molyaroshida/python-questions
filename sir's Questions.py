#!/usr/bin/env python
# coding: utf-8

# # Questions on For Loop
# #Question 1: Print Even Numbers Write a program that prints all even numbers between 1 and 20.
# 
# 

# In[4]:


for i in range(1,21):
    if i%2==0:
        print(i)


# In[69]:


#Question 2: Calculate Factorial Write a program that calculates the factorial of a given positive integer.
fact = 1
num = int(input("Enter the number that you want to factorise : "))
org = num
while num>0:
    fact = fact = num
    num = num - 1
print("The factorial of ",org," is" , fact)    


# In[ ]:





# In[ ]:


#Question 3: Print Multiplication Table Write a program that takes an 
    #integer as input and prints its multiplication table up to 10


# In[14]:


n = int(input("multiplication table : "))


# In[21]:


for i in range(1,11):
    print(" {} * {} = {}".format(n,i, n*i))
    


# In[25]:


t = int(input("multiplication table : "))


# In[26]:


for i in range(1,11):
    print("{} * {} ={}".format(t, i, t*i))               
else:
    print("all done")


# In[68]:


#Question 4: Calculate Sum of Digits Write a program that calculates the sum of the digits of a given number.



# In[31]:


sum_ = int(input(" enter the sum of digits : ") )


# In[96]:


print("Enter the first number ")
n1 = input()
print("Enter the first number ")
n2 = input()
print("sum of these two numbers are", int(n1) + int(n2))
    


# In[ ]:


#Question 5: Calculate Fibonacci Series Write a program that generates the Fibonacci series up to a given number of terms.


# In[ ]:





# # pattern printing

# In[12]:


#Question 3: Right Triangle Number Pattern
#Write a program to print a right triangle number pattern

1
12
123
1234
12345

n = int(input("enter your number: "))
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()


# In[79]:


n = int(input("enter youe number: "))


# In[80]:


for i in range(n, 0, -1):                 
    print("*"*i)                     
                       


# In[87]:


#n = int(input("enter your number: "))
l = 0
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(l),end=" ")
        l=l+1
    print()
    l=0
    


# In[46]:


#Question 2: Hollow Square Pattern
#Write a program to print a hollow square pattern of asterisks (*) with a side length of 5.

*****
*   *
*   *
*   *
*****


# In[71]:


num = int(input("enter the number for ros and col: "))

for i in range(num):
    for j in range(num):
        if i ==0 or i == num-1 or j ==0 or j==num-1:
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()       


# In[ ]:


#Example 9: Divisibility Check
#Write a program that checks if a number is divisible by both 3 and 5, only by 3, only by 5, or not by either.


# In[103]:


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





#!/usr/bin/env python
# coding: utf-8

# # TEST - 1:

# # 1 . name of two modes in python:
#    - interactive mode
#    - script mode
# 
# 

# # 2. Interface mode of python is also called
#  - python shell

# # 3. write the full form of IDLE:
#   - Intergated developement learning environment 

# In[11]:


# 4. write te output of the following

t = 5

y = 7

print(t+y)


# In[12]:


2**5


# # 5. write a drawback of interactive mode
#  - we can not save our commands 

# # 6. Tuli purchased 5 pencils & 2 erasers at the cost of Rs 7 and Rs 5 respectively.
# #write a program to calculate and display the total amount paid by tuli 

# In[11]:


pen = 7
eraser = 5
TC= pen*5+2*eraser

print(" Total amoount paid by tuli is",TC)


# In[15]:


# 7.  what do u mean by comments
# commentsis basically , when we wants to remember something of a particular lines or statements.
# with the symbol of (#)
# non executable lines that we cannnot execute or command


# # 8. what is variables?
#  - variables is a placeholder wher we store our data

# In[ ]:





# # TEST - 2:

# # 1.What is the is purpose of creating variables?
#   the main purpose of creating variables is to give a placeholder where we store or save our data or values 
#   in the form of small, capital or underscore(_) or combination of all 3 except digits or specail characters like 2 or @ ,
#   it will give an error.

# # 2. write the code to find  the address of variable?
#    id is the code to find  the address of variable.
#    Ex:
#     
# x = 2
# id(x)

# In[19]:


X = 2

id(X)


# # 3. what do you mean by datatype?
#   - datatype is a type function which tells about which datatype is belongs to which type of value as used for ex:
#         1.integer
#         2.float
#         3.string
#         4.floor
#         5.boolen
#         6.complex

# In[2]:


# 4. write 3 numeric data type in python?
# ans. integer,floating ,complex 


# # 5. name the 3 sequential data types in python?
#  - list , tuple and string

# In[5]:


# 6. write the data type of variables x and y.
x = 100

type(x)


# In[6]:


y = 12.2

type(y)


# # 7. data type variable is according to the value it holds. state whether it true or false?
#  - true

# In[7]:


# 8. which datatype store the combination of real and imaginary numbers?
# ans: compplex


# In[9]:


# 9. write the output of followinf

3.9e2


# In[10]:


4.7e7                                   # the number of e is given it will provide the exact number of zeros


# In[11]:


2.5e10


# In[12]:


# 10. which datatype returns the value true or false?
# ans: boolen


# In[ ]:





# # TEST - 3:

# In[13]:


# Q1. write the output of the following 


# In[14]:


(75>2**5)


# In[15]:


(25!=5*2)


# In[16]:


5**2


# In[17]:


# Q2 . which operator can be changed in above part 2 so that it returns true?
# ans: == in the place of !=

(25==5*2)                                    # doubt to ask to sir


# In[18]:


# Q3. dictionary is enclosed in _ brackets.
# ans: curly brackets{}


# In[19]:


# Q4. what do u mean by keywords in python?
# ans: kewywords are  reserved words. we can not use variable name or any other identifier


# In[20]:


# Q5. keywrods can be used as variable names.(t/f)
# ans: false


# In[9]:


# Q6. write the code to display all keywords in python.

import keyword
t = keyword
print("keyborad")


# In[31]:


# Q7.write two keywords which starts with capital letters 
# ans: True or False


# In[5]:


# Q8. write the output of the following 
#str = "informatics"
#str[3]='e'

# ans: type error as it does not support assignment operator

str = "informatics"
str[3]


# In[40]:


# Q9. write the output of the following:
a = [1,2,3]
a[0]=6
print(a)


# In[41]:


a = [1,2,3]
a[1]=6
print(a)


# In[44]:


a = [1,2,3]                 # replace
a[2]=6
print(a)


# # Q10. write the operators:
# 
# 1. Arithmetic operators == +, -, *, /, // ,**, %
# 
# 2. Comparision Operators == > ,>=, <, <=, ==, !=
# 
# 3. Logical Operators == AND, OR, NOT
# 
# 4. Bitwsie Operators == Bitwsie AND, Bitwise OR, Bitwsie XOR,
# 
# 5. Assignment operators == +=, -=, *=, /=, //=, **=, %=,
# 
# 6. special operators :
#    1. membership operator = in , not
#    2. Special Operators = is, is no

# In[ ]:





# # TEST- 4

# In[11]:


# Q1. write the following output:
x = 8
x = 10
print(x+x)              


# In[14]:


x = 10
y = 12
print(y+x)              


# In[53]:


# Q2. what do u mean by escape sequence?
# ans: sequwnce .after backlasah is called escape sequence


# In[54]:


# Q3. write the output of the following:
x = 2+5j
print(x.real,x.imag)


# In[55]:


x = 8+9j
print(x.real,x.imag)


# # Q4. what is the none datatype?
# this data type is used to define null or no value . for ex: m = none , now the variable 'm' is not pointing to any value , imstead it is pointing to none
#     

# In[58]:


# Q5. write the following 
v1 = 10
v2 = None

print(v2)


# In[15]:


v1 = 10
v2 = None

print(v1)


# # Q6. what is the main purpose of type() function?
# this function tell us about the which datatype of a variable. ex:
#     

# In[59]:


a = 45
type(a)


# In[60]:


a = 45
print(type(a))


# # Q7. write the following:
# 

# In[62]:


type(10)


# In[63]:


type(12.4)


# In[64]:


type("tuli")


# In[65]:


type(True or False)


# In[67]:


type(4+5j)


# # Q8. which function is used for find the datatype of vairaible?
# type function

# # Q9. WRITE THE FOLLOFOLLOWING:
# 

# In[69]:


a = "hello"


# In[70]:


print(a)


# In[72]:


b = 10


# In[73]:


print(b)


# In[75]:


c = 2.5


# In[76]:


print(c)


# In[77]:


d = 6+8.5j


# In[78]:


print(d)


# # Q10. identify the variable name,variable types,value operator used in the following statement 
# 
# # b = 9
# 
#     -variable name = b
#     -variable types = int
#     -operator (=)
#     -value = 9
# 
# 
# 

# # Q11 what do you mean by assignment operator?
#  - addignment operator is used as to assign a value t a variable is known as assignment operator 

# In[ ]:





# # TEST - 5:

# # Q1. write 7%10 and see the what return will it give

# In[81]:


7%10     


# In[82]:


5%4


# In[83]:


10%3


# In[84]:


10%2


# In[85]:


32%5


# In[86]:


32//5


# In[88]:


32/5


# In[89]:


65*4


# In[90]:


7%3


# In[91]:


7%5


# In[92]:


7%9


# # Q2. is the following statement is correct or not.
# a, b,c=8,Amit,5

# # Q3. identify the invalid variable names from the following and specify the reason for this also 
#   - a) m_m
#   -  b) unit_day
#   - c)45apple
#   -  d)#sum
#   -  e)for
#   - f)s name

# # ans
# - m_m                  :  true
# - unit_day             :  true
# - 45apple              :  false # a variable will never starts with any numbers
# - #sum                 :  false # a variable will never starts with any special characters 
# - for                  :  false # a variable will never starts with any keywords 
# - s name               :  false # a variable will never starts with any given spaces between 2 letters or 2 words

# # Q4. what do you mean by expression?
#  a combination of operators and operands is known as expression. example:
#         x+5=10

# # Q5. what do you mean by operators?
# operators are the special symbol that perform a specific tasks(arithmatic or lgical operators)
# 
# the 6 operators are :
# 1. Arithmetic operators == +, -, *, /, // ,**, %
# 
# 2. Comparision Operators == > ,>=, <, <=, ==, !=
# 
# 3. Logical Operators == AND, OR, NOT
# 
# 4. Bitwsie Operators == Bitwsie AND, Bitwise OR, Bitwsie XOR,
# 
# 5. Assignment operators == +=, -=, *=, /=, //=, **=, %=,
# 
# 6. special operators :
#    1. membership operator = in , not
#    2. Special Operators = is, is no
# 

# In[ ]:





# # TEST - 6

# In[5]:


4**2


# # Q1. write the following outputs:
#   

# # 
# - print("hello*5")
# - print("hello"*5)
# - print("***"*5)
# - print("hello","how", "R", "u")
# - print(""hello"+"how", "R", "u"")
# - print("amit"+"sethi")
# - print("7+9")
# - print(4+5)
# - print(7//9)
# - print(7%9)
# - print(7**9)
# - print(7*9)
# - print(7-9)

# In[16]:


print("hello*5")


# In[9]:


print("hello"*5)


# In[10]:


print("***"*5)


# In[11]:


print("hello","how", "R", "u")


# In[29]:


print("hello"+"how"+ "R" + "u")


# In[17]:


print(" amit " + "sethi")


# In[17]:


print("7+9")


# In[18]:


print(4+5)


# In[19]:


print(7//9)


# In[20]:


print(7/9)


# In[21]:


print(7**9)


# In[22]:


print(7%9)


# In[23]:


print(7*9)


# In[24]:


print(7-9)


# In[25]:


4**3


# In[26]:


3%7


# In[27]:


8%2


# In[30]:


7%3


# In[31]:


7%7


# # Q2. what do mean by string concatenation? give example.
#   string concatenation means joining the strings . for example:
#        s = "asalamu" + "alaikum"
#         print(s)
# 

# In[5]:


s = "asalamu" + " alaikum "
print(s)

             


# # Q3. what do you mean by binary and unary operators? give one example of each .
#    - Binary operators woks on two or more operators . like( /,*)
#    - Unary operators works on only one operands like (-) 

# In[6]:


# binary
#8/8
#9*8


# In[7]:


# unary
#-9
# -4


# # Q4. evaluate the following  expressions:

# In[8]:


23+4**2


# In[9]:


9*3-8+6


# In[10]:


7%2+7//2


# In[11]:


8//2


# In[12]:


67+3%3


# In[13]:


12%4+6+4//3


# # Q5. write the purpose of the following.
#  - (//) : this is known as floor division , which used as to find the lower integer of any operations
#         when one number is divided by other
#  - (%)  : this is known as mod or modules, which gives the remainder of the divisible numbers .
#  - (**) : this is known as exponents and power, it is used to find the powers of any numbers.  

# In[14]:


# floor 
8//4


# In[15]:


# mod
5%3


# In[16]:


# exponents
6**6


# In[17]:


36*6


# In[18]:


5**5


# In[19]:


3**3


# In[21]:


4**4


# In[ ]:





# In[ ]:





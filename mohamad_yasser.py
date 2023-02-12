#!/usr/bin/env python
# coding: utf-8

# > # Dear Epsilon Students, 
# > # The More you practice The better You'll Be.

# ### Instructions: 
# - Make sure that you understand this topics before you start.
# - If you found something hard to do, try and try then google it and finally ask someone. 
# - You can divide this work into daily tasks so that you do not feel pressure.
# - After you finish, go to model answer and rate yourself. 
# - If you find something ambiguous, Try to make a hypothesis to solve a problem. 

# ### Question classification: 
# - Green is level 1 
# - Orange is level 2 
# - Red is level 3 

# # <center> Let's start 💪 </center> 

# ## <p style="color:green;">Q.01 Write a function takes a two-word string and returns True if both words begin with same letter</p>
# > ('Levelheaded Llama') → True
# 
# > ('Crazy Kangaroo') → False

# In[1]:


def check_first_letter(s):
    
    g=s.split()

    if g[0][0]==g[1][0]:
        return(True)
    else:
        return(False)


# ## <p style="color:green;">Q.02 Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd</p>
# 
# > (2,4) → 2
# 
# > (2,5) → 5

# In[ ]:


def odd_even(x,y):

    if x%2==0, y%==0:
        if x<y:
            return(x)
        elif x>y:
            return(y)
        
    elif x%2=!0, y%=!0:
        if x<y:
            return(x)
        elif x>y:
            return(y)


# ## <p style="color:green;">Q.03 Write a function that capitalizes the first and fourth letters of a name</p>
# > ('macdonald') → MacDonald

# In[ ]:


def capitalize_letter(x):

  x=list(x)
  x[0]=x[0].upper()

  x[3]=x[3].upper()

  x="".join(x)

  return(x)


# ## <p style="color:green;">Q.04 Given a sentence, return a sentence with the words reversed</p>
# > ('I am home') → 'home am I'

# In[ ]:


y='I am home'
y=y.split()
y=y[ ::-1]
y=" ".join(y)
y


# ## <p style="color:orange;">Q.05 Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.</p>
# > has_33([1, 3, 3]) → True
# 
# > has_33([1, 3, 1, 3]) → False
# 

# In[ ]:


def Moh_Y(x):
    for i in range(len(x)-1):
        if x[i:i+2] == [3,3]:
            return (True)
    return (False)


# ## <p style="color:orange;">Q.06 BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'¶</p>
# 
# >blackjack(5,6,7) → 18
# 
# >blackjack(9,9,9) → 'BUST'
# 
# >blackjack(9,9,11) → 19

# In[ ]:


def blackjack(x,y,z):
  if (x+y+z)<21:
    print(x+y+z)
  elif (x+y+z)>21 and x==11 or y==11 or z==11:
    if (x+y+z)-10<21:
      print(x+y+z-10)
  else:
    print('BUST')
  

blackjack(5,6,7)


# ## <p style="color:red;">Q.07 SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.</p>
# >summer_69([1, 3, 5]) → 9
# 
# >summer_69([4, 5, 6, 7, 8, 9]) → 9
# 
# >summer_69([2, 1, 6, 9, 11]) → 14

# In[ ]:


def func_1(l):
  l1=l[:l.index(6)]
  l2=l[l.index(9)+1:]
  return(sum(l1)+sum(l2))

func_1([2,1,6,9,11])


# ## <p style="color:red;">Q.08 SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order</p>
# 
# >spy_game([1,2,4,0,0,7,5]) → True
# 
# > spy_game([1,0,2,4,0,5,7]) → True
# 
#  >spy_game([1,7,2,0,4,5,0]) → False
# 

# In[2]:


def func_2(x):
  for i in range(len(x)):
      if (x[i:i+3])==[0,0,7]:
        return(True)
  else:
    return(False)
        
func_2([1,2,4,0,0,7,5])


# ## <p style="color:green;">Q.09 Write a function that checks whether a number is in a given range (inclusive of high and low)</p>
# 

# In[ ]:


def ran_check(num,low,high):
    for i in range(low,high+1):
        if num==i:
            print('Number is within the range')
            break
    else :
            print('Number is out of range')
ran_check(6,5,9)


# ## <p style="color:orange;">Q.10 Write a Python function to multiply all the numbers in a list.</p>
# > Sample List : [1, 2, 3, -4]
# 
# > Expected Output : -24

# In[ ]:


def mult_list(l):
  x=1
  for i in l:
    x =x*i
  return(x)
   
mult_list([1,2,3,-4])


# ## <p style="color:red;">Q.11 Write a Python function that checks whether a passed string is palindrome or not.</p>
# >Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

# In[ ]:


def is_palindrome(s):
  if s[::-1]==s[0:]:
    print('palindrome')
  else:
    print('not palindrome')

is_palindrome('madam')


# ## <p style="color:green;">Q.12 Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument
# 

# In[ ]:


x=lambda a : a+15

x(5)


# ## <p style="color:green;">Q.13 create a lambda function that multiplies argument x with argument y and print the result.</p>
# 

# In[ ]:


x = lambda a, b : print(a * b)

x(6,5)


# ## <p style="color:orange;">Q.14 Write a Python program to filter a list of integers using Lambda. </p>
# > Original list of integers:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 
# > Even numbers from the said list:[2, 4, 6, 8, 10]
# 
# > Odd numbers from the said list:[1, 3, 5, 7, 9]
# 

# In[ ]:


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)
print("\nEven numbers from the said list:")
even_nums = list(filter(lambda x: x%2 == 0, nums))
print(even_nums)
print("\nOdd numbers from the said list:")
odd_nums = list(filter(lambda x: x%2 != 0, nums))
print(odd_nums)


# ## <p style="color:green;">Q.15 Write a Python program to triple all numbers of a given list of integers. Use Python map.</p>
# 

# In[ ]:


l=[1,2,3,4]
result = map(lambda x: x + x + x, l) 
print(list(result))


# ## <p style="color:orange;">Q.16 Write a Python program to add three given lists using Python map and lambda.
# 
# </p>
# 

# In[ ]:


l1 = [1, 2, 3] 
l2 = [4, 5, 6] 
l3 = [7, 8, 9] 

result = map(lambda x, y, z: x + y + z, l1, l2, l3) 

print(list(result))


# ## <p style="color:orange;">Q.17 Write a Python program to square the elements of a list using map() function.</p>
# 

# In[ ]:


def square_l(x):
  return x * x
l = [5, 2, 3, 4]
result = map(square_l, l)
print(list(result))


# ## <p style="color:green;">Q.18 Using filter() function filter the list so that only negative numbers are left.</p>
# > lst1  [12,-1,9,8,-.5,-.2,-100]
# 

# In[ ]:


lst1 =[12,-1,9,8,-.5,-.2,-100]
lst2 = list(filter(lambda x: x<0, lst1))
print(lst2)


# ## <p style="color:green;">Q.19 Using filter function, filter the even numbers so that only odd numbers are passed to the new list.</p>
# > lst1  [22,100,19,13,11,1,4,66]
# 

# In[ ]:


lst1 =[22,100,19,13,11,1,4,66]
lst2 = list(filter(lambda x: x%2!=0, lst1))
print(lst2)


# ## <p style="color:green;">Q.20 Using map() and filter() functions add 2000 to the values below 8000.</p>
# > lst [1000,500,600,700,5000,90000,17500]

# In[ ]:


lst=[1000,500,600,700,5000,90000,17500]
lst2 = list(map(lambda x: x+2000, filter(lambda x: x<8000, lst)))
print(lst2)


# # <center> Thank's for your effort ❤️ </center> 

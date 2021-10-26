from typing import ChainMap


a = "Hello, World!"
print(a.upper())    #For all upper case 

print(a.lower())    #For all lower case 


b = "     Amazong Python    "
print(b.strip())    #To remove white space 


#Replacing Strings
b = "Amazing Python"
print(b.replace("A","J"))

# Splitting Strings
c ="Amazing Python"
d = c.split(" ")
print(d)

""" To split specify where you want to split for the above example we split at space, 
For splitting at commas "," etc."""

a = "Hello World"
b = "in all languages"
c = a + b 
print(c)

# to add space //Add " "

a = "Hello World"
b = "in all languages"
c = a + " " + b
print(c)


# Using format 
age = 45
txt = "My name is John, and I am {}"
print(txt.format(age))

"""The format() method takes unlimited 
number of arguments, and are placed into the respective placeholders"""

quantity = 100
name =" Mickey "
item = "Sweater"
price = 78.98
disc = "I want {} pieces of {} in the item of an {} for a total of {}"
print(disc.format(quantity,name,item,price))

#Using index numbers to change the order to what you want 
quantity = 100
name =" Mickey "
item = "Sweater"
price = 78.98
disc = "I want {2} pieces of {1} in the item of an {0} for a total of {3}"
print(disc.format(quantity,name,item,price))


# To use Quotes inside a string use \"

txt = "Far away in a \"broken\" kingdom. "
print(txt)

# Escape Characters 

# Single quotes \' 
txt = "Far away in a \'broken\' kingdom. "
print(txt)

# Backslash \\
txt = "Far away in a broken\\unhappy kingdom. "
print(txt)

# New Line \n
txt = "Wendy and henry were going in the\ntrain and suddenly they saw fiona."
print(txt)

# Return \r The is only print the latter 
txt = "The adventure of \rthe speckled band "
print(txt)

# Tab \t 
txt = "\tMediocrity knows nothing higher than itself: but talent instantly recognizes genius."
print(txt)

#Backspace \b 
txt = "Education never ends, Watson.\bIt is a series of lessons, with the greatest for the last"
print(txt)

#Form Feed 
txt ="What\f you do in this world is a matter of no consequence."
print(txt)

# Other methods 
txt ="what you do in this World is a matter of no consequence."
print(txt.capitalize())    # First Letter Capital
print(txt.casefold())      #Everything to lower case 
print(txt.count("matter")) #Counts specific words in string 
print(txt.find("no"))      #Searches the string for a specified value and returns the position of where it was found

"""
Different Operators
=   x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3
"""

# Create a program to output numbers 1 to 9 on a seperate line followed by a dot.

print("1\n2\n3\n4\n5\n6\n7\n8\n9\n.")
#or
print("1\n2\n3\n4\n5\n6\n7\n8\n9\n")

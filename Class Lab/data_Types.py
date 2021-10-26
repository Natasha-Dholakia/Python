x ="Hello World"
print (type(x)) #String

x = 20
print(type(x)) #Int

x = 20.5
print(type(x)) #Float

x = 1j
print(type(x)) #Complex

x = ["Apple","Kiwi","Mango"]
print(type(x)) #List

x = ("Apple","Kiwi")
print(type(x)) #Tuple

x = {"Name": "John", "age" : 34}
print(type(x)) #dict

x = {"apple", "banana", "cherry"}
print(type(x))   #set

x = range(6)
print(type(x)) #Range

x = frozenset({"Apple","Kiwi"})
print(type(x)) #Frozenset

x = True
print(type(x)) #Bool

x = bytearray(5)
print(type(x)) #bytearray

x = memoryview(bytes(5))
print(type(x)) #memoryview


# changing one type to another
x = 1 
y = 2.8
z = 1j
 
a = float(x)
b = int(y)
c = complex(x)

print(a,b,c)
print(type(a),type(b),type(c))


#Random number between 1-9
import random
print(random.randrange(1,10))

a = "Hello, World!"
print(a[1])   # This will print letter "e"

a = "Hello, World!"
print(len(a))

#looping Stings

for x in "Apple":
    print(x)

txt = "The best things in life are free!"
print("free" in txt)  

##############   Go to Looping.py ###############
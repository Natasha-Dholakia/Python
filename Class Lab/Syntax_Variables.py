x = 5 
y = "John"
print(x,",",y)

#Casting tells you the format 
x = 5 
y = "John"
print(type(x))
print(type(y))

#A will not override a
a = "sally"
A = "Molly"
print(A,a)

#x, y, z all have the value of an orange 
x = y = z = "Orange"
print(x,y,z)

fruits = ["Apple", "Orange", "Banana"]
x,y,z = fruits
print(x)
print(y)
print(z)

x = "My Life "
y = "is Awesome. "
z =(x + y)
print(z)

#Global Varibales
x = "Awesome"

def myfunc():
    x ="Fantastic "
    print("Python is " + x )

myfunc()
print("Python is " + x )
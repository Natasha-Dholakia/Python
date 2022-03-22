thislist = ["apple", "banana", "cherry"]
print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)


listt = ["abc", 34, True, 40, "male"]
print(type(listt))

thislist = list(("apple", "banana", "cherry"))
print(thislist)

#Returning 3rd, 4th, 5th item in list 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#Changing the items
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3]= ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple","banana","cherry"]
thislist[1:2] = "blackcurrant", "watermelon"
print(thislist)


#instering watermelon as third item
thislist = ["apple","banana","cherry"]
thislist.insert(2,"watermelon")
print(thislist)

#appending an item // adds an item towards the end of the list 
thislist = ["apple","banana","cherry"]
thislist.append("orange")
print(thislist)

# to insert an item to a specific area use insert 
thislist = ["apple","banana","cherry"]
thislist.insert(1,"strawberry")
print(thislist)

#extend // adding another list to the existing list
thislist = ["apple","banana","cherry"]
tropical = ["mango", "kiwi", "pineapple"]
thislist.extend(tropical)
print(thislist)


#add any thing to the list // we added tuple
thislist = ["apple","banana","cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#Removing 
thislist = ["apple","banana","cherry"]
thislist.remove("banana")
print(thislist)

#removing specific index // using POP
thislist = ["apple","banana","cherry"]
thislist.pop(1)
print(thislist)

# if pop not specified it removes the last item
thislist = ["apple","banana","cherry"]
thislist.pop()
print(thislist)


#del also removes specific index
thislist = ["apple","banana","cherry"]
del thislist[0]
print(thislist)

#deleting the entire list
thislist = ["apple","banana","cherry"]
del thislist
#print(thislist) #this will cause an error because you have succsesfully deleted "thislist".


# using clear empties the list 
thislist = ["apple","banana","cherry"]
thislist.clear()
print(thislist)

#printing all items reffering to index number 
thislist = ["apple","banana","cherry"]
for i in range(len(thislist)):
    print(thislist[i])

#Using while loop 
thislist = ["apple","banana","cherry"]
i = 0 
while i < len(thislist):
    print(thislist[i])
    i = i + 1


#Using list comprehension 
thislist = ["apple","banana","cherry"]
[print(x) for x in thislist]
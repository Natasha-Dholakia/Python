# Problem Name: Two Number Sum 

# Problem Description: Write a function that takes in a non-empty 
# array of distinct integers and an integer representing a target sum. 
# If any two numbers in the input array sum up to the target sum,
# the function should return them in an array, in sorted order. 
# If no two numbers sum up to the target sum, the function should 
# return an empty array. Assume that there will be at most one pair 
# of numbers summing up to the target sum.

# You can assume that there will be at most one pair of numbers summing 
# up to the target sum.

####################################
# Sample Input: array = [3, 5, -4, 8, 11, 1, -1, 6], targetSum = 10
# Sample Output: [-1, 11]
####################################
"""
Explain the solution: 
#hints1: 
# Try using two for loops to sum all possible pairs of numbers in the input array. 
# What are the time and space implications of this?

#hints2:
# Realize that for every number X in the iput array, you are essentially trying to find
# the number Y in the input array such that X + Y = targetSum.
# With two variables in this equation known to you, it shouldn't be too hard to solve for Y.


#hints3:
# Try storing every number in a hash table, solving the equation mentuined in Hint#2
# for every number and checking of the Y that you found is stored in the hash table.
# What are the time and space implications of this?

##################
Detailed explanation of the Solution:
# solution1
#O(n^2) time | O(1) space
function twoNumberSum(array, targetSum):
    loop for i in range(len(array)): #i is the first number
        firstNum is equal to array[i] #firstNum is the first number
        loop for j in range(i+1, len(array)): #j is the second number
            secondNum is equal to array[j] #secondNum is the second number
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []

# solution2
#O(n) time | O(n) space
function twoNumberSum(array, targetSum):
    nums is a hash table #create a hash table
    loop for num in array: #loop through the array
        potentialMatch is equal to targetSum - num #find the potential match
        if potentialMatch in nums: #if the potential match is in the hash table
            return [num, potentialMatch] #return the two numbers
        else: #if the potential match is not in the hash table
            nums[num] = True #add the number to the hash table
    return [] #return an empty array


#solution3
#O(nlog(n)) time | O(1) space

function twoNumberSum(array, targetSum):
 sort the array 
    left is equal to 0 #left is equal to 0
    right is equal to len(array) - 1 #right is equal to len(array) - 1
    while left < right: #while left is less than right
        currentSum is equal to array[left] + array[right] #currentSum is equal to array[left] + array[right]
        if currentSum == targetSum: #if currentSum is equal to targetSum
            return [array[left], array[right]] #return the two numbers
        elif currentSum < targetSum: #if currentSum is less than targetSum
            left += 1 #increment left
        else: #if currentSum is greater than targetSum
            right -= 1 #decrement right
    return [] #return an empty array

"""

####################################
#O(n^2) time | O(1) space
def twoNumberSum(array, targetSum):
    for i in range(len(array)-1): #i is the first number
        firstNum = array[i] #firstNum is the first number
        for j in range(i+1, len(array)): #j is the second number
            secondNum = array[j] #secondNum is the second number
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum] #return the two numbers
    return [] #if no two numbers sum up to the target sum, return an empty array

print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))


#####################################
#O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    nums = {} #create a hash table
    for num in array: #loop through the array
        potentialMatch = targetSum - num #find the potential match
        if potentialMatch in nums: #if the potential match is in the hash table
            return [num, potentialMatch] #return the two numbers
        else: #if the potential match is not in the hash table
            nums[num] = True #add the number to the hash table
    return [] #if no two numbers sum up to the target sum, return an empty array


#######################################
#O(nlog(n)) time | O(1) space

def twoNumberSum(array, targetSum):
    array.sort() #sort the array
    left = 0 #left is equal to 0
    right = len(array) - 1 #right is equal to len(array) - 1
    while left < right: #while left is less than right
        currentSum = array[left] + array[right] #currentSum is equal to array[left] + array[right]
        if currentSum == targetSum: #if currentSum is equal to targetSum
            return [array[left], array[right]] #return the two numbers
        elif currentSum < targetSum: #if currentSum is less than targetSum
            left += 1 #increment left
        else: #if currentSum is greater than targetSum
            right -= 1 #decrement right 
    return [] #if no two numbers sum up to the target sum, return an empty array

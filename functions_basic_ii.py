
# 1. Countdown - Create a function that accepts a number as an input.
# Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def countdown(x):
    countdown_list = []
    for x in range(x,-1,-1):
        countdown_list.append(x)
    return countdown_list

print(countdown(10))

# 2. Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.

def list_return(a,b):
    print(a)
    return b

list_result = list_return(8,24)
print(list_result)

# 3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

def first_plus_length(x):
    list = x
    return list[0] + list[len(list)-1]

addition_result = first_plus_length([5,4,3,2,1])
print(addition_result)

# 4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False

def values_greater_than_second(x):
    new_list = []
    count = 0
    if len(x) < 2:
        return False
    for i in range(0,len(x)):
        if x[i] > x[1]:
            new_list.append(x[i])
            count += 1
    print(count)
    return new_list

list_result = values_greater_than_second([12,7,8,13,2])
print(list_result)

# .5 This Length, That Value - Write a function that accepts two integers as parameters: size and value.
# The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

def this_length_that_value(size,value):
    new_list = []
    for i in range(0,size):
        new_list.append(value)
    return new_list



list_updated = this_length_that_value(8,12)
print(list_updated)
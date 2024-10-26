"""Topic :List
Exercise
Q1. Create a list of 5 random numbers and print the list.
Q2. Insert 3 new values to the list and print the updated list.
Q3. Try to use a for loop to print each element in the list."""

#Q1
# import random
# l=[random.randint(1,100) for _ in range(5)]
# print(l)
# #
# #Q2
# l.extend([55,44,22])
# print(l)
#
# #Q3
# for i in l:
#     print(i)

"""Topic: Dictionary
Exercise 
Q1. Create a dictionary with keys 'name', 'age', and 'address' and values 'John', 25, and 
'New York' respectively.
Q2. Add a new key-value pair to the dictionary created in Q1 with key 'phone' and 
value '1234567890'."""

# #Q1.
# newdictionary ={
#     "Name":"John",
#     "Age":"25",
#     "Address":"New York"
# }
#
# #Q2.
# print(newdictionary)
# newdictionary["phone"]="9827387298"
# print(newdictionary)

"""Topic: Set
Exercise  
Q1.Create a set with values 1, 2, 3, 4, and 5.
Q2. Add the value 6 to the set created in Q1.
Q3. Remove the value 3 from the set created in Q1.
"""
#Q1.
set1={1,2,3,4,5}
print(set1)

#Q2.
set1.add(6)
print(set1)

#Q3.
set1.remove(3)
print(set1)

"""Topic:Tuple
Exercise 
Q1. Create a tuple with values 1, 2, 3, and 4
Q2. Print the length of the tuple created in Q1."""

tupple1=(1,2,3,4)
print(tupple1)
print(len(tupple1))

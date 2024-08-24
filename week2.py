# Empty list
my_list = []

# Add elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# Insert 15 at the second position in the list
my_list.insert(1, 15)
print(my_list)

# Another list
list2 = [50, 60, 70]
print(list2)

# Add my_list with another list2
my_list.extend(list2)
print(my_list)

# Remove the last element from my_list
my_list.pop()
print(my_list)

#Sort my_list in ascending order
my_list.sort()
print(my_list)

#Find and print the index of the value 30 in my_list
position = my_list.index(30)
print(f"Index of 30 in my_list is: {position}")

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

#Account statement in python
# def name():
#     return f"Hello, {name} Welcome!"
# print(name("victor"))
    

name = input("Enter your name: ")   
balance = int(input("Enter your Balance: "))
credit = int(input("Enter your saving today: "))
debit = int(input("Enter your expenses: "))

#balance sheet
updatedBalance = balance + credit - debit

if balance == updatedBalance:
    print("Books not balancing")
elif balance < updatedBalance:
    print("Your spending morethan what you earn, manage your finances well")
else:
    print("Books balanced")

print(f"Hello {name} Welcome!")
print('=====================')    
print(f"Available balance is : {updatedBalance}")



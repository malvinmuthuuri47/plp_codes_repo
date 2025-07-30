my_list = []

print("Before append", my_list)

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print("After append", my_list)

my_list.insert(1, 15)

print("After insertion", my_list)

my_list.extend([50, 60, 70])

print("After extending", my_list)

my_list.pop()

print("After removing the last element in the list", my_list)

num_idx = my_list.index(30)

print(f"The index of the value 30 is: {num_idx}")

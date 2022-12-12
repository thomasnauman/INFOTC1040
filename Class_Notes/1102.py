# write a for loop
# prints integers 0-4

ls = [0, 1, 2, 3, 4]
for item in ls:
    print(item)

for i in range(0,5):
    print(i)

# create new list
# in new list: every item is corresponding item in ls + 1
# new list should be [1, 2, 3, 4, 5]

new_ls = []
for item in ls:
    new_ls.append(item+1)

print(new_ls)

# list comprehension
new_list_2 = [item + 1 for item in ls]
print(new_list_2)
# syntax: list = [operation for x in y]

new_list_3 = [item*2 for item in ls]
# list should be [0, 2, 4, 6, 8]
print(new_list_3)

new_list_4 = ["Even" for item in ls]
print(new_list_4)

# "Even" only when item is actually even (item % 2 = 0)
new_ls_5 = []
for item in ls:
    if item % 2 == 0:
        new_ls_5.append(f"{item} is Even")
    else:
        new_ls_5.append(f"{item} is Odd")
print(f"Using a For Loop: {new_ls_5}")

new_list_5 = [f"{item} is Even" if item % 2 == 0 else f"{item} is Odd" for item in ls]
print(f"List Comprehension: {new_list_5}")
# weird: if/else goes after "for x in y" if there is only "if", but before "for x in y" if there is if & else

new_list_6 = [item * 10 for item in ls if item == 2]
print(new_list_6)
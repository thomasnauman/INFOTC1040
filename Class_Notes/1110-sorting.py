ls = [9,1,8,2,7,3,6,4,5]
print(ls)

# create a new list
s_ls = sorted(ls, reverse = True)
print(s_ls)

# modifies the list
ls.sort(reverse = True)
print(ls)

tup = (9,1,8,2,7,3,6,4,5)
s_tup = sorted(tup, reverse = True)
print(s_tup)

di = {'name': "Corey", 'job': 'programming', 'age': None, 'os': "mac"}
s_di = sorted(di)
print(s_di)

ls2 = [-6,-5,-4,1,2,3]
s_ls2 = sorted(ls2,key=abs)
print(s_ls2)

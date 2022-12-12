# create a variable with name s, datatype str, value "cat"

s = "Cat"
print(s)

# compiler and interpreter will decode the program, so spaces are not required (just a stylistic choice)

s2 = "has"
s3 = "four legs"

print(s + " " + s2 + " " + s3)
print("A {} {} {}".format(s,s2,s3))
print(s,s2,s3)

x = ("apple", "banana", "cherry")
# x is a tuple, which is a collection of strings, integers, other datatypes; they are immutable, unlike lists

myself = ("name", "age", "email")
print(myself)

def put_them_together(x, y, z):
    print(x,y,z)
# everything inside the parenthesis after the function, called parameters

combined = put_them_together(s,s2,s3)

combined




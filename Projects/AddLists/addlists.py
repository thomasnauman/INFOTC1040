list1 = open("list1.txt", "r+")
list2 = open("list2.txt", "r")
list3 = open("list3.txt", "r")
list4 = open("list4.txt", "r")
result = open("result.txt","w+")

def main():
    new_list1 = []
    new_list2 = []
    new_list3 = []
    first_list = input("What is the first list you would like to add? (list1.txt, list2.txt, list3.txt, or list4.txt: ")
    if first_list == "list1.txt":
        first_list = list1
    elif first_list == "list2.txt":
        first_list = list2
    elif first_list == "list3.txt":
        first_list = list3
    elif first_list == "list4.txt":
        first_list = list4

    second_list = input("What is the second list you would like to add?(list1.txt, list2.txt, list3.txt, or list4.txt: ")
    if second_list == "list1.txt":
        second_list = list1
    elif second_list == "list2.txt":
        second_list = list2
    elif second_list == "list3.txt":
        second_list = list3
    else:
        second_list = list4

    for index in first_list:
        ind = index.replace(" ", "")
        new_list1.append(float(ind))
    print(new_list1)

    for index in second_list:
        ind = index.replace(" ", "")
        new_list2.append(float(ind))
    print(new_list2)

    i = 0
    for index in new_list1:
        total = new_list1[i] + new_list2[i]
        new_list3.append(total)
        i += 1

    for index in new_list3:
        result.write(str(index) + "\n")

    list1.close()
    list2.close()
    list3.close()
    list4.close()
    result.close()

main()
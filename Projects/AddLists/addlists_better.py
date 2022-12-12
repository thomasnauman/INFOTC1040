result = open("result.txt", "w+")


def main():
    new_list1 = []
    new_list2 = []
    new_list3 = []
    first_list = input("What is the first list you would like to add? (list1.txt, list2.txt, list3.txt, or list4.txt: ")
    first_list = open(first_list, "r+")
    second_list = input(
        "What is the second list you would like to add?(list1.txt, list2.txt, list3.txt, or list4.txt: ")
    second_list = open(second_list, "r+")

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

    first_list.close()
    second_list.close()
    result.close()


main()

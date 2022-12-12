def main():
    numbers = open("numbers.txt", "r")
    list_nums = []
    stat_dict = {}
    for number in numbers:
        list_nums.append(float(number))
    numbers.close
    stat_dict["file_name"] = "numbers.txt"
    stat_dict["sum"] = sum(list_nums)
    stat_dict["count"] = (len(list_nums))
    stat_dict["average"] = stat_dict["sum"]/stat_dict["count"]
    stat_dict["maximum"] = max(list_nums)
    stat_dict["minimum"] = min(list_nums)
    stat_dict["range"] = stat_dict["maximum"]-stat_dict["minimum"]

    selection = input("What would you like to know about the numbers? (sum, count, average, maximum, minimum, range): ")
    print(f"The {selection} of the numbers is {stat_dict[selection]}")

main()
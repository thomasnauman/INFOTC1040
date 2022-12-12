journal_dict = {}  # this is an intermediate dictionary that holds the CSV entries and sorts them into transaction types
stat_dict = {}  # this is a dictionary that holds the stat values


def parser(csv):  # this function parses the CSV and writes data to the journal_dict dictionary
    journal = open(csv, "r+")
    for transaction in journal:
        split = transaction.split(",")
        messy_amount = split[1]
        amount = messy_amount.strip("\n")
        category = split[0]
        if category not in journal_dict:
            journal_dict[category] = []
        journal_dict[category].append(amount)
    journal.close()


def find_all_costs():  # this function finds the total cost of all transactions
    total_cost = 0
    for key in journal_dict:
        for index in journal_dict[key]:
            num = round(float(index), 2)
            total_cost += num
    stat_dict["total_cost"] = total_cost


def find_num_of_purchases():  # this function finds the total number of transactions
    purchases = 0
    for key in journal_dict:
        purchases += (len(journal_dict[key]))
    stat_dict["num_of_purchases"] = round(float(purchases), 2)


def find_num_of_purchases_for_type():  # this function finds the number of purchases per transaction type
    for key in journal_dict:
        stat_dict[f"{key}_length"] = len(journal_dict[key])


def find_cost_of_purchases_for_type():  # this function finds the cost of all purchases for each transaction type
    for key in journal_dict:
        cost = 0
        for index in journal_dict[key]:
            num = float(index)
            cost += num
        stat_dict[f"{key}_cost"] = cost


def calculate_average_cost():  # this function finds the average cost of all transactions
    average_cost = stat_dict["total_cost"] / stat_dict["num_of_purchases"]
    stat_dict["average_cost"] = average_cost


def find_min_transaction_cost():  # this function finds the lowest transaction cost
    smallest = 2 ** 31 - 1
    smallest_category = None
    for key in journal_dict:
        for index in journal_dict[key]:
            if float(index) < float(smallest):
                smallest = index
                smallest_category = key
            if float(index) == float(smallest):
                smallest_category = smallest_category + ", " + str(key)
    stat_dict["smallest"] = smallest
    stat_dict["smallest_category"] = str(smallest_category)


def find_max_transaction_cost():  # this function finds the highest transaction cost
    largest = -2 ** 31 - 1
    largest_category = None
    for key in journal_dict:
        for index in journal_dict[key]:
            if float(index) > float(largest):
                largest = index
                largest_category = key
            if float(index) == float(largest):
                largest_category = largest_category + ", " + str(key)
    stat_dict["largest"] = str(largest)
    stat_dict["largest_category"] = str(largest_category)


def stat_dict_assembler():  # this function assembles the stat_dict dictionary
    find_all_costs()
    find_num_of_purchases()
    calculate_average_cost()
    find_num_of_purchases_for_type()
    find_cost_of_purchases_for_type()
    find_min_transaction_cost()
    find_max_transaction_cost()


def summary():  # this function outputs the summary statistics in a neat, readable fashion
    print(f"The total cost of all transactions is ${stat_dict['total_cost']:.2f}")
    print(f"The number of purchases is {stat_dict['num_of_purchases']}")
    print(f"The average purchase cost is ${stat_dict['average_cost']:.2f}")
    for key in journal_dict:
        print(f"There were {stat_dict[f'{key}_length']} purchases in {key}")
        print(f"${stat_dict[f'{key}_cost']:2f} was spent on {key}")
    print(f"The least expensive purchase(s): ${stat_dict['smallest']} spent on {stat_dict['smallest_category']}")
    print(f"The most expensive purchase(s): ${stat_dict['largest']} spent on {stat_dict['largest_category']}")


def dict_display():  # this function displays the two dictionaries
    print(journal_dict)
    print(stat_dict)


def main():
    want_to_continue = True
    while want_to_continue:
        csv = input("What csv file would you like to analyze?: ")
        parser(csv)
        stat_dict_assembler()
        #dict_display()
        summary()
        repeat = input("Would you like to do another calculation? (y/n): ")
        if repeat != "y":
            want_to_continue = False
            print("All done!")


main()

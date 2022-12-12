# write a file called "result.txt"

def main():
    file = open("/Users/thomasnauman/PycharmProjects/INFOTC1040/Class Notes/Files/result.txt", "w")
    # this opens a file in write mode; if the file exists, open it: if not, make it
    file.write("This file contains the results of numbers added together")
    file.close()
    # this closes the file

    file2 = open("/Users/thomasnauman/PycharmProjects/INFOTC1040/Class Notes/Files/result.txt", "a")
    file2.write("\nResult: \n")

    inputs = open("/Users/thomasnauman/PycharmProjects/INFOTC1040/Class Notes/Files/numbers2", "r+")
    for line in inputs:
        nums = line.split()
        file2.write(str(float(nums[0]) + float(nums[1])) + "\n")
    inputs.close
    file2.close

main()
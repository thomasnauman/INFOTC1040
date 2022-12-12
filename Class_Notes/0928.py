import sys

def max(ls):
    # edge case
    # when list is empty
    # if ls == []
    if len(ls) == 0:
        return 0
    else:
        max_number = -1 * (2*31-1)
        # there is never a number smaller than this, so the first value it reads will automatically be bigger
        for x in ls:
            if x > max_number:
                max_number = x
        return max_number

def main():
    numbers = [5, 7, -9, 2]
    numbers2 = []
    print(max(numbers))
    print(max(numbers2))
    print(sys.maxsize)
    print(2 ** 31 - 1)

main()

from collections import defaultdict, Counter
import sys


# This file shows different ways of counting how many times each number in
# a sequence occurs. Uncomment the version you want to run, and then run with:
#   python3 counter_demo.py < nums


def main():
    # Uncomment the version you want to run

    # Counting with regular dictionary
    num_count = {}
    for line in sys.stdin:  # Iterating over stdin gives you one line at a time
        num = int(line)
        if num not in num_count:
            num_count[num] = 1
        else:
            num_count[num] += 1

    # Counting with default dictionary
    # lambda: 0 is a function that takes in no arguments and returns zero
    #         It gets called whenever we access a key in the default dictionary
    #         that doesn't exist, and the requested key is added with the value
    #         returned by the lambda function.
    # num_count = defaultdict(lambda: 0)
    # for line in sys.stdin:
    #     num = int(line)
    #     num_count[num] += 1  # num gets added if it's not in the dict

    # Counter is essentially an adapter for defaultdict(lambda: 0) with
    # some extra features that we don't need for this.
    # num_count = Counter()
    # for line in sys.stdin:
    #     num = int(line)
    #     num_count[num] += 1

    # One-liner version using list comprehension
    # num_count = Counter([int(line) for line in sys.stdin])

    print("Num counts:", list(sorted(num_count.items())))

    # Bonus: Splitting a string every time there's a ':' character (colon)
    spam = '42: 1234: cout << "WAAAA";'
    parts = spam.split(':')  # Split at :
    print("Line split at colon:", parts)
    count = int(parts[0])
    line_num = int(parts[1])
    print("Line num:", line_num)
    print("Count:", count)


if __name__ == "__main__":
    main()

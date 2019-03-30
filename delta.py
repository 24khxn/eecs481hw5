import os
import subprocess
import sys

if len(sys.argv) != 3:
    exit(1)

set_size = int(sys.argv[1]) # n, size of set to be minimized
interesting_check = sys.argv[2] # command to check if set is interesting

def main():
    set_range = list(range(set_size))

    min_set = minimize(set(), set_range)
    return min_set.sort()

def minimize(min_set, set_range):

    # base case
    if len(set_range) == 1:
        return set_range

    p1, p2 = split_list(set_range)

    if is_interesting(min_set.union(p1)):
        return minimize(min_set, p1)
    if is_interesting(min_set.union(p2)):
        return minimize(min_set, p2)

    return minimize(min_set.union(p2), p1).union(minimize(min_set.union(p1), p2))

def split_list(set_range):
    half = len(set_range)//2
    return set_range[:half], set_range[half:]

def is_interesting(split_set):
    return 1;

if __name__ == "__main__":
    main()

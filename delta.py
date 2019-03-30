import os
import subprocess
import sys

if len(sys.argv) != 3:
    exit(1)

set_size = int(sys.argv[1])  # n, size of set to be minimized
interesting_check = sys.argv[2]  # command to check if set is interesting


def main():
    set_range = list(range(set_size))  # range of changes {c_1, c_2, ..., c_n}

    p = minimize(set(), set_range)
    return list(p).sort()

# delta debugging algorithm, see slides for pseudocode


def minimize(p, set_range):

    # base case
    if len(set_range) == 1:
        return set_range

    p1, p2 = split(set_range)

    if is_interesting(p.union(p1)):
        return minimize(p, p1)
    if is_interesting(p.union(p2)):
        return minimize(p, p2)

    return set().union(minimize(p.union(p2), p1), minimize(p.union(p1), p2))


def split(set_range):
    half = len(set_range)//2
    return set_range[:half], set_range[half:]


def is_interesting(split_set):
    command = '\"'
    command += interesting_check
    command += '\"'
    for number in split_set:
        command += ' {}'.format(number)

    return subprocess.call(command, shell=True)


if __name__ == "__main__":
    main()

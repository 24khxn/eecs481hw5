import os
import subprocess
import sys

if len(sys.argv) != 3:
    exit(1)

set_size = int(sys.argv[1])  # n, size of set to be minimized
interesting_check = sys.argv[2]  # command to check if set is interesting


def main():
    changes = list(range(set_size))  # set of changes {c_1, c_2, ..., c_n}

    p = minimize(set(), changes)
    return list(p).sort()


# delta debugging algorithm, see slides for pseudocode
def minimize(p, changes):

    # base case
    if len(changes) == 1:
        return changes

    p1, p2 = split(changes)

    if is_interesting(p.union(p1)):
        return minimize(p, p1)
    if is_interesting(p.union(p2)):
        return minimize(p, p2)

    return set().union(minimize(p.union(p2), p1), minimize(p.union(p1), p2))


def split(changes):
    half = len(changes)//2
    return changes[:half], changes[half:]


def is_interesting(split_set):
    command = '\"'
    command += interesting_check
    command += '\"'
    for number in split_set:
        command += ' {}'.format(number)

    return subprocess.call(command, shell=True)


if __name__ == "__main__":
    main()

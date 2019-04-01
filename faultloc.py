import sys
from collections import defaultdict
import math
import operator

"""
NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE
osha(s) = failed(s) / sqrt(total_failed * (failed(s) + passed(s) ) )
failed(s) = number of failing files which covered line 's' at least once
passed(s) = number of passing files which covered line 's' at least once
total_failed = number of test files which caused the program to fail
"""

HASHTAG_C = '#####'
DASH_C = '-'
PASS_C = 'pass'
FAIL_C = 'fail'
GCOV_FILENAMES_C = sys.argv[1:]


def get_rel_data(line):
    return line.split(':')[0].split(' ')[-1], int(line.split(':')[1].split(' ')[-1])


def not_number(num):
    return num == HASHTAG_C or num == DASH_C


if __name__ == '__main__':
    passed_counter = defaultdict(int)
    failed_counter = defaultdict(int)
    line_nums = []
    num_failed_files = 0

    for fname in GCOV_FILENAMES_C:
        file = open(fname, 'r')
        lines = file.read().split('\n')
        file.close()

        if FAIL_C in fname:
            num_failed_files += 1

        for line in lines:
            if not line:
                continue

            num_visits, line_num = get_rel_data(line)

            if not_number(num_visits):
                continue
            # else:
            #     line_num.append()

            # num_visits = int(num_visits)
            if line_num not in line_nums:
                line_nums.append(line_num)

            if PASS_C in fname:
                passed_counter[line_num] += 1
            elif FAIL_C in fname:
                failed_counter[line_num] += 1


# osha(s) = failed(s) / sqrt(total_failed * (failed(s) + passed(s) ) )
    oshas = {}
    for line in line_nums:

        osha = failed_counter[line] / math.sqrt(
            num_failed_files * (
                failed_counter[line] + passed_counter[line]))

        # print("""
        # num_failed: {}\n
        # num_passed: {}\n
        # osha:       {}
        # """.format(
        #     failed_counter[line],
        #     passed_counter[line],
        #     osha
        # ))

        oshas[line] = osha

    # print('total failed files: {}'.format(num_failed_files))

    sorted_by_keys = sorted(
        oshas.items(), key=operator.itemgetter(0), reverse=False)

    sorted_oshas = sorted(
        sorted_by_keys, key=operator.itemgetter(1), reverse=True)

    print(sorted_oshas[:100])

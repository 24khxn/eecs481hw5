#!/bin/bash

rm libpng-1.6.34/*.gcov 2> /dev/null
rm libpng-1.6.34/*.gcda 2> /dev/null 
rm *.gcov 2> /dev/null 

ALL_TEST_NAMES=""
for i in $*
do
    ALL_TEST_NAMES+="./large-png-suite/"
    ALL_TEST_NAMES+="$i.png"
    ALL_TEST_NAMES+=" "
done

./libpng-1.6.34/pngtest -m $ALL_TEST_NAMES > /dev/null 2> /dev/null
gcov libpng-1.6.34/*.c 2> /dev/null | grep "Lines executed:" > all_percentages.output
PERCENT_COVERAGE=$(python parse_gcov.py)
INT_PERCENT_COVERAGE=$(echo $PERCENT_COVERAGE | tr -dc '0-9')
echo "percent coverage: $PERCENT_COVERAGE"

if [ $INT_PERCENT_COVERAGE -lt 3588 ]
then
	exit 0
fi 
exit 1
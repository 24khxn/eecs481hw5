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

echo "$ALL_TEST_NAMES"

./libpng-1.6.34/pngtest -m $ALL_TEST_NAMES > /dev/null 2> /dev/null 

TEST_RESULT=$(gcov libpng-1.6/*.c 2> /dev/null)
echo "test result: $TEST_RESULT"



#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fetchItemsToDisplay' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. 2D_STRING_ARRAY items
#  2. INTEGER sortParameter
#  3. INTEGER sortOrder
#  4. INTEGER itemsPerPage
#  5. INTEGER pageNumber
#

def fetchItemsToDisplay(items, sortParameter, sortOrder, itemsPerPage, pageNumber):
    items.sort(key=lambda x: x[sortParameter], reverse=sortOrder)
    
    k = itemsPerPage
    i = pageNumber * itemsPerPage
    j = i + k

    return [x[0] for x in items[i:j]]

if __name__ == '__main__':
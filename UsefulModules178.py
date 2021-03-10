# List in Python are dynamic - but takes less memory and runs faster

import datetime
from array import array
print(datetime.time(5, 42, 2))
print(datetime.time())
print(datetime.date.today())

arr = array('i', [1, 2, 3])
print(arr)

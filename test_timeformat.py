#!/usr/bin/env python

from timeformat import timeformat


print(timeformat('1216')) # prints '12:16 AM'
print(timeformat('110')) # prints '1:10 AM'

print(timeformat('1216p')) # prints '12:16 PM'
print(timeformat('110p')) # prints '1:10 PM'

print(timeformat('garbage')) # prints None. The input does not match regex.


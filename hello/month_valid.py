# -----------
# User Instructions
#
# Modify the valid_month() function to verify
# whether the data a user enters is a valid
# month. If the passed in parameter 'month'
# is not a valid month, return None.
# If 'month' is a valid month, then return
# the name of the month with the first letter
# capitalized.
#
from __future__ import print_function
import string

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

month_abbvs = [m[:3] for m in months]

def valid_month(month):
    """
    Simply use https://docs.python.org/2/library/string.html#string.capitalize
    """
    caped_month = string.capitalize(month)
    return caped_month if caped_month in months+month_abbvs else None

print(valid_month("january")) # => "January"
print(valid_month("January")) # => "January"
print(valid_month("foo"))        # => None
print(valid_month("")) # => None
print(valid_month("Jan")) # => "Jan"
print(valid_month("Dec")) # => "Dec"
print(valid_month("Dec")) # => "dec"

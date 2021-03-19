# Program that use dateutil
from dateutil import parser

# Read a string and convert in date type
parsed_date = parser.parse('3rd January 2014')

# Display the type of date
print('The type of the parsed date is {}'.format(type(parsed_date)))
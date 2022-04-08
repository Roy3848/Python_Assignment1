# Calculate the date 7 month from any date, take the date as an input from the user

import datetime
from dateutil.relativedelta import *

date = datetime.datetime.now()  # function to get the current date and time
print(date)

# relative_delta function to be applied to an existing datetime
# and can replace specific components of that datetime,
# like here we have modified the months
date2 = date + relativedelta(months=+7)
print(date2)


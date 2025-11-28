"""
Sample program for time measurement

We save the start time and the end time, then we take the 
difference.
"""

import datetime as dt

start_time = dt.datetime.now()

answer = input("What is the answer to the question? ")

end_time = dt.datetime.now()

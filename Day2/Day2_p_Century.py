# Statement

# Given a year (as a positive integer), 
# find the respective number of the century. Note that, for example, 
# 20th century began with the year 1901. 
C=int(input())
import math
print(math.ceil(C/100))
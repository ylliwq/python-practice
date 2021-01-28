# Given a month - an integer from 1 to 12, print the number of days in it in the year 2017.
m=int(input())
if m in[1,3,5,7,8,10,12]:
  print(31)
elif m in[4,6,9,11]:
  print(30)
else:
  print(28)

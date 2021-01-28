# Given an integer, print "YES" if it's a three-digit number and print "NO" otherwise.
n=int(input())
if 99<n<1000:
  print("YES")
else:
  print("NO")
# another way
n=input()
if len(n)==3:
  print("Yes")
else:
  print("NO")
# Given two non-zero integers, print "YES" if exactly one of them is positive and print "NO" otherwise.
a=int(input())
b=int(input())
if a*b<0:
  print("YES")
else:
  print("NO")
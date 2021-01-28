# Given a three-digit integer X consisting of three different digits, print "YES" 
# if its three digits are going in an ascending order from left to right and print "NO" otherwise.

X=int(input())
if int(X/100)<int(X%100/10)<int(X%10):
  print("YES")
else:
  print("No")
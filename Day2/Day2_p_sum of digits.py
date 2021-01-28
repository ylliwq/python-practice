# Given a three-digit number. Find the sum of its digits.
N=int(input())
print(N//100+N%100//10+N%10)
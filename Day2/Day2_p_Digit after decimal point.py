# Given a positive real number, print its first digit to the right of the decimal point.
N=float(input())
print(int(N*10%10))
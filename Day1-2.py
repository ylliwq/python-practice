# input輸入的值會被儲存成字串 input()內容可以填入相關的提示
a=int(input('a='))
b=int(input('b='))
print(a+b)
# , can be used to seperate different strings and values in print function
print ("a+b =",a+b)

apple=int(input("please input how many apples?"))
student=int(input("please input how many students?"))
print("Each student can get",apple//student,", and basket remained",apple%student)

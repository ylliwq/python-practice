First_name = input('Please enter your first name')
Last_name = input ('Please enter your last name')
#output = f'Hello, {First_name} {Last_name}'
output = 'Hello, {} {} ' .format(First_name.capitalize(),Last_name.capitalize())
print(output) 


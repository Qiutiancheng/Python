# The in keyword is used to check if a value is present in a sequence (list, range, string etc.).

# album = ['马冬梅']
# album.append('马什么梅')
# print('马冬梅' in album) # True

# It tests if two variables point the same object, not if two variables have the same value.

# a1 = '马冬梅'
# a2 = '马冬梅'
# print(a1 is a2) # True



# if...else... or if...elif...else, It's the same as Javascript
# input : The input() function allows user input

# password_list=['*****','12345']
# def account_login():
#     password = input('Password:')
#     password_reset = password == password_list[0]
#     password_correct = password == password_list[-1]
#     if password_correct:
#         print('login success!')
#     elif password_reset:
#         new_password = input('please enter a new password:')
#         password_list.append(new_password)
#         print('Your password has changed successfully!')
#         account_login()    
#     else:
#         print('Wrong pass word or invalid input!')
#         account_login()
# account_login()



# loop: A for loop is used for iterating over a sequence.
# range: 在range函数后的括号内填上数字，就可以获得一个范围。

# for x in range(1,11):
#     print(str(x)+'+1=',x+1)
for x in range(1,10):
    for o in range(1,10):
        print('{}X{}={}'.format(x,o,x*o))

# while
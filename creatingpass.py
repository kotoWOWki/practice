import random

create_pass = True
create_login = True
sign_in = False
attempts = 2

while create_pass:
    user_pass = input("Create New Password(For create a random password please type RANDOM): ")
    length_p = len(user_pass)
    if length_p == 0:
        print("Password wasn't created, please try again")
    elif length_p <= 7:
        print("Password is too Short, please try again")  
    elif length_p >= 8:
        print(" Password Successfully Created")
        create_pass = False
        break

while create_login:
    user_login = input("Please create new Login: ")
    length_l = len(user_login)
    if length_l == 0:
        print("Login wasn't created, please try again")
    elif length_l <= 4:
        print("Login must include more than 4 symbols, please try again")  
    elif length_l >= 5:
        print(" Login Successfully Created")
        create_login = False
        sign_in = True
        break
        
while sign_in:
    correct_log = input("Please type your login: ")
    correct_pass = input("Please type your password: ")
    if attempts == 0:
        print("Account was Frozen!")
        break   
    elif correct_log != user_login or correct_pass != user_pass:
        print("Login or Password is incorrect, please try again")
        print("Attempts:", attempts)
        attempts -= 1
    else:
        print("Access Granted!")
        break   
                
          
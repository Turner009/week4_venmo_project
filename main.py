user_one = {
    'full_name':'Bugs Bunny',
    'username': 'HareJordan',
    'password': 'bugs1',
    'account_balance': 250.00,
    'connected_banks': [('bank one', 0),('bank two', 0)]
}
user_two = {
    'full_name':'Elmer Fudd',
    'username': 'Besthunter',
    'password': 'elmer1',
    'account_balance': 50.00,
    'connected_banks': [('bank one', 0),('bank two', 0)]
}

login = ''
password = ''

while login != user_one['username'] or user_two['username']:
    login = input('Enter your username please.')
    if login == user_one['username']:
        print(f"Welcome {user_one['full_name']}")
        password = input('Please enter your password. ')
        while password != user_one['password']:
            print("Incorrect password")
            password = input('Please enter your password. ')
            if password == user_one['password']:
                print("")
                print(f"Successful login your current balance is {user_one['account_balance']}.")   
        break
    elif login == user_two['username']:
        print("")
        print(f"Welcome {user_two['full_name']}")
        print("")       
        password = input('Please enter your password. ')
        while password != user_two['password']:
            print("Incorrect password")
            password = input('Please enter your password. ')
            if password == user_two['password']:
                print("")
                print(f"Successful login your current balance is {user_two['account_balance']}.") 
        break
    else:
        print("")
        print("Invalid Username")

# print(user_two['connected_banks'][0][0])

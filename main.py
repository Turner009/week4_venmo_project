user_one = {
    'full_name':'Bugs Bunny',
    'username': 'HareJordan',
    'password': 'bugs1',
    'account_balance': 250.00,
    'connected_banks': [('MCU', 1500.00),('Acme Savings Club', 2000.00)]
}
user_two = {
    'full_name':'Elmer Fudd',
    'username': 'Besthunter',
    'password': 'elmer1',
    'account_balance': 50.00,
    'connected_banks': [('Chase', 1000.00),('Acme Savings Club', 2500.00)]
}

login = ''
password = ''
logged_in_user =''
other_user = ''




while login != user_one['username'] or user_two['username']:
    login = input('Enter your username please.')
    if login == user_one['username']:
        logged_in_user = user_one
        other_user = user_two
        break
    elif login == user_two['username']:
        logged_in_user = user_two
        other_user = user_one
        break
    else:
        print("")
        print("Invalid username")  

print (f"Welcome {logged_in_user['full_name']}")
while password != logged_in_user['password']:
    password = input('Please enter your password. ')
    if password == logged_in_user['password']:
        print("")
        print(f"Successful login your current balance is {logged_in_user['account_balance']}.")    
        print(f"Your available connected accounts funds are:")
        for bank, balance in logged_in_user['connected_banks']:
            print(bank, balance)
        break     
    else:
        print("Incorrect password")

tranfer = input(f"Would you like to make a transfer to {other_user['full_name']}? (Y or N) ")

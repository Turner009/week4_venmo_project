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
logged_in_user =''
other_user = ''

def password_confirm(user):
    password = ''
    while password != user['password']:
        password = input('Please enter your password. ')
        if password == user['password']:
            print("")
            print(f"Successful login your current balance is {user['account_balance']}.")    
            print(f"Your available connected accounts funds are:")
            balance_check(user)
            break     
        else:
            print("Incorrect password")

def balance_check(user):
    for bank, balance in user['connected_banks']:
            print(bank, balance)

def transfer_function(user):
    transfer = input(f"Would you like to make a transfer to {other_user['full_name']}? (Y or N) ")
    if transfer == "N":
        print(f"Have a nice day {user['full_name']} good bye.")
    elif transfer == "Y":
        transfer_amount = float(input("How much would you like to tranfer?"))
        while transfer_amount > user['account_balance']:
            print("")
            print("There are not enough funds for that amount.")
            transfer_amount = float(input("Please input new amount."))
        user['account_balance'] -= transfer_amount
        other_user['account_balance'] += transfer_amount
        print(f"Transfer complete your updated balance is {user['account_balance']}")


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

password_confirm(logged_in_user)

transfer_function(logged_in_user)

repeat_transfer = input(f"Would you like to make another transfer to {other_user['full_name']} (Y or N)")
if repeat_transfer == "Y":
    transfer_amount = float(input("How much would you like to tranfer?"))
    while transfer_amount > logged_in_user['account_balance']:
        print("")
        print("There are not enough funds for that amount.")
        transfer_amount = float(input("Please input new amount."))
    logged_in_user['account_balance'] -= transfer_amount
    other_user['account_balance'] += transfer_amount
    print(f"Transfer complete your updated balance is {logged_in_user['account_balance']}") 

elif repeat_transfer == "N":
    print(f"Your balance is {logged_in_user['account_balance']}. Have a nice day.")






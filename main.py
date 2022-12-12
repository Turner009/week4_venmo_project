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
            print(f"{bank}: {balance}")

def funds_from_bank(user):
    select_bank = int(input(f"You can transfer funds from a bank account to complete transaction, which bank would you like to use? 0 for {(user['connected_banks'][0][0])} OR 1 for {(user['connected_banks'][1][0])}  "))
    withdrawal = float(input("How much would you like to withdraw?"))
    list_bank = list(user['connected_banks'][select_bank])
    user['account_balance'] += withdrawal ; list_bank[1] -= withdrawal
    list_bank = tuple(list_bank)
    user['connected_banks'][select_bank] = list_bank

    print(f"Your new balance is {user['account_balance']}")
    print(f"Your updated balance is {user['connected_banks'][select_bank][0]} {user['connected_banks'][select_bank][1]}")




def transfer_function(user):
    transfer = input(f"Would you like to make a transfer to {other_user['full_name']}? (Y or N) ")
    if transfer == "N":
        print(f"Have a nice day {user['full_name']} good bye.")
    elif transfer == "Y":
        transfer_amount = float(input("How much would you like to tranfer?"))
        while transfer_amount > user['account_balance']:
            print("")
            print("There are not enough funds for that amount.")
            funds_from_bank(logged_in_user)
            transfer_amount = float(input(f"Please input new amount to transfer to {other_user['full_name']}."))
        user['account_balance'] -= transfer_amount
        other_user['account_balance'] += transfer_amount
        print(f"Transfer complete your updated balance is {user['account_balance']}")
        repeat_transfer = input(f"Would you like to make another transfer to {other_user['full_name']} (Y or N)")
        if repeat_transfer == "Y":
            transfer_amount = float(input("How much would you like to tranfer?"))
            while transfer_amount > logged_in_user['account_balance']:
                print("")
                print("There are not enough funds for that amount.")
                funds_from_bank(logged_in_user)
                transfer_amount = float(input(f"Please input new amount to transfer to {other_user['full_name']}."))
            logged_in_user['account_balance'] -= transfer_amount
            other_user['account_balance'] += transfer_amount
            print(f"Transfer complete your updated balance is {logged_in_user['account_balance']}") 
        elif repeat_transfer == "N":
            print(f"Your balance is {logged_in_user['account_balance']}. Have a nice day.")



def login_function():
    login = ''
    while login != user_one['username'] or user_two['username']:
        login = input('Enter your username please.')
        global logged_in_user
        global other_user
        
        if login == user_one['username']:
            logged_in_user = user_one
            other_user = user_two
            print (f"Welcome {logged_in_user['full_name']}")
            break
        elif login == user_two['username']:
            logged_in_user = user_two
            other_user = user_one
            print (f"Welcome {logged_in_user['full_name']}")
            break
        else:
            print("")
            print("Invalid username")

    

login_function()

password_confirm(logged_in_user)

transfer_function(logged_in_user)








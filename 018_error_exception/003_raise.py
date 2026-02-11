def withdraw_money(balance, amount):
    if amount < 0:
        raise ValueError("Cannot withdraw negetive value")
    
    if amount > balance:
        raise Exception("account e porjapto balance nai")
    
    balance -= amount
    print(amount)
    return balance
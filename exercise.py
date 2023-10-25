current_amount = 5000
min_amount = 10
max_amount = 1000

while True:
    amount_from_ATM = input("Do you want money from ATM (yes/no): ")

    if amount_from_ATM == "no":
        print("Thank you for using our ATM")
        break

    if amount_from_ATM == "yes":
        amount_to_withdraw = int(input("Enter the amount to withdraw: "))

        if amount_to_withdraw < min_amount:
            print("Amount to withdraw is less than the minimum amount.")
        elif amount_to_withdraw > max_amount:
            print("Amount to withdraw is more than the maximum amount.")
        elif amount_to_withdraw > current_amount:
            print("Amount to withdraw is more than the current amount.")
        else:
            current_amount -= amount_to_withdraw
            print("Withdrawal successful. Remaining balance:", current_amount)

    another_transaction = input("Do you want another transaction? (yes/no): ")

    if another_transaction == "no":
        print("Thank you for using our ATM")
        break


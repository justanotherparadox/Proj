
#my_first_git_commit
#Assignment No.- Module 1 Assignment-20
'''Multi-line
   comment and not commit'''
account_number=int(input("Enter account number"))
account_balance=int(input("Enter your account balance"))
salary=int(input("Enter your salary"))
loan_type=input("Enter your loan type")
loan_amount_expected=int(input("Enter requested loan"))
customer_emi_expected=int(input("Enter expected emi"))
if (account_number<1000 and account_number>1999 and account_balance<100000):
    print("Enter correct account number")
    print("You should have a minimum account balance of 100000 INR")
else:
    if (salary>25000 and loan_type=="car"):
        if (loan_amount_expected<=500000 and customer_emi_expected<=36):
            print("Your account number is:", account_number)
            print("You requested an amount equivalent to:", loan_amount_expected)
            print("Eligible loan amount is equivalent to:", 500000)
            print("Your requested EMI:", customer_emi_expected)
            print("Number of EMI's required to repay:", 36)
        else:
            print("Not eligible")
    elif (salary>50000 and loan_type=="House"):
        if (loan_amount_expected<=6000000 and customer_emi_expected<=60):
            print("Your account number is:", account_number)
            print("You requested an amount equivalent to:", loan_amount_expected)
            print("Eligible loan amount is equivalent to:", 6000000)
            print("Your requested EMI:", customer_emi_expected)
            print("Number of EMI's required to repay:", 60)
        else:
            print("Not eligible")
    elif (salary>75000 and loan_type=="Business"):
        if (loan_amount_expected<=7500000 and customer_emi_expected<=84):
            print("Your account number is:", account_number)
            print("You requested an amount equivalent to:", loan_amount_expected)
            print("Eligible loan amount is equivalent to:", 7500000)
            print("Your requested EMI:", customer_emi_expected)
            print("Number of EMI's required to repay:", 84)
        else:
            print("Not eligible")
    else:
        print("Not eligible")

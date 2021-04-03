# write your code here
import argparse
import math

parser = argparse.ArgumentParser(description="Loan calculator")

parser.add_argument("--type", choices=["annuity", "diff"],
                    help="type of payment")
parser.add_argument("--payment", type=int, help="monthly payment amount")
parser.add_argument("--principal", type = int)
parser.add_argument("--periods", type = int, help = "number of months needed to repay the loan")
parser.add_argument("--interest", type = float)  # must have
                               
args = parser.parse_args()



# print(args)

if (not args.type) or ((args.type == "diff") and (args.payment)) or (not args.interest) or ( not(args.periods == None) and args.periods < 0):
    print("Incorrect parameters")
elif args.type == "annuity": 
    p = args.principal
    n = args.periods
    i = args.interest / (12 * 100)
	
    if args.periods == None: # for number of monthly payments
        # print('for number of monthly payments')
        loan_principal = args.principal
        monthly_payment = args.payment
        loan_interest = args.interest
        i = loan_interest / (12 * 100)
        n = math.ceil(math.log(monthly_payment / (monthly_payment - i * loan_principal), 1 + i) )
    
        # convert n to year, month
        years = n // 12
        months = n % 12
        if years == 0:
            years_str = ''
        elif years == 1:
            years_str = '1 year'
        else:
            years_str = str(years) + ' years'
        if months > 0:
            months_str = ' and '+str(months)+ (' month ' if months % 10 == 1 else ' months ')
        else:
            months_str = ''
        print(f'It will take {years_str} {months_str}to repay the loan')
        print('Overpayment', monthly_payment * n - loan_principal)
    elif args.payment == None:  # annuity monthly payment amount
        # print('annuity monthly payment amount')
        p = args.principal
        n = args.periods        
        loan_interest = args.interest
        i = loan_interest / (12 * 100)
        monthly_payment = math.ceil(p * (i * pow((1 + i), n)) / (pow((1 + i), n) -1))
        last_payment = (p + p * i * n ) % n
        print('Your monthly payment =', monthly_payment)  # , 'and the last payment =' if last_payment > 0 else '', last_payment if last_payment > 0 else '')
        # print('Overpayment1', p * i * n)
        print('Overpayment', monthly_payment * n - p)
    elif args.principal == None:  # for loan principal
        # print('for loan principal')
        a = args.payment
        n = args.periods        
        loan_interest = args.interest
        i = loan_interest / (12 * 100)
        p = int(a / ((i * pow(1 + i, n)) / (pow(1 + i, n) - 1)))
    
        print(f'Your loan principal = {p}')
elif args.type == "diff": 
    p = args.principal
    n = args.periods
    i = args.interest / (12 * 100)

    if args.payment == None:
        sum_payments = 0
        for m in range(n):
            d = math.ceil(p / n + i * (p - (p * m ) / n))
            print(f'Month {m+1}: payment is {d}')
            sum_payments += d
    print()
    print('Overpayment = ', sum_payments - p)
else:
    print('Invalid args.type')

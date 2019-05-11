# This project calculates loans.
# Description: Programming Project 2


def loan_amount():
    initial_loan = float(input("Please provide the requested loan amount: $"))
    while initial_loan < 500:
        print("We're sorry, but we do not finance loans under $500.\n")
        initial_loan = float(input("Please provide the requested loan amount: $"))
    return initial_loan 
    
def number_payments(initial_loan):
    number_payment = int(input("Please enter how many payments you would like to make on this loan: "))
    while number_payment < 6 or number_payment > 48:
        print("We're sorry, but the minimum amount of payemnts is 6 months.\n")
        number_payment = int(input("Please enter how many payments you would like to make on this loan: "))
    return number_payment 
    
def interest_rates(initial_loan, number_payment):
    if 500 <= initial_loan or initial_loan <= 2500:
        if 6 <= number_payment or number_payment <= 12:
            interest_rate = 0.08
        elif 13 <= number_payment or number_payment <= 36:
            interest_rate = 0.10
        else:
            interest_rate = 0.12
    elif 2501 <= initial_loan or initial_loan <= 10000:
        if 6 <= number_payment or number_payment <= 12:
            interest_rate = 0.07
        elif 13 <= number_payment or number_payment <= 36:
            interest_rate = 0.08
        else:
            interest_rate = 0.06
    elif initial_loan >= 10001:
        if 6 <= number_payment or number_payment <= 12:
            interest_rate = 0.05
        elif 13 <= number_payment or number_payment <= 36:
            interest_rate = 0.06
        else:
            interest_rate = 0.07
    return interest_rate 
    
def main():
    loanAmount = loan_amount()
    numofPayments = number_payments(loanAmount)
    interestRate = interest_rates(loanAmount, numofPayments)

    monthly = (loanAmount * interestRate * (1 + interestRate) * numofPayments / ((1 + interestRate) * numofPayments - 1))
    
    print("Loan Amount: $%4.2f , Number of Payments: %3d , Interest Rate: %3.2f , Monthly Payment of: $%3.2f " % (loanAmount, numofPayments, interestRate, monthly))

main()
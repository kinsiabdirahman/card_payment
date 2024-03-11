
# import pandas as pd
import calendar

# Function to calculate the final account balance
def solution(A, D):
    # Initializing account balance at the beginning of the year to zero
    acc_balance = 0
    # Creating a dictionary to track monthly expenses
    monthly_expenses = {month: {'total': 0, 'count': 0} for month in range(1, 13)}

    # Split the dates and amounts
    for date, amount in zip(D, A):
        # Check for the month by splitting the date
        # Get month and then convert to an integer for finding mon
        month = int(date.split('-')[1])
        # Update the account balance with the transaction amount
        acc_balance += amount
        # Update monthly expenses if the transaction is a card payment
        if amount < 0:
            monthly_expenses[month]['total'] += amount
            monthly_expenses[month]['count'] += 1

    return acc_balance

# TEST CASE:
print(solution([100, 100, 100, -10], ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"]))
                # Check if the total card payments are less than -100 for any month
    # for month, expenses_info in monthly_expenses.items():
    #     total_expenses = expenses_info['total']
    #     payments_count = expenses_info['count']

        
        # if total_expenses < -100 and payments_count < 3:
            # Subtract the 5 fee for each month with total card payments less than -100
            # acc_balance -= 5



    # Check if the total card payments are less than -100 for any month
    # for month, expenses_info in monthly_expenses.items():
    #     total_expenses = expenses_info['total']
    #     payments_count = expenses_info['count']

    #     if total_expenses < -100 and payments_count < 3:
            # Subtract the 5 fee for each month with total card payments less than -100
            # acc_balance -= 5

    # return acc_balance






            # def solution(A, D):

    #initializing account balance at the beginning of the year to zero
    # acc_balance = 0

    # #check if mount is card payment or incoming transfer
    # for amount in A:
    #     if amount < 0:
    #         #update the account balance with the fee 
    #         #by summing upp all the values in the array + the fee amount
    #         #then update the account balance1
    #         acc_balance += sum(A) +( 5 * 12)
    #     else:
    #         #else maintain the account balance as the total amount 
    #         acc_balance += sum(A)


    # pass





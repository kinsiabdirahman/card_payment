# import pandas as pd
import calendar
def solution(A, D):

  #initializing account balance at the beginning of the year to zero
    acc_balance = 0
    #creating a dict to     
    monthly_expenses = {month: 0 for month in range(1, 13)}

    # Split the dates and amounts
    for date, amount in zip(D, A):
        #check for the month by splitting 
        #get month and then convert to in so that month is identified
        month = int(date.split('-')[1])
        acc_balance += amount
        #update the account balance with the fee 
            #by summing upp all the values in the array + the fee amount
            #then update the account balance1
        if amount < 0:
            monthly_expenses[month] += amount

        # Check if the amount is less than 100 
    for month, total_expenses in monthly_expenses.items():
        if total_expenses < -100:  
            #subtract the 5
            acc_balance -= 5  

    return acc_balance

# TEST CASE:
print(solution([100, 100, 100, -10], ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"]))



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





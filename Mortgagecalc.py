#! /usr/bin/env python3

# Calculating a mortgage loan with monthly compound interest
# By C. Calongne, 01/14/2019
# Pseudocode & Python with Strings, M3Lab2_student.py
# Write the statements requested in Steps 1-7 below
# 
# See the examples in the provided code
# Use structured programming and indent your code.
# Programmer Name: Jack Fischer CSC1019 

print()
print("Welcome to the Mortgage Loan Calculator.")
print("****************************************")

# ****Instructions****
# Complete Steps 1-7 in the comments below. The remaining comments explain the logic.
# Customers can check a variety of loans and interest rates. When finished, type quit

# Step 1: add an input statement to enter name or type quit to exit

print("------\nType quit to leave the program\n------")
#name=(input("What is your name? "))
name=()



# Step 2: add a while loop to keep asking for a name until the user types quit
while name != "quit":
    name=(input("What is your name? "))
    if name == "quit":
        print("Thank you for using the Mortgage Loan Calculator.")
        quit()

    # Step 3: declare two variables for loan and interest, like months below, 
    # convert them to float, and ask the user to input their values to the screen. 
    try:
        loan=float(input("What is the total price of your loan? "))
        interest=float(input("What is the interest rate of your loan? "))
        months=float(input("How many months will it take to repay your loan? "))
    except ValueError:
        print("Please enter a valid float. For example, 5.5, 0.25, or -103.34")
        continue

    print("***************************************************************")
    print (name, "you requested an estimate on a loan for {0:.2f}" .format(loan))

    # Step 4: add a print statement to display the interest and # of months
    print("Let's calculate your interest rate of",interest,"over the course of",months,"months")
    
    print("*******************************************************************************")
    print("Here are the rates for simple interest, compound interest, and monthly interest", "\n") 

    # calculate the rate for one month's interest + payment by adding 1 to a month's interest
    interest_rate = float((interest/12)+1)

    # calculate the compound interest per payment period by raising the  
    # monthly payment to the negative power of total months
    compound_interest = float(1-((interest/12)+1) ** -months)

    # Step 5: print the interest_rate and compound_interest to the display screen

    print("Simple interest",interest_rate, "\n")
    print("Compound",compound_interest, "\n")


    # calculate the monthly interest based on the compound interest
    monthly_interest = float((interest/12)/ compound_interest)
    print("Monthly",monthly_interest, "\n")

    # calculate the monthly loan payment with monthly compound interest
    payments = float(loan * monthly_interest)


    # Step 6: write a print statement that displays the monthly payments to two decimal points
    # Tip: use the 0:.2f format from an earlier example, only for the payments
    #monpay=(interest/12)*(1/(1-(1+interest/12)**(-months)))*loan 
    #print("Your monthly payments are, {0:.2f}", monpay)
    print("Your monthly payments are, {0:.2f}" .format(payments))
    

    print("*******************************************")
    # Step 7: add an input statement to enter name or type quit to exit


print()
print("Thank you for using the Mortgage Loan Calculator")
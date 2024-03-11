import math 

'''
Create a program that allows the user to: 

1. Calculate their interest on an investment (simple and compound)
 or 

2.Calculate the amount that should be paid on a home loan
 each month.

'''
print("-"*90)
print("\nFinance Calculator\n")
print("-"*90)

print("To calculate the amount of interest you'll earn on your investment enter 'Investment'")
print("\nTo calculate the amount you'll pay on a home loan enter 'Bond'\n")
print("-"*90)
# Created a variable called 'service' for user to input 'Investment' or 'Bond'

service = input("\nPlease enter 'Investment' or 'Bond' : ")

# if user enters 'investment' ask user to input following:

    # how much they are depositing,
    # at what interest rate (%),
    # the number of years they plan on investing 
    # 'Simple' or 'Compound' interest

    # .lower() is used  to make sure all str user inputs aren't case sensitive

if service.lower() == "investment" :
    deposit_amount = int(input("\nEnter the amount you're depositing: "))
    user_interest = int(input("\nEnter interest rate (%) : "))
    years_interest = int(input("\nEnter number of years you plan on investing : "))
    interest = input("\nPlease enter 'Simple' or 'Compound' interest: ")   
     
    # Simple interest formula:

    P = deposit_amount
    r = user_interest/100
    t = years_interest

    A = P*(1+r*t)
    simple = A
    
    # Compound interest formula:

    A = P*math.pow((1+r),t)

    compound = A

# Total amount once interest has been applied is calculated and printed for
#        simple and compound interest.

    if interest.lower() == 'simple' :
          print("\nTotal amount once interest has been applied: ", simple )
    elif interest.lower() == 'compound' :
          print("\nTotal amount once interest has been applied : ", compound)
    else: print ("\nPlease try again.")

# Bond repayment user input:

elif service.lower() == "bond" :
    house_value = int(input("\nEnter present value of house : "))
    user_interest = int(input("\nEnter interest rate (%) : "))
    months_interest = int(input("\nEnter number of months you plan take to repay : "))    
   
# Bond repayment formula:

    P = house_value      #Present house value
    i = (user_interest/100)/12  #Monthly interest rate
    n = months_interest    #Number of months to repay
    
    repayment = (i*P)/(1-(1+i)**(-n))

# Bond repayment calculated and printed:

    print("\nYour repayment will be: ", repayment)

else: 
    print("\nError: We didn't understand your request. Please try again.")



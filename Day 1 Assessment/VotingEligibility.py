def furtherSteps():
    toPrint = '''
Next steps:-
    step 1: Apply for voter ID card for nearest election office
    step 2: Required documents:-\n\ta.Age Proof\n\tb.Address Proof\n\tc.Identity Proof
    step 3: You can vote in Lok sabha, Vidhan sabha and local elections    
'''
    print(toPrint)


def voteEligibility():
    print("Checking Vote Eligiblity...")

    '''
    Vote Eligibility Criteria is based upon 2 things:-
    1. Nationality
    2. Age
    '''
    try:
        personName = input("Enter your name:")
        nationality = int(input("Are you an Indian citizen\n1--->Yes\n2--->No\nEnter:"))
        age=int(input("Enter your age:"))

        if nationality==1 and age>=18:
            print(f"Congratulations {personName}\nYou are Eligible to Vote in indian Elections.")
            furtherSteps()
        elif nationality==2 and age<18:
            print("You cannot Vote\n1. You are not an indian citizen!\n2.You are below 18!")
        elif nationality==1 and age<18:
            print(f"Unfortunately you cannot vote Now \n You need to wait for {18-age} year to Vote")
        elif nationality==2 and age>18:
            print("You cannot vote since you are not an indian citizen")
        else:
            print("Invalid data provided Try again")
    except Exception as e:
        print(e)

voteEligibility()
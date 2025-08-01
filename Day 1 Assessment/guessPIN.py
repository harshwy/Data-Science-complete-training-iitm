def setPIN():
    import random
    pin= random.randint(1000,9999)
    return pin

def temporaryLock():
    bankBrach = 'HDFC Bank'
    print(f"Your account has been temporarily Locked\n Reached the nearst branch of {bankBrach} to unlock it!")

def guessPIN():
    print("Your PIN has been temporarily Locked!")
    print("Guess your 4-Digit PIN to unlock ")
    
    newPIN = setPIN()
    attempts = 3
    print(f"Actual PIN = {newPIN}")
    print(f"_________________________________________\nAttemps Left : {attempts}")
    for i in range(1,attempts+2):
        if i==4:
            temporaryLock()
        userPIN = int(input("Enter your PIN _ _ _ _ :"))
        pinSize = len(str(userPIN))
        try:
            if pinSize !=4:
                print("PIN must be exactly 4 digits!")
                continue
            elif pinSize ==4 and userPIN!= newPIN:
                print("Incorrect PIN!")
                print(f"Attemps Left : {attempts-i}")
                continue
            elif pinSize==4 and userPIN==newPIN:
                print("PIN is correct!\nAccess Granted")
                break

        except Exception as e:
            print(e)
                
                
guessPIN()
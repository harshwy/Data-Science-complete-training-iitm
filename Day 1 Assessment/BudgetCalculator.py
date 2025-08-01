def displayExpenses(myDictionary):
    totalExpense=0
    print("------------Budget Summary------------")
    for expenseType,expenseValue in myDictionary.items():

        budgetSummary = f'''
                        {expenseType} = {expenseValue}
                        '''
        print(budgetSummary)
        totalExpense=totalExpense+expenseValue
    print(f"Total Expense: {totalExpense}")

def totalExpenses(mydict):
    ex=0
    for x,y in mydict.items():
        ex=ex+y
    return ex

def suggestions(saving):
    if saving>0:
        if saving >0 and saving<5000:
            print("I will recommend to invest in SIP")
        elif saving > 5000 and saving < 10000:
            print("I will recommend to invest in gold and SIPs")
        elif saving > 10000 and saving < 15000:
            print("I will recommend you to \n1. Fixed Deposits\n2.SIPs\n3.Gold Investment")
        else:
            print("I recommend you to invest in \n1.properties \n2.luxury Watches\n3.SIPs")

    else:

        print("Try to save money")

def monthlyExpensesCalculator():
    data = {}
    numberOfExpenses = int(input("Enter the number of expenses:"))
    for i in range(numberOfExpenses):
        expenseType = input(f"Enter Expense {i+1}: ")
        expenseValue= float(input(f"Enter amount for {expenseType} :"))
        data[expenseType]=expenseValue
    return data




def main():
    totalIncome = float(input("Enter your montly income:"))
    expenseDictionary = monthlyExpensesCalculator()
    total_expenses = totalExpenses(expenseDictionary)
    displayExpenses(expenseDictionary)
    savings = totalIncome - total_expenses
    print(f"Savings : {savings}")
    suggestions(savings)

main()



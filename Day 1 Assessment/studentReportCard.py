def gradeCalculation(marks):
    #below 33 = F
    if marks<33:
        return 'F'
    #above 33 = C
    elif marks>=33 and marks<45:
        return 'C'
    #45 to 59 = B
    elif marks >=45 and marks <60:
        return 'B'
    #60 to 69 = B+
    elif marks >=60 and marks <70:
        return 'B+'
    #70 to 79 = A
    elif marks>=70 and marks < 80:
        return 'A'
    #80 to 89 = A+
    elif marks>=80 and marks < 90:
        return 'A+'
    #90 & above = O
    elif marks >=90 and marks <=100:
        return 'O'
    else:
        return 'Invalid marks!'
    

def setMarks():
    no_of_subject = int(input("Enter the number of subjects:"))
    subDict = {}
    for i in range(no_of_subject):
        subject = input(f"Enter Subject {i+1}:")
        marks = int(input(f"Enter {subject} marks :"))
        subDict[subject] = marks
    return subDict



def generateReport():
    student_data=setMarks()
    headingList = ['Subject','Marks','Grade']
    tableData = []
    tableData.append(headingList)
    for sub,mark in student_data.items():
        currentList = []
        currentList.append(sub)
        currentList.append(mark)
        currentList.append(gradeCalculation(mark))
        tableData.append(currentList)

    import pandas as pd
    dataFrame = pd.DataFrame(tableData)
    print(dataFrame)

    
generateReport()
def bookSeat(personal_details,train_details,station_name,train_name):
    #personal_Details is a dictionary that stores the personal data
    import pymysql as py
    connection = py.connect(host='localhost',user='root',password='ayush',autocommit=True)
    cursor = connection.cursor()
    column_query=''''''
    for person_key,person_value in personal_details.items():
        column_query = f"{column_query} '{person_value}' ,"
    for train_key,train_value in train_details.items():
        column_query = f"{column_query} '{train_value}' ," 
    column_query=column_query[0:-1]
    station_name=station_name.replace(" ","_")
    train_name=train_name.replace(" ","_")
    cursor.execute(f'use {station_name};')
    query = f'''insert into {train_name} values({column_query});'''
    print(query)
    cursor.execute(query)
    connection.close()

def createTrain(station_name,train_name,column_list):
    try:
        import pymysql as py
        connection = py.connect(host='localhost',user='root',password='ayush',autocommit=True)
        cursor = connection.cursor()
        cursor.execute(f'''use {station_name};''')
        columnQuery = ''
        for i in column_list:
            to_insert=f''' {i} varchar(50) ,'''
            columnQuery=columnQuery+to_insert
        
        columnQuery=columnQuery[0:-3] + ')'
        query = f'''create table {train_name}({columnQuery});'''
        cursor.execute(query)
        #print(query)
        print("Train Created Successfully")
        connection.close()
    except Exception as e:
        print(e)

def createStation(stationName):
    try:
        import pymysql as py
        connection = py.connect(host='localhost',user='root',password='ayush',autocommit=True)
        cursor = connection.cursor()
        cursor.execute(f'''create database {stationName};''')
        print("Station Established Successfully!")  
        connection.close()  
    except Exception as e:
        print(e)

def setPersonalDetails():
    name = input("Enter your Name:")
    age = input("Enter you Age: ")
    gender = input("Gender Details\n1. Male\n2.Female\nEnter:") 
    data = {}
    data['name'] = name
    data['age'] = age
    data['gender'] =gender.lower()
    return data

def setTrainDetails():
    seat_no = input("Enter the seat number:")
    coach_no= input("Enter the coach number:") 
    data = {}
    data['seat_no']=seat_no
    data['coach_no']=coach_no
    return data

def client():
    print("Personal Details:-\n"+"-"*30)
    person_details=setPersonalDetails()
    print("-"*30+"\nEnter Train Details\n")
    station_name=input("Enter the station name:").lower()
    train_name=input("Enter the train name:").lower()
    print("-"*30+"\nSeat Booking:-")
    train_details=setTrainDetails()
    print("Booking in process...")
    bookSeat(person_details,train_details,station_name,train_name)

def server():
    print("Enter your Choice:-")
    print("1-->Establish new Station")
    print("2-->Establish New Train")
    print("3-->exit")
    choice = int(input("Enter your choice:"))
    if choice==1:
        station_name=input("Enter the station name:").lower()
        station_name=station_name.replace(" ","_")

        try:
            print("Creating New Station...")
            createStation(station_name)
        except Exception as e:
            print(e)
    elif choice==2:
        try:
            station_name = input("Enter the Station name:").lower()
            train_name =input("Enter the train name:").lower()
            station_name=station_name.replace(' ','_')
            train_name=train_name.replace(' ','_')
            train_column = ['name','age','gender','seat_no','coach_no']
            print("Creating New Train...")
            createTrain(station_name,train_name,train_column)
        except Exception as e:
            print(e)
    elif choice==3:
        print("Terminating....")
    else:
        print("Choice does not exists!")


client()
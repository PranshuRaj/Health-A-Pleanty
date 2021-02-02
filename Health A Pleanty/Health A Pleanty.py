import datetime
import random
import smtplib
import mysql.connector as mysql
from testing import sendemail_patient
from speaker import speak

print("Have you created the database?")
print("Y for yes and N for No")
sql_choice = input("enter your choice :- ")
user_name = input("Enter your Username:-\n")
password_user = input("Enter your Password:-\n")
if sql_choice.lower() == "n":
    try:

        mydb = mysql.connect(
            host="localhost",
            user=user_name,
            password=password_user
        )

        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE health_a_pleanty")
        mycursor.execute("use health_a_pleanty")
        mycursor.execute(
            "create table user_data(S_no int, First_name varchar(65), Last_name varchar(65), password varchar(65), receiver_email varchar(69), phone_number varchar(65), file_name varchar(65))")
        mycursor.execute(
            "create table user_hospital_data(p_name varchar(30), age int,disease_name varchar(30),hospital_data varchar(1000), receipt_number int)")
        print("Your database, table is created ")
        print("Please proceed to main program")
        print("\n Thank YOU!!")
        mydb.commit()
        mydb.close()
    except Exception as e:
        m = e
        print("Database already exist")
        print("Please proceed to main program")
        print("\n Thank YOU!!")

else:
    pass

host = mysql.connect(host="localhost", user=user_name, password=password_user, database="health_a_pleanty")
cursor = host.cursor(buffered=True)

speak("Welcome to our program")
print("\t \t \t \t HEALTH-A-PLENTY\n")
print("\t \t \t\t*STAY HOME, STAY SAFE*\n \n")
print("Press 1 for Sign Up")
print("Press 2 for Log In")
global value

our_otp = random.randint(111111, 999999)

with open("email.txt", "r") as f_email:
    email = f_email.read()

with open("imp.txt", "r") as f_imp:
    email_pass = f_imp.read()

mine_email = email
password = email_pass

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login(mine_email, password)


def time():
    return datetime.datetime.now()


user_selection = input("Enter your choice:- ")

if user_selection == "1":
    global value
    k = 1
    if k == 1:
        print("\t \t \t WELCOME \t")
        number_of_family = int(input("Enter how many people you want to add in list:"))
        for i in range(number_of_family):
            firs_name = input("Enter your first name:")
            last_name = input("Enter your last name:")
            phone_number = input("Enter your phone number:")
            cursor.execute("select * from user_data")
            check_data = cursor.fetchall()
            data_list = list(check_data)
            length = len(data_list)
            if length == 0:
                cursor.execute("insert into user_data values(0,'check','lastname','password','emailid', 'phonenumber', 'filename')")
            else:

                b = 0
                for i in range(length):
                    if check_data[i][5] == phone_number:
                        print("Phone number already exist\n")
                        print("Try with another phone number")
                        exit()
                    else:
                        if b == length:
                            print()
                        else:
                            continue

            user_password = input("Create your password")

            receiver_email = input("enter your email address:- ")

            message = "Your otp is " + str(our_otp) + ", Please don't share it with anyone"
            cursor.execute("select * from user_data")
            check_data = cursor.fetchone()
            data_list1 = list(check_data)
            length1 = len(data_list1)
            c = 0
            for i in range(length1):

                if check_data[4] == receiver_email:
                    print("Email id already exist\n")
                    print("Try with another Email ID")

                else:
                    if c == length1:
                        print()
                    else:
                        continue

            server.sendmail(mine_email, receiver_email, message)
            print("Otp has been send successfully")
            user_otp = input("Enter the otp send to your Email : ")
            if str(our_otp) == user_otp:
                print("Sign In successful")
            else:
                print("Incorrect otp")
                value = "wrong"
                server.quit()

            while True:
                if len(phone_number) == 10:
                    break
                else:
                    print("Invalid Number")

            file_name = input("Enter the file name:")
            with open(f"{file_name}", "a") as file:
                file.write(f"Hello\n {firs_name}")
                print(f"{firs_name} SUCCESSFULLY SIGN_UP")

                with open("serial_name.txt", "r") as serial:
                    serial_get = serial.read()
                    S_no_fake = int(float(serial_get))
                    S_no = S_no_fake + 1
                    serial.close()

                with open("serial_name.txt", "w") as serial:
                    S_no = str(S_no)
                    serial.write(S_no)
                    serial.close()

                data = (S_no, firs_name, last_name, user_password, receiver_email, phone_number, file_name)
                query = "insert into user_data values(%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(query, data)
                user_kanam = firs_name + "" + last_name
                sendemail_patient(receiver_email, user_kanam)
elif user_selection == "2":

    print("\t \t \t Log_in \t \t")

    email_check = input("Enter your email id :-\n")
    user_password = input("Enter password:")
    cursor.execute("select * from user_data")
    check_data = cursor.fetchall()
    data_list = list(check_data)
    length = len(data_list)
    a = 0
    for i in range(length):
        if check_data[i][4] == email_check and check_data[i][3] == user_password:
            file_name = check_data[i][6]
            your_name = check_data[i][1]
            with open(f"{file_name}", "r") as file:
                for i in file:
                    print(i, end="")
                    print(f"\n\t\t{your_name} LOG_IN SUCCESSFULLY")
                    print("\nYou can add and retrieve anything in you are health routine from here:")
                    choice = input("For yes press y and for no press m :- ")
                    if choice.lower() == "y":
                        def exercise(l):
                            if l == 1:
                                a = int(input("Enter 1 for exercise and 2 for food:"))
                                _name = file_name
                                if a == 1:
                                    exercise_type = input("Enter exercise\n")
                                    with open(f"{_name}", "a") as file:
                                        file.write("\n" + exercise_type + "\n" + "\t\t" + str([str(time())]))
                                        print(f"^\t{your_name} your data Successfully added\t^")
                                elif a == 2:
                                    food_type = input("Enter Food\n")
                                    with open(f"{_name}", "a") as file:
                                        file.write("\n" + food_type + "\n" "\t\t" + str([str(time())]))
                                        print(f"^\t{your_name} your data Successfully added\t^")

                                else:
                                    print("!INVALID!")

                            else:
                                print("!INVALID")


                        def retrieve(l):
                            if l == 2:
                                a = int(input("Enter 1 for Exercise and 2 for Food:"))
                                _name = file_name
                                if a == 1:
                                    with open(f"{_name}", "r") as file:
                                        for i in file:
                                            print(i, end="")
                                elif a == 2:
                                    with open(f"{_name}", "r") as file:
                                        for i in file:
                                            print(i, end="")
                                else:
                                    print(" !INVALID! ")
                            else:
                                print("!INVALID!")


                        l = int(input("Press 1 for log and 2 for retrieve:"))
                        if l == 1:
                            exercise(l)
                        elif l == 2:
                            retrieve(l)
                        else:
                            print("Choice does not match")

                    else:
                        sendemail_patient(email_check, your_name)
                        print("THANK YOU")

        else:
            a = a + 1
            if a == length:
                print("Incorrect Email Id and password used")
            else:
                continue

    else:
        print("Data not available")

else:
    print("!INVALID!")
print("Thanks for being here \U0001f44d")
speak("thanks for being here")
print("\U0001F60D")
host.commit()
host.close()
server.close()
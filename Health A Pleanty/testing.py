import random
import mysql.connector
import smtplib
from win32com.client import Dispatch


def speak(str):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str)


def sendemail_patient(email_id,patient_name):
    print("Want to take appointment?")
    print("Press y for yes and n for no")
    appoinment = input("Enter your choice")
    if appoinment.lower() == "y":
        data_base = mysql.connector.connect(host="localhost", user="root", password="2004", database="health_a_pleanty")

        my_cursor = data_base.cursor()
        try:
            a = "create table user_hospital_data(p_name varchar(30), age int, disease_name varchar(30),hospital_data " \
                "varchar(" \
                "1000),receipt_number int) "
            my_cursor.execute(a)

        except Exception as e:
            waste = e
            print("------------")

        hospital_name = [
            "HOSPITAL NAME:BATRA HOSPITAL AND MEDICAL RESEARCH CENTRE\nADDRESS:1,MEHRAULI BADARPUR ROAD,TUGHLAQABAD "
            "INSTITUTIONAL AREA,NEW DELHI-110062\nPHONE NUMBER:011-29958747,011-29957485",
            "HOSPITAL NAME:MAX DEVKI DEVI HEART & VASCULAR INSTITUTE\nADDRESS:2,PRESS ENCLAVE ROAD,PRESS ENCLAVE, "
            "SAKET, "
            "NEW DELHI-110017\nPHONE NUMBER:011-26515050",
            "HOSPITAL NAME:MAJEEDIA HOSPITALS\nADDRESS:GURU RAVIDAS MARG,TUGHLAQABAD INSTITUTIONAL AREA, "
            "NEW DELHI-110062\nPHONE NUMBER:011-26059669, 011-26059670, 011-26059671",
            "HOSPITAL NAME:INDRAPRASTHA APOLLO HOSPITALS\nADDRESS:N H. 2, MATHURA ROAD,SARITA VIHAR NEW "
            "DELHI-110076\nPHONE "
            "NUMBER:011-26925858,011-26925801",
            "HOSPITAL NAME:BANARSI DAS CHANDIWALA INSTITUTE OF MEDICAL SCIENCE\nADDRESS:BANARSI DAS CHANDIWALA ESTATE,"
            "MAA ANANDMAI MARG, KALAKAJI NEW DELHI-110019\nPHONE NUMBER:011-49020300",
            "HOSPITAL NAME:HOLY FAMILY HOSPITALS\nADDRESS:OKHLA ROAD, NEAR ESCORT HEART INSTITUTE,OKHLA, NEW DELHI - "
            "110025\nPHONE NUMBER:011-26845900,011-26845909,011-26332800",
            "HOSPITAL NAME:ESCORTS HEART INSTITUTE AND RESEARCH CENTRE\nADDRESS:OKHLA MAIN ROAD,OPPOSITE HOLY FAMILY "
            "HOSPITAL, MAIN OKHLA ROAD, JASOLA VIHAR, NEW DELHI - 110025\nPHONE NUMBER:011-26825000,011-26825001",
            "HOSPITAL NAME:LIONS KIDNEY HOSPITAL & UROLOGY RESEARCH INSTITUTE\nADDRESS:OPP. B BLOCK ,NEW FRIENDS "
            "COLONY, "
            "KHIZRABAD, NEW DELHI - 110065\nPHONE NUMBER:011-26324739,011-26324749,011-65807700",
            "HOSPITAL NAME:MAX HOSPITALS\nADDRESS:A-364, SECTOR-19, NOIDA ,UP -201 301\nPHONE NUMBER:0120-254 9999",
            "HOSPITAL NAME:MOOL CHAND KARAITI RAM HOSPITALS\nADDRESS:LALA LJAPAT RAI PATH, PART-III, LAJPAT NAGAR, "
            "NEW DELHI - 110024\nPHONE NUMBER:011-42000102",
            "HOSPITAL NAME:SAFDARJUNG HOSPITALS INSTITUTE OF PATHOLOGY (I.C.M.R.)\nADDRESS:AUROBINDO MARG,SAFDARJUNG, "
            "NEW DELHI - 110029\nPHONE NUMBER:011-26193614",
            "HOSPITAL NAME:AIIMS\nADDRESS:OPP. SAFDARJANG HOSPITAL, AUROBINDO MARG,ANSARI NAGAR, NEW DELHI - "
            "110029\nPHONE "
            "NUMBER:011-26588500,011-26594884",
            "HOSPITAL NAME:BASE HOSPITALS\nADDRESS:HOSPITAL ROAD, DELHI CANTT, NEW DELHI - 110010\nPHONE "
            "NUMBER:011-25666201",
            "HOSPITAL NAME:MATA CHANNAN DEVI HOSPITALS\nADDRESS:	C-1, JANAKPURI, NEW DELHI - 110058\nPHONE "
            "NUMBER:011-25554702",
            "HOSPITAL NAME:DEEN DYAL UPADHYAY HOSPITALS\nADDRESS:NEAR HARI NAGAR GHANTA GHAR, HARI NAGAR, NEW DELHI - "
            "110064\nPHONE NUMBER:011-25494462,011-25494408",
            "HOSPITAL NAME:DDU SUPER SPECIALITY HODPITALS\nADDRESS:LAL SAIN MANDIR MARG,C3 ROAD,JANAKPURI, NEW DELHI - "
            "110058\nPHONE NUMBER:11-25552023",
            "HOSPITAL NAME:RAM MANOHAR LOHIA HOSPITALS\nADDRESS:BABA KHARAK SINGH MARG,CONNAUGHT PLACE, NEW DELHI "
            "-110001\nPHONE NUMBER:011-23365525",
            "HOSPITAL NAME:SMT. SUCHETA KIRPLANI HOSPITALS\nADDRESS:PANCHKUIAN ROAD, NEAR BASANT LANE COLONY, "
            "CONNAUGHT "
            "PLACE, NEW DELHI - 110001\nPHONE NUMBER:011-23361524,011-23408447",
            "HOSPITAL NAME:MAULANA AZAD MEDICAL COLLEGE\nADDRESS:BAHADUR SHAH ZAFAR MARG,DELHI - 110002\nPHONE "
            "NUMBER:011-23239271",
            "HOSPITAL NAME:SANT PARMANAND HOSPITALS\nADDRESS:18, SHAMNATH MARG, CIVIL LINES, NEW DELHI-110054\nPHONE "
            "NUMBER:011-23994401",
            "HOSPITAL NAME:VALLABH BHAI PATEL INSTITUTE\nADDRESS:	CHHATRA MARG, DELHI UNIVERSITY, SARUP NAGAR, "
            "NORTH CAMPUS, "
            "NEW DELHI-110007\nPHONE NUMBER:011-24699328",
            "HOSPITAL NUMBER:Dr. B.L.KAPUR MEMORIAL HOSPITALS\nADDRESS:PUSA ROAD, NEW DELHI-110005\nPHONE "
            "NUMBER:011-30403040",
            "HOSPITAL NUMBER:BALAK RAM HOSPITALS\nADDRESS:TIMARPUR, NEW DELHI-110070\nPHONE NUMBER:011-23914315, "
            "011-23984204",
            "HOSPITAL NUMBER:HINDU RAO HOSPITALS\nADDRESS:RANI JHANSHI MARG,MALKAGANJ, NEW DELHI 110007\nPHONE "
            "NUMBER:011-23831177"]

        select_hospital = random.choice(hospital_name)
        print("Your near by hospital mention below", "\n" + select_hospital)
        choice = input("You want appointment mention above hospital\nFor Yes press y or NO press N")
        if choice.lower() == "y":

            patient_age = input("Enter the age of the patient:")
            disease_name = input("Enter the name of disease:")
            receipt_number = random.randint(100000, 999999)
            sql_insert = "insert into user_hospital_data values(""'" + patient_name + "'," + str(
                patient_age) + ",'" + disease_name + "','" + "    " + select_hospital + "'," + str(receipt_number) + ")"
            my_cursor.execute(sql_insert)
            print("Your receipt number:", receipt_number)
            data_base.commit()

            mine_email = "healthaplenty0@gmail.com"
            password = "uresuyeriqwnnlkr"

            server = smtplib.SMTP('smtp.gmail.com', 587)

            server.starttls()

            server.login(mine_email, password)
            message = f""""THANKS FOR GIVING US A CHANCE......
                           NAME:- {patient_name}
                           AGE :- {patient_age}
                           DISEASE:- {disease_name}
                                         HOSPITAL REFERED:- {select_hospital}
                           RECEIPT NUMBER:- {receipt_number}
            PLEASE REMEMBER YOUR RECEIPT NUMBER FOR FURTHER REFERENCE"""

            server.sendmail(mine_email, email_id, message)
            server.quit()
            print("Take care of your self :)")
            speak("Take care of your self ")
            speak("Your appointment is booked, please be on time")

        elif choice.lower() == "n":
            print("Take care of your self :)")
            speak("Take care of your self ")

        else:
            print("Invalid choice")

    else:
        speak("Thank You")
        print("!!Thank You!!")
        exit()
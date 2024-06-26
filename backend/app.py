from flask import Flask;
# import psycopg2

# conn = psycopg2.connect("")

import asyncio
from prisma import Prisma

async def createAppointment() -> bool:
    prisma = Prisma()
    await prisma.connect()
    
    response = await prisma.appoint.create(
        data= {
            'doctor_id': 'sdklfjklsajdf',
            'patient_id': 'pariekljflskjf0',
            'date': '21-06-2024'
        },
    )

    await prisma.disconnect()
    
    if (response.status == 200):
        return True
    else:
        return False


app = Flask('__main__')

# @app.route('/getAllStudent')
# def getAllStudent():
#     return 'all students data'

# @app.route('/createPatientsTables')
# def createPatientsTables():
#     try:
#         cur =conn.cursor()
#         cur.execute("""
#                 CREATE TABLE patients(
#                     ID  varchar(255) PRIMARY KEY NOT NULL,
#                     NAME varchar(255) NOT NULL,
#                     CONTACT varchar(255) NOT NULL,
#                     ADDRESS varchar(255) NOT NULL,
#                     AGE varchar(255) NOT NULL,
#                     DOB DATE NOT NULL,
#                     TIME INT NOT NULL,
#                     GENDER varchar(10) NOT NULL,
#                     ILLNESS varchar(255) NOT NULL
#                     )
#                     """)
#         conn.commit()
#         conn.close()
#         return True
#     except:
#         return False
    
# @app.route('/createDoctorsTable')
# def createDoctorsTable(): 
#     try:
#         cur = conn.cursor()
#         cur.execute("""
#         CREATE TABLE doctors(
#             ID INT PRIMARY KEY NOT NULL,
#             NAME varchar(255) NOT NULL,
#             CONTACT varchar(255) NOT NULL,
#             SPECIALITY varchar(255) NOT NULL,
#             GENDER varchar(10) NOT NULL,
#             TIME INT NOT NULL 
#         )           
#         """)
#         conn.commit()
#         conn.close()
#         return True
#     except:
#         return False
    
# @app.route('/createAppointmentTable')
# def createAppointmentTable(): 
#     try:
#         cur = conn.cursor()
#         cur.execute("""
#         CREATE TABLE appointment(
#             ID INT PRIMARY KEY NOT NULL,
#             PATIENT_ID varchar(255) NOT NULL,
#             DOCTOR_ID varchar(255) NOT NULL,
#             DT DATE NOT NULL,
#             STATUS varchar(10) NOT NULL
#         )           
#         """)
#         conn.commit()
#         conn.close()
#         return True
#     except:
#         return False
    
# @app.route('/createIllnessTable')
# def createIllnessTable(): 
#     try:
#         cur = conn.cursor()
#         cur.execute("""
#         CREATE TABLE illness(
#             NAME varchar(255) NOT NULL,
#             SYMPTOMS varchar(255) NOT NULL,
#             CURE varchar(255) NOT NULL,
#             DURATION INT NOT NULL,
#             DOCTOR varchar(255) NOT NULL
#         )
#         """)
#         conn.commit()
#         conn.close()
#         return True
#     except:
#         return False
        

     
    
   


if (__name__ == '__main__'):
    app.run(debug=True)
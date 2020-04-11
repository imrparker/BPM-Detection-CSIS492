# Program: Senior Project
# File: DPMdb.py
# Author: Parker Ostertag
# CSIS 492 Spring 2020

import mysql.connector

# TESTDATA
filename = "C:/filename.WAV"
tempo = "84"
peaksDetected = "500"
songDuration = "00:00:13.123"

def testConnection():
    mydb = mysql.connector.connect(
        host="localhost",
        username="root",
        password="root"
    )

    print(mydb)

def WAVInsert(filename, tempo, peaksDetected, songDuration):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            database="BPMdb",
            username="root",
            password="root"
        )
        mySql_insert_query = "INSERT IGNORE INTO wav_info VALUES (%s, %s, %s, %s)"

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, (filename, tempo, peaksDetected, songDuration))
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into BPMdb table")
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into BPMdb table{}".format(error))

    finally:
        if (connection.is_connected()):
            connection.close()
            print("MySQL connection is closed")


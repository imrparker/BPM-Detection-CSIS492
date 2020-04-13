# Program: Senior Project
# File: DPMdb.py
# Author: Parker Ostertag
# CSIS 492 Spring 2020

import mysql.connector
import userInterface

# TESTDATA
filename = "C:/filename.WAV"
tempo = "84"
peaksDetected = "500"
songDuration = "00:00:13.123"


def testConnection():
    try:
        test = mysql.connector.connect(
            host="localhost",
            username="root",
            password="root"
        )

    except mysql.connector.Error as error:
        userInterface.dbFail(("Failed to connect to MySQL Database{}".format(error)))

    finally:
        if (test.is_connected()):
            test.close()
            userInterface.dbSuccess("Connection Successful")


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
            userInterface.dbSaveSuccess()


def WAVDropRecords():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            database="BPMdb",
            username="root",
            password="root"
        )
        mySql_insert_query = "truncate wav_info"

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to delete records{}".format(error))

    finally:
        if (connection.is_connected()):
            connection.close()
            print("MySQL connection is closed")
            userInterface.dbDroppedRecords()


def MIDIInsert(filename, tempo):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            database="BPMdb",
            username="root",
            password="root"
        )
        mySql_insert_query = "INSERT IGNORE INTO midi_info VALUES (%s, %s)"

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, (filename, tempo))
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into BPMdb table")
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into BPMdb table{}".format(error))

    finally:
        if (connection.is_connected()):
            connection.close()
            print("MySQL connection is closed")
            userInterface.dbSaveSuccess()


def MIDIDropRecords():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            database="BPMdb",
            username="root",
            password="root"
        )
        mySql_insert_query = "truncate midi_info"

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to delete records{}".format(error))

    finally:
        if (connection.is_connected()):
            connection.close()
            print("MySQL connection is closed")
            userInterface.dbDroppedRecords()
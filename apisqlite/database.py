#!/usr/bin/env python3
"""Load csv file to sqlite3 database"""

import csv
import time
import sqlite3

def create_db_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM flask")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    return

def close_db_connection(conn):
    conn.close()
    return

def main():
    database = r"C:\Users\marqch1\PycharmProjects\verizon0513\flask.db"

    conn = create_db_connection(database)
    with conn:
        select_all_tasks(conn)

"""
    conn = sqlite3.connect('flask.db')
    try:
        conn.execute("DROP TABLE IF EXISTS FLASK")
        conn.execute('''CREATE TABLE IF NOT EXISTS FLASK
                (TIME VARCHAR2,
                NAME VARCHAR,
                IPADDR VARCHAR2,
                SERVICE VARCHAR,
                PORT VARCHAR);''')
    except:
        pass

    with open("mycsv.csv") as csvfile:
        csvdat = csv.reader(csvfile, delimiter=',')
        for row in csvdat:
            conn.execute("INSERT INTO FLASK (TIME,NAME,IPADDR,SERVICE,PORT) VALUES (?,?,?,?,?)",\
                         (time.ctime(), row[0], row[1], row[2], row[3]))
    conn.commit()

    cursor = conn.execute("SELECT TIME, NAME, IPADDR, SERVICE, PORT FROM FLASK")
    for row in cursor:
        print("TIME:", row[0])
        print("NAME:", row[1])
        print("IPADDR:", row[2])
        print("SERVICE:", row[3])
        print("PORT:", row[4])
        print("\n")

    print("Database operation done")
"""


if __name__ == "__main__":
    main()

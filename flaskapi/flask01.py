#!/usr/bin/env python3

import csv
import json
import sqlite3
import time

from flask import Flask

app = Flask(__name__)

from app import routes


@app.route("/")
@app.route("/index")
def vzw():
    return "Welcome to API automation"


@app.route("/hello/<name>")
def hello_name(name):
    return "Hello {}".format(name)


@app.route("/v1/csvreader/")
def csv_reader():
    with open("header.csv", encoding="utf8") as csvfile:
        csvdat = csv.DictReader(csvfile, delimiter=',')
        rows = list(csvdat)
    return json.dumps(rows)


@app.route("/v1/database/")
def database_reader():
    database = r"C:\Users\marqch1\PycharmProjects\verizon0513\flask.db"
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM FLASK")
    rows = cur.fetchall()

    dblist = []
    dbdict = {}
    for row in rows:
        dbdict['name'] = row[1]
        dbdict['ipaddr'] = row[2]
        dbdict['service'] = row[3]
        dbdict['port'] = row[4]
        dblist.append(dbdict.copy())

    return json.dumps(dblist)


if __name__ == "__main__":
    app.run(port=5006)


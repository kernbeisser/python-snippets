#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb


"""
A sample for getting database credentials in a script
"""


def login():
    credentials = []
    f = open('SOMEWHERE/.config.properties')

    credentials.append('localhost')
    # it's a java property file
    credentials.append(f.readline().split('=')[1].strip())
    credentials.append(f.readline().split('=')[1].strip())
    credentials.append(f.readline().split('=')[1].strip())

    return credentials


def print_data():
    con = mdb.connect(login()[0], login()[3], login()[1], login()[2])

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM SOME_TABLE")

        rows = cur.fetchall()

        desc = cur.description

        print "YOUR DATA", desc[0]

        for row in rows:
            print row


if __name__ == '__main__':
    print_data()

#!/usr/bin/python

#Paul Croft
#November 4, 2014

import sqlite3

cursor = None

def initializedb(dbname):
    global cursor
    connection = sqlite3.connect(dbname)
    cursor = connection.cursor()

def testdb():
    cursor.execute("""INSERT INTO catagories VALUES (NULL,'Misc','resources/catagories/Misc.html');""")
    cursor.execute("""INSERT INTO projects VALUES (NULL,'subwords','inbox/subwords',(SELECT catagoryid FROM catagories WHERE catagories.name == 'Misc'),'resources/projects/subwords.html');""")

    cursor.execute("""SELECT * FROM projects;""")
    print cursor.fetchone()


def main():

#    c.execute("""CREATE TABLE catagories(catagoryid INTEGER PRIMARY KEY, name text);""")
#    c.execute("""CREATE TABLE projects(projectid INTEGER PRIMARY KEY, name text, location text, catagoryid int key);""")
    initializedb("test.db")

    testdb()

if __name__ == '__main__':
    exit(main())
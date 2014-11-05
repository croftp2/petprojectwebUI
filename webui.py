#!/usr/bin/python

#Paul Croft
#November 4, 2014

from bottle import run, request, get, post, route
import sqlite3

import dbhandler

@route('/')
def mainpage():
    return "Hello world!"



dbhandler.initializedb("test.db")
dbhandler.testdb()
run(host='0.0.0.0', port=63142, debug=True, reloader=True)

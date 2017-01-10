# SQLtest.py
# querying the SQlite3 test.db database stars table

import sqlite3 as lite
import sys

# initialise the connection object con
con = None

try:
    # connect to the database and return a connection object
    con = lite.connect('test.db')
    # get the cursor object, used to traverse the records
    cur = con.cursor()
    # call the execute() method of the cursor object and execute the SQL statement
    cur.execute("SELECT * FROM stars WHERE spectral_type = 'O'")
    # Get all records
    rows = cur.fetchall()
    # print the data row by row
    for row in rows:
        print row


# exception handling    
except lite.Error, e:   
    print "Error %s:" % e.args[0]
    sys.exit(1)

# close the connection    
finally:   
    if con:
        con.close()

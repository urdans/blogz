""" pymysql cheatsheet - Urdans
The connection object members:
------------------------------

.begin()
    Begin transaction.

.close()
    Send the quit message and close the socket.
    Raises:	Error – If the connection is already closed.

.commit()
    Commit changes to stable storage.

.cursor(cursor=None)
    Create a new cursor to execute queries with.
    Parameters:	cursor – The type of cursor to create; one of Cursor, SSCursor, DictCursor, or SSDictCursor. None means use Cursor.

.open
    Return True if the connection is open

.rollback()
    Roll back the current transaction.

.select_db(db)
    Set current db.
    Parameters:	db – The name of the db.


Type of cursors:
----------------
    cursor = conn.cursor(Cursor) --> a regular cached cursor.
    cursor = conn.cursor(SSCursor) --> a non cached cursor. Used for remote DBs or slow remote connections.
    cursor = conn.cursor(DictCursor) --> a regular cached cursor which returns results as a dictionary.
    cursor = conn.cursor(SSDictCursor) --> a non cached cursor, which returns results as a dictionary.

cursor members:
---------------
.rowcount

.close()
    Closing a cursor just exhausts all remaining data.

.execute(query, args=None)
    Executes a query.
    Parameters:	
        query (str) – Query to execute.
        args (tuple, list or dict) – parameters used with query. (optional)
    Returns:	
        Number of affected rows
    Return type:	
        int
    If args is a list or tuple, %s can be used as a placeholder in the query. If args is a dict, %(name)s can be used as a placeholder in the query.

.executemany(query, args)
    Run several data against one query
    Parameters:	
        query – query to execute on server
        args – Sequence of sequences or mappings. It is used as parameter.
    Returns:	
        Number of rows affected, if any.

This method improves performance on multiple-row INSERT and REPLACE. Otherwise it is equivalent to looping over args with execute()

.fetchall()
    Fetch all the rows.


.fetchone()
    Fetch the next row.
------------------------------------------------------------------------------------------------------------------------------------------------------
"""

import pymysql.cursors
import hashlib
import os


ds = '**'
os.system('cls')

print('*'*70)
print(ds + 'MySQL user and database setup utility'.center(66) + ds)
print(ds + 'Jose Urdaneta - October 2018'.center(66) + ds)
print(ds + 'Dedicated to LauchCode for its free LC101 Summer bootcamp'.center(66) + ds)
print('*'*70)
print('\nThis utility will create a MySQL user and a database to be accessed locally.\nEnter the following parameters (press <Enter> for default).\n')

# ask for mysql user credentials
rj = 36
hc = input("Host computer [ locallhost ]: ".rjust(rj, ' '))
n = 3
for i in range(n):
    try:
        cp = input("Connection port [ 8889 ]: ".rjust(rj, ' '))
        if not cp:
            cp = -1
            break
        cp = int(cp)
        if cp not in range(2**16):
            raise
    except:
        if i == n-1:
            print('Using default value...')
            break
        else:
            print('\nInvalid connection port!.\nPlease try again!')
    else:
        break

aun = input("MySQL admin user [ root ]: ".rjust(rj, ' '))
ap = input("MySQL admin password [ root ]: ".rjust(rj, ' '))

host_computer = 'localhost'
connection_port = 8889
administrator_user_name = 'root'
administrator_password = 'root'

if hc:
    host_computer = hc
if cp != -1:
    connection_port = cp
if aun:
    administrator_user_name = aun
if ap:
    administrator_password = ap

# ask for the user and dabase to be created
print()
un = ''
while not un:
    un = input("New user name, not empty: ".rjust(rj, ' '))
up = ''
while not up:
    up = input("New user password, not empty: ".rjust(rj, ' '))

dbn = input("New database name [ {} ]: ".format(un).rjust(rj, ' '))

user = un
dbname = user
password = up
if dbn:
    dbname = dbn

print()

# prepare the queries
s1 = "CREATE USER '{}'@'localhost' IDENTIFIED WITH mysql_native_password;".format(
    user)
s2 = "GRANT USAGE ON *.* TO '{}'@'localhost' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;".format(
    user)
s3 = "SET PASSWORD FOR '{}'@'localhost' = PASSWORD('{}');".format(
    user, password)
s4 = "CREATE DATABASE IF NOT EXISTS `{}`;".format(dbname)
s5 = "GRANT ALL PRIVILEGES ON `{}`.* TO '{}'@'localhost';".format(dbname, user)

# start the connection and execute the queries
try:
    errmsg = '\n\nAl done!'
    connection = pymysql.connect(host=host_computer,
                                 port=connection_port,
                                 user=administrator_user_name,
                                 password=administrator_password)
except Exception as E:
    print('Error: ', E.__repr__())
    print('\nCannot continue.')
    quit()

with connection.cursor() as cursor:
    try:
        try:
            print("\nExecuting:\n"+s1)
            print('Result: ', cursor.execute(s1))
        except:
            print('Looks like user "{}" already exists!'.format(administrator_user_name))
        print("\nExecuting:\n"+s2)
        print('Result: ', cursor.execute(s2))
        print("\nExecuting:\n"+s3)
        print('Result: ', cursor.execute(s3))
        print("\nExecuting:\n"+s4)
        print('Result: ', cursor.execute(s4))
        print("\nExecuting:\n"+s5)
        print('Result: ', cursor.execute(s5))
    except Exception as E:
        print('Error: ', E.__repr__())
        errmsg = '\n\n Process ended with error.'

connection.close()
print(errmsg)

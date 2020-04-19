import pyodbc
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = '20.20.1.7'
database = 'X931D_CONFIG'
username = 'apatil'
password = 'Admin@123'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute('SELECT * FROM USERS_MASTER')
print('start')
for row in cursor:
    print('row = %r' % (row,))
print('end')
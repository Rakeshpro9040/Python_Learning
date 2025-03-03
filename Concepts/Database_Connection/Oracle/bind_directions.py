import cx_Oracle
import config

# construct a PL/SQL anonymous block
plsql = ('begin '
        'select count(*) into :customer_count ' 
        'from customers; '
        'end;')
try:
    # establish a new connection
    with cx_Oracle.connect(
            config.username,
            config.password,
            config.dsn,
            encoding=config.encoding) as connection:
        # create a cursor
        with connection.cursor() as cursor:
            # create a variable
            customer_count = cursor.var(int)
            # To have the Oracle Database return data to the Python, you need to create a variable by using the Cursor.var() method.
            # execute the pl/sql anonymous block
            cursor.execute(plsql, customer_count=customer_count)
            # show the value of the variable
            print(f'The number of customers is {customer_count.getvalue()}')
except cx_Oracle.Error as error:
    print(error)

'''
Output:
The number of customers is 319
'''
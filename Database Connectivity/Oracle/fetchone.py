import cx_Oracle
import config

sql = 'select customer_id, name ' \
    'from customers ' \
    'order by name'
try:
    with cx_Oracle.connect(
                config.username,
                config.password,
                config.dsn,
                encoding=config.encoding) as connection:
        with connection.cursor() as cursor:
            # print(f'cursor.arraysize: {cursor.arraysize}') # Default = 100
            # cursor.arraysize = 500 # To improve performance
            cursor.execute(sql)
            while True:
                row = cursor.fetchone()
                if row is None:
                    break # break when all rows are fetched
                print(row)
except cx_Oracle.Error as error:
    print(error)

import cx_Oracle
import config

sql = 'select customer_id, name ' \
    'from customers ' \
    'order by name'

try:
    # connect to the Oracle Database
    with cx_Oracle.connect(
            config.username,
            config.password,
            config.dsn,
            encoding=config.encoding) as connection:
        with connection.cursor() as cursor:
            # execute the SQL statement
            cursor.execute(sql)
            # fetch all rows
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(row)
except cx_Oracle.Error as error:
    print(error)

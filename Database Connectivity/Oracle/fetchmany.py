import cx_Oracle
import config

sql = 'select customer_id, name ' \
    'from customers ' \
    'order by name'
batch_size = 20
try:
    with cx_Oracle.connect(
            config.username,
            config.password,
            config.dsn,
            encoding=config.encoding) as connection:
        with connection.cursor() as cursor:
            # execute the SQL statement
            cursor.execute(sql)
            while True:
                # fetch rows
                rows = cursor.fetchmany(batch_size) 
                # ftech rows in batches, here we are fetching 20 rows in each iteraction, default = 100
                if not rows:
                    break # break when all rows are fetched in batches
                # display rows
                for row in rows:
                    print(row)
except cx_Oracle.Error as error:
    print(error)

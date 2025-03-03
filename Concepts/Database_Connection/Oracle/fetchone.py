import cx_Oracle
# import config
import config_ADB

sql = 'select customer_id, name ' \
    'from customers ' \
    'order by name'
try:
    # local
    # with cx_Oracle.connect(
    #             config.username,
    #             config.password,
    #             config.dsn,
    #             encoding=config.encoding) as connection:
    
    # cloud-ADB
    cx_Oracle.init_oracle_client(config_ADB.lib_dir)
    with cx_Oracle.connect(
                config_ADB.username,
                config_ADB.password,
                config_ADB.dsn) as connection:
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

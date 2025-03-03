# Installing the cx_Oracle module
# python -m pip show cx_oracle [Run this in powershell]
# python -m pip install cx_Oracle --upgrade

import cx_Oracle
import config

# Creating standalone connections
connection = None
try:
    connection = cx_Oracle.connect(
        config.username,
        config.password,
        config.dsn,
        encoding=config.encoding)

    # show the version of the Oracle Database
    print(connection.version)

    # Using with block
    # with cx_Oracle.connect(
    #     config.username,
    #     config.password,
    #     config.dsn,
    #     encoding=config.encoding) as connection:

    #     # show the version of the Oracle Database
    #     print(connection.version)
except cx_Oracle.Error as error:
    print(error)
# finally:
#     # release the connection
#     if connection:
#         connection.close()
#         # Alternatively, you can use with block in try block while opening the connection
#         # with block will take care of closing the connections automatically
#         # Refer to: "Using with block" section

'''
Output:
19.3.0.0.0
'''
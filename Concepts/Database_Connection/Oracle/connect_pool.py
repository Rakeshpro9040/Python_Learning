import cx_Oracle
import config

# Create the session pool
pool = cx_Oracle.SessionPool(
    config.username,
    config.password,
    config.database,
    min=100,
    max=100,
    increment=0,
    encoding=config.encoding
)

# Acquire a connection from the pool
connection = pool.acquire()

# Use the pooled connection
print('Using the connection')

# Release the connection to the pool
pool.release(connection)

# Close the pool
pool.close()

'''
Output:
Using the connection
'''
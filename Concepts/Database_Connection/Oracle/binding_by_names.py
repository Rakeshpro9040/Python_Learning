import cx_Oracle
import config

sql = ('select product_name '
    'from products '
    'where list_price > :price and '
    'standard_cost <= :cost')

try:
    with cx_Oracle.connect(
            config.username,
            config.password,
            config.dsn,
            encoding=config.encoding) as connection:
        cursor = connection.cursor()

        # Named
        for row in cursor.execute(sql, price=600, cost=500):
        # for row in cursor.execute(sql, cost=500, price=600):
        # Above 2 will give same results

        # Alternatively, can use dict to pass the parameters
        # for row in cursor.execute(sql, {'price':600, 'cost':500}):

        # Also, can pass the parameters in list --> This will behave like postional
        # price = 600
        # cost = 500
        # for row in cursor.execute(sql, [price, cost]):
        # for row in cursor.execute(sql, [cost, price]):
        # Above 2 will give different results due to positional in nature

        # Binding by names, use dictionanry to pass the parameters
            print(row[0])
        cursor.close()
except cx_Oracle.Error as error:
    print(error)

'''
Output:
Intel Xeon E5-2630 V3
Intel Core i7-4790K     
G.Skill Ripjaws V Series
G.Skill Ripjaws V Series
Kingston
G.Skill Ripjaws V Series
Kingston HyperX Predator
'''
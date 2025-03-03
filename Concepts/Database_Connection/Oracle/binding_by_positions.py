import cx_Oracle
import config

'''
def find_customer_by_id(customer_id):
    """
    Find customer name by id
    :param customer_id: id of the customer
    :return: customer name
    """
    sql = ('select name '
        'from customers '
        'where customer_id = :customer_id')
    customer_name = None
    try:
        # establish a new connection
        with cx_Oracle.connect(
                config.username,
                config.password,
                config.dsn,
                encoding=config.encoding) as connection:
            # create a cursor
            with connection.cursor() as cursor:
                cursor.execute(sql, [100])
                row = cursor.fetchone()
                print(row)
                if row:
                    customer_name = row[0]
    except cx_Oracle.Error as error:
        print(error)

    return customer_name


# Call the above function
print(find_customer_by_id(100))  # Verizon
'''

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
        for row in cursor.execute(sql, [600, 500]):
        # Binding by positions, use list to pass the parameters
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
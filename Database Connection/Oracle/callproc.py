import cx_Oracle
import config as cfg


def get_order_count(salesman_id, year):
    """
    Get order count by salesman and year
    :param salesman_id:
    :param year:
    :return: the number of orders by a salesman and year
    """
    try:
        # create a connection to the Oracle Database
        with cx_Oracle.connect(cfg.username,
                            cfg.password,
                            cfg.dsn,
                            encoding=cfg.encoding) as connection:
            # create a new cursor
            with connection.cursor() as cursor:
                # create a new variable to hold the value of the
                # declare order_count as OUT parameter
                order_count = cursor.var(int)
                # call the stored procedure
                cursor.callproc('get_order_count',
                                [salesman_id, year, order_count])
                '''
                It is important to note that when you call the Cursor.callproc() method, cx_Oracle actually generates the following anonymous block and then executes it:
                cursor.execute("begin get_order_count(:1,:2,:3); end;", [salesman_id, year, order_count])
                '''
                return order_count.getvalue()
    except cx_Oracle.Error as error:
        print(error)


if __name__ == '__main__':
    orders = get_order_count(54, 2017)
    print(orders)  # 3

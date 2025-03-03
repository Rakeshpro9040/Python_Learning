import cx_Oracle
import config as cfg


def get_revenue(salesman_id, year):
    """
    Get revenue by salesman in a specific year
    :param salesman_id:
    :param year:
    :return: the revenue
    """
    revenue = None
    try:
        # create a connection to the Oracle Database
        with cx_Oracle.connect(cfg.username,
                            cfg.password,
                            cfg.dsn,
                            encoding=cfg.encoding) as connection:
            # create a new cursor
            with connection.cursor() as cursor:
                # call the function
                revenue = cursor.callfunc('get_revenue',
                                        float,
                                        [salesman_id, year])
                # In the Cursor.callfunc() method: the first argument is the stored function’s name, the second argument is the type of the returned value, and the third argument is a list of arguments passed to the stored function.
    except cx_Oracle.Error as error:
        print(error)

    return revenue


if __name__ == '__main__':
    sales_revenue = get_revenue(54, 2017)
    print(sales_revenue)  # 1160350.79

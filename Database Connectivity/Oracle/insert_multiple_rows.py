import cx_Oracle
import config as cfg
from datetime import datetime


def insert_billings(billings):
    """
    insert multiple billings
    :param billings: a list of billings
    :return:
    """
    # construct an insert statement that add a new row to the billing_headers table
    sql = ('insert into billing_headers(billing_date, amount, customer_id, note) '
        'values(:billing_date,:amount,:customer_id,:note)')

    try:
        # establish a new connection
        with cx_Oracle.connect(cfg.username,
                            cfg.password,
                            cfg.dsn,
                            encoding=cfg.encoding) as connection:
            # create a cursor
            with connection.cursor() as cursor:
                # execute the insert statement
                cursor.executemany(sql, billings)
                # The Cursor.executemany() is more efficient than calling the Cursor.execute() method multiple times because it reduces network transfer and database load.
                # commit work
                connection.commit()
    except cx_Oracle.Error as error:
        print('Error occurred:')
        print(error)


if __name__ == '__main__':
    billing_docs = [
        (datetime.now(),1000, 1, None),
        (datetime.now(), 1500, 2, None),
        (datetime.now(), 1700, 3, None),
    ]
    # insert multiple billings
    insert_billings(billing_docs)

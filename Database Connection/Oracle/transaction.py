import cx_Oracle
import config as cfg
from datetime import datetime


def insert_billing_header(billing_header, cursor):
    """
    Insert a new row into the billing_header table and
    return the inserted billing no
    :param billing_header:
    :param cursor:
    :return:
    """
    sql = ('insert into billing_headers(billing_date, amount, customer_id) '
        'values(:billing_date,:amount,:customer_id) '
        'returning billing_no into :billing_no')
    # declare billing_no as OUT parameter
    billing_no = cursor.var(int)
    # add the variable to billing_header list
    billing_header.append(billing_no)
    # execute the insert statement
    cursor.execute(sql, billing_header)
    # return the inserted value
    return billing_no.getvalue()[0]


def insert_billing_items(billing_no, billing_items, cursor):
    """
    insert billing items
    :param billing_no:
    :param billing_items:
    :param cursor:
    :return:
    """
    # insert into billing items
    sql = ('insert into billing_items(billing_no, product_id, price) '
        'values(:billing_no,:product_id,:price)')

    items = []
    for item in billing_items:
        items.append((billing_no, item[0], item[1]))

    cursor.executemany(sql, items)


def insert_billing_doc(billing_header, billing_items):
    """
    Insert a billing document
    :param billing_header: 
    :param billing_items: 
    :return: 
    """
    try:
        # establish a new connection
        with cx_Oracle.connect(cfg.username,
                            cfg.password,
                            cfg.dsn,
                            encoding=cfg.encoding) as connection:
            # create a cursor
            with connection.cursor() as cursor:
                # insert the billing header
                billing_no = insert_billing_header(billing_header, cursor)
                # rollback the transaction if no billing no is generated
                if not billing_no:
                    connection.rollback()
                # insert the billing items
                insert_billing_items(billing_no, billing_items, cursor)
                # commit the transaction
                connection.commit()
    except cx_Oracle.Error as error:
        print(error)


if __name__ == '__main__':
    insert_billing_doc(
        [datetime.now(), 1, 1000],
        [(1, 200),
        (2, 300),
        (3, 500)])

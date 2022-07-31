import cx_Oracle
import config as cfg


def update_billing(billing_no, amount):
    """
    Update new amount for a billing
    :param billing_no:
    :param amount:
    :return:
    """
    sql = ('update billing_headers '
        'set amount = :amount '
        'where billing_no = :billing_no')

    try:
        # establish a new connection
        with cx_Oracle.connect(cfg.username,
                            cfg.password,
                            cfg.dsn,
                            encoding=cfg.encoding) as connection:
            # create a cursor
            with connection.cursor() as cursor:
                # execute the insert statement
                cursor.execute(sql, [amount, billing_no])
                # commit the change
                connection.commit()
    except cx_Oracle.Error as error:
        print(error)


if __name__ == '__main__':
    update_billing(1, 2000)

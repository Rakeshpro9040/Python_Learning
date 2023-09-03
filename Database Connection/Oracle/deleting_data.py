import cx_Oracle
import config as cfg


def delete_billing(billing_no):
    """
    Delete a billing based on a billing no.
    :param billing_no:
    :return:
    """
    sql = ('delete from billing_headers '
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
                cursor.execute(sql, [billing_no])
                # commit the change
                connection.commit()
    except cx_Oracle.Error as error:
        print(error)


if __name__ == '__main__':
    delete_billing(1)

import cx_Oracle
import config_ADB

# Connect to oracle instantclient
cx_Oracle.init_oracle_client(config_ADB.lib_dir)

connection = cx_Oracle.connect(
                user=config_ADB.username, 
                password=config_ADB.password, 
                dsn=config_ADB.dsn)

cursor = connection.cursor()

# Create a table

cursor.execute("""begin
                     execute immediate 'drop table pytab';
                     exception when others then if sqlcode <> -942 then raise; end if;
                  end;""")
cursor.execute("create table pytab (id number, data varchar2(20))")

# Insert some rows

rows = [ (1, "First" ),
         (2, "Second" ),
         (3, "Third" ),
         (4, "Fourth" ),
         (5, "Fifth" ),
         (6, "Sixth" ),
         (7, "Seventh" ) ]

cursor.executemany("insert into pytab(id, data) values (:1, :2)", rows)

connection.commit()  # uncomment to make data persistent

# Now query the rows back

for row in cursor.execute('select * from pytab'):
    print(row)
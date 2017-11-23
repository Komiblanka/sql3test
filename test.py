import sqlite3

sqlite_file = 'python.sqlite'    # name of the sqlite database file
table_name2 = 'my_table_2'  # name of the table to be created
first_field = 'my_1st_column' # name of the column
first_field_type = 'INTEGER'  # column data type

second_field = 'my_2nd_column' # name of the column
second_field_type = 'TEXT'  # column data type
number = 123456
text = "HELLO"

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Creating a table
c.execute('CREATE TABLE {} ({} {} PRIMARY KEY, {} {})'\
        .format(table_name2, first_field, first_field_type, second_field, second_field_type))

# Doing an insert without sql injection
try:
    cmd = "INSERT INTO {tn} ({idf},{iidf}) VALUES (?, ?)".format(table_name2, first_field, second_field)
    c.execute(cmd, (number, text)
except sqlite3.IntegrityError:
        print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()

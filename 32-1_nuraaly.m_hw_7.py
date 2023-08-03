import sqlite3


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price FLOAT(10,2) NOT NULL DEFAULT 0.0,
quantity INTEGER NOT NULL DEFAULT 0,
)
'''

def insert_product(conn, product):
    sql = '''INSERT INTO products 
    (product_title, price, quantity)
    VALUES (?, ?, ?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def update_product_quantity(conn, product):
    sql = '''UPDATE products SET quantity = ?
    WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def update_product_price(conn, product):
    sql = '''UPDATE products SET price = ?
    WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def delete_product(conn, id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def select_all_products(conn):
    sql = '''SELECT * FROM products'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)

        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_products_by_limit(conn, limit):
    sql = '''SELECT * FROM products 
    WHERE price <= 100 AND quantity >= 5'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (limit,))

        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

def search_products_by_title(conn, product_title):
    sql = '''SELECT * FROM products
    WHERE product_title LIKE ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (product_title,))

        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

connection_to_db = create_connection('hw.db')
if connection_to_db is not None:
    print('Successfully connected to DB!')
    # create_table(connection_to_db, sql_create_products_table)
    # insert_product(connection_to_db, ('МЫЛО', 70.0, 25))
    # insert_product(connection_to_db, ('ШАМПУНЬ', 380.0, 10))
    # insert_product(connection_to_db, ('БУМАГА', 15.0, 50))
    # insert_product(connection_to_db, ('БРИТВА', 70.0, 30))
    # insert_product(connection_to_db, ('ГУБКА', 25.0, 15))
    # insert_product(connection_to_db, ('ТРЯПКА', 50.0, 18))
    # insert_product(connection_to_db, ('ЗУБНАЯ ПАСТА', 250.0, 23))
    # insert_product(connection_to_db, ('ЗУБНАЯ ЩЕТКА', 50.0, 13))
    # insert_product(connection_to_db, ('САЛФЕТКИ', 50.0, 17))
    # insert_product(connection_to_db, ('КРЕМ ДЛЯ РУК', 250.0, 10))
    # insert_product(connection_to_db, ('АНТИПЕРСПИРАНТ', 200.0, 10))
    # insert_product(connection_to_db, ('ДЕЗОДОРАНТ', 200.0, 10))
    # insert_product(connection_to_db, ('ГЕЛЬ ДЛЯ ДУША', 230.0, 5))
    # insert_product(connection_to_db, ('ПОДГУЗНИКИ', 500.0, 50))
    # insert_product(connection_to_db, ('ПЕНА ДЛЯ БРИТЬЯ', 180.0, 7))
    # update_product_price(connection_to_db,(75.0, 1))
    # update_product_quantity(connection_to_db,(26, 1))
    # delete_product(connection_to_db, 7)
    # select_all_products(connection_to_db)
    # select_products_by_limit(connection_to_db)
    # search_products_by_title(connection_to_db, 'ГЕЛЬ')
    connection_to_db.close()
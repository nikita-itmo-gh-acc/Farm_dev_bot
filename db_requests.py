from db_create import cursor, farm_dev_db


def find_products_by_name(pattern):
    cursor.execute("USE sql7707767")
    cursor.execute(f"SELECT * FROM Products WHERE name LIKE '%{pattern}%';")
    return cursor.fetchall()


def find_seller(pattern):
    cursor.execute("USE sql7707767")
    cursor.execute(f"SELECT * FROM Sellers WHERE name LIKE '%{pattern}%';")
    return cursor.fetchall()


def find_seller_by_id(sell_id):
    cursor.execute("USE sql7707767")
    cursor.execute(f"SELECT phone FROM Sellers WHERE id={sell_id};")
    return cursor.fetchall()


def find_user_by_email(email):
    cursor.execute("USE sql7707767")
    cursor.execute(f"SELECT * FROM Users WHERE email = '{email}';")
    return cursor.fetchall()

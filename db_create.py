import mysql.connector

farm_dev_db = mysql.connector.connect(
  host="sql7.freesqldatabase.com",
  user="sql7707767",
  password="TqQSwxk97V",
  port="3306"
)

cursor = farm_dev_db.cursor()


def create_db():
    global cursor
    cursor.execute("USE sql7707767;")
    cursor.execute("CREATE TABLE IF NOT EXISTS Users ( \
                    id INTEGER PRIMARY KEY AUTO_INCREMENT, \
                    name VARCHAR(128) NOT NULL, \
                    email VARCHAR(128) UNIQUE NOT NULL, \
                    zipcode CHAR(6));"
                   )
    cursor.execute("CREATE TABLE IF NOT EXISTS Sellers ( \
                    id INTEGER PRIMARY KEY AUTO_INCREMENT, \
                    name VARCHAR(128) NOT NULL, \
                    email VARCHAR(128) UNIQUE NOT NULL, \
                    phone VARCHAR(128) UNIQUE NOT NULL \
                    );")
    cursor.execute("CREATE TABLE IF NOT EXISTS Products ( \
                    id INTEGER PRIMARY KEY AUTO_INCREMENT, \
                    name VARCHAR(128), \
                    production_date DATE, \
                    expiration_date DATE, \
                    seller_id INTEGER, \
                    FOREIGN KEY (seller_id) REFERENCES Sellers (id));"
                   )


def delete_db():
    global cursor
    cursor.execute("DROP DATABASE sql7707767;")


if __name__ == "__main__":
    create_db()

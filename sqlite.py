import sqlite3


def create_table():
    conn = sqlite3.connect("lite.db")

    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store ( item TEXT, quantity INTEGER, price REAL )")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")

    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("lite.db")

    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    results = cur.fetchall()
    conn.close()
    return results


def delete(item):
    conn = sqlite3.connect("lite.db")

    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = ?", (item,))
    conn.commit()
    conn.close()


def update(item, quantity):
    conn = sqlite3.connect("lite.db")

    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = ? WHERE item = ?", (quantity, item))
    conn.commit()
    conn.close()


# insert("Water Bottle", 10, 2.99)
update("Water Bottle", 20)
print(view())

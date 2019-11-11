import psycopg2
import json

with open("credentials.json") as credentials_file:
    credentials = json.load(credentials_file)


def create_table():
    conn = psycopg2.connect("dbname='%s' user='%s' password='%s' host='%s' port='%s'"
                            % (credentials["database"], credentials["user"], credentials["pass"], credentials["host"],
                               credentials["port"]))

    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store ( item TEXT, quantity INTEGER, price REAL )")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='%s' user='%s' password='%s' host='%s' port='%s'"
                            % (credentials["database"], credentials["user"], credentials["pass"], credentials["host"],
                               credentials["port"]))

    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("dbname='%s' user='%s' password='%s' host='%s' port='%s'"
                            % (credentials["database"], credentials["user"], credentials["pass"], credentials["host"],
                               credentials["port"]))

    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    results = cur.fetchall()
    conn.close()
    return results


def delete(item):
    conn = psycopg2.connect("dbname='%s' user='%s' password='%s' host='%s' port='%s'"
                            % (credentials["database"], credentials["user"], credentials["pass"], credentials["host"],
                               credentials["port"]))

    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = %s", (item,))
    conn.commit()
    conn.close()


def update(item, quantity):
    conn = psycopg2.connect("dbname='%s' user='%s' password='%s' host='%s' port='%s'"
                            % (credentials["database"], credentials["user"], credentials["pass"], credentials["host"],
                               credentials["port"]))

    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = %s WHERE item = %s", (quantity, item))
    conn.commit()
    conn.close()


# insert("Water Bottle", 10, 2.99)
# update("Water Bottle", 20)
print(view())

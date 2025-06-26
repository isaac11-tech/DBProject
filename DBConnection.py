import mysql.connector
from mysql.connector import Error


def connect(cs=None):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            database='classicmodels'
        ) if cs is None else mysql.connector.connect(**cs)

        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error: {e}")
        return None


def disconnect(conn):
    if conn.is_connected():
        conn.close()


def execute_query(sql, cs=None):
    conn = connect(cs)
    if conn is None:
        return []

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    except Error as e:
        print(f"Error executing query: {e}")
        return []
    finally:
        cursor.close()
        disconnect(conn)


def print_results(results):
    if not results:
        print("No results found.")
        return

    for row in results:
        for key, value in row.items():
            print(f"{key}: {value}")
        print("---")

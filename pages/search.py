import sqlite3
import urllib.request
import urllib.parse
import re
from sqlite3 import Error

def create_connection(db_file):
	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print(e)
	return None
 
def select_all_employees(conn, num):
	cur = conn.cursor()
	cur.execute("SELECT * FROM pages_employees")
	rows = cur.fetchall()
	rows = sorted(rows, key=lambda row: -row[num])
	#for row in rows:
	#	print(row)
	i = 0
	for row in rows:
		row = [row[1], row[2], row[num]]
		rows[i] = row
		i += 1
	return rows

def search_database(num):
    database = "db.sqlite3"
    conn = create_connection(database)
    #with conn:
    return select_all_employees(conn, num)
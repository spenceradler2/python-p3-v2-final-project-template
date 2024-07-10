import sqlite3

CONN = sqlite3.connect('db/traveling_information.db')
CURSOR = CONN.cursor()

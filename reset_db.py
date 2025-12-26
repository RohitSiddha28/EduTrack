import sqlite3

conn = sqlite3.connect("attendance.db")
cur = conn.cursor()

cur.execute("DELETE FROM attendance")
cur.execute("DELETE FROM students")
cur.execute("DELETE FROM subjects")

cur.execute("DELETE FROM sqlite_sequence")

conn.commit()
conn.close()

print("Database data cleared successfully")

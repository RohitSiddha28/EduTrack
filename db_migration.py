# import sqlite3

# conn = sqlite3.connect("attendance.db")
# cursor = conn.cursor()

# cursor.execute("""
# ALTER TABLE subjects
# ADD COLUMN active INTEGER DEFAULT 1
# """)

# conn.commit()
# conn.close()

# print("Subjects migration completed")

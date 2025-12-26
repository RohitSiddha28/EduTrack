import sqlite3

def get_connection():
    return sqlite3.connect("attendance.db")

def add_student():
    name = input("Enter name: ").strip()
    roll = input("Enter roll: ").strip()

    if not name or not roll:
        print("Invalid input")
        return

    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO students (name, roll_no) VALUES (?, ?)",
            (name, roll)
        )
        conn.commit()
        print("Student added")
    except sqlite3.IntegrityError:
        print("Roll already exists")
    conn.close()

def add_subject():
    name = input("Enter subject name: ").strip()
    if not name:
        print("Invalid input")
        return

    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO subjects (subject_name) VALUES (?)",
            (name,)
        )
        conn.commit()
        print("Subject added")
    except sqlite3.IntegrityError:
        print("Subject already exists")
    conn.close()

def mark_attendance():
    sid = input("Student ID: ")
    subid = input("Subject ID: ")
    date = input("Date (YYYY-MM-DD): ")
    status = input("Status (P/A): ").upper()

    if status not in ("P", "A"):
        print("Invalid status")
        return

    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO attendance (student_id, subject_id, date, status)
            VALUES (?, ?, ?, ?)
        """, (sid, subid, date, status))
        conn.commit()
        print("Attendance marked")
    except sqlite3.IntegrityError:
        print("Attendance already exists")
    conn.close()

def constructive_menu():
    while True:
        print("""
--- Add / Create Menu ---
1. Add Student
2. Add Subject
3. Mark Attendance
0. Back
""")
        ch = input("Choice: ").strip()

        if ch == "1":
            add_student()
        elif ch == "2":
            add_subject()
        elif ch == "3":
            mark_attendance()
        elif ch == "0":
            break
        else:
            print("Invalid choice")

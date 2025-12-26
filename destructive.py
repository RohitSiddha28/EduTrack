import sqlite3

def get_connection():
    return sqlite3.connect("attendance.db")

def deactivate_student():
    sid = input("Student ID: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE students SET active=0 WHERE student_id=?", (sid,))
    conn.commit()
    print("Student deactivated")
    conn.close()

def activate_student():
    sid = input("Student ID: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE students SET active=1 WHERE student_id=?", (sid,))
    conn.commit()
    print("Student activated")
    conn.close()

def deactivate_subject():
    sid = input("Subject ID: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE subjects SET active=0 WHERE subject_id=?", (sid,))
    conn.commit()
    print("Subject deactivated")
    conn.close()

def activate_subject():
    sid = input("Subject ID: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE subjects SET active=1 WHERE subject_id=?", (sid,))
    conn.commit()
    print("Subject activated")
    conn.close()

def destructive_menu():
    while True:
        print("""
--- Activate / Deactivate Menu ---
1. Deactivate Student
2. Activate Student
3. Deactivate Subject
4. Activate Subject
0. Back
""")
        ch = input("Choice: ").strip()

        if ch == "1":
            deactivate_student()
        elif ch == "2":
            activate_student()
        elif ch == "3":
            deactivate_subject()
        elif ch == "4":
            activate_subject()
        elif ch == "0":
            break
        else:
            print("Invalid choice")

import sqlite3

def get_connection():
    return sqlite3.connect("attendance.db")

def list_students(active=1):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT student_id,name,roll_no FROM students WHERE active=?",
        (active,)
    )
    rows = cur.fetchall()
    conn.close()
    for r in rows:
        print(r)

def list_subjects(active=1):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT subject_id,subject_name FROM subjects WHERE active=?",
        (active,)
    )
    rows = cur.fetchall()
    conn.close()
    for r in rows:
        print(r)

def attendance_percentage():
    sid = input("Student ID: ")
    subid = input("Subject ID: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT COUNT(*),
               SUM(CASE WHEN status='P' THEN 1 ELSE 0 END)
        FROM attendance
        WHERE student_id=? AND subject_id=?
    """, (sid, subid))

    total, present = cur.fetchone()
    conn.close()

    if total == 0:
        print("No records")
    else:
        print(f"Attendance: {(present/total)*100:.2f}%")

def subject_wise_attendance_percentage():
    subject_id = input("Enter Subject ID: ").strip()

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            s.student_id,
            s.name,
            s.roll_no,
            COUNT(a.attendance_id) AS total_classes,
            SUM(CASE WHEN a.status = 'P' THEN 1 ELSE 0 END) AS present_days,
            ROUND(
                (SUM(CASE WHEN a.status='P' THEN 1 ELSE 0 END) * 100.0) 
                / COUNT(a.attendance_id), 2
            ) AS percentage
        FROM attendance a
        JOIN students s ON a.student_id = s.student_id
        WHERE a.subject_id = ?
          AND s.active = 1
        GROUP BY s.student_id
        ORDER BY percentage DESC
    """, (subject_id,))

    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("No attendance data found")
        return

    print("\nStudent-wise Attendance Percentage:")
    print("ID | Name | Roll | %")
    for r in rows:
        print(r[0], r[1], r[2], r[5])

def date_wise_attendance():
    date = input("Enter date (YYYY-MM-DD): ").strip()

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            s.name,
            s.roll_no,
            sub.subject_name,
            a.status
        FROM attendance a
        JOIN students s ON a.student_id = s.student_id
        JOIN subjects sub ON a.subject_id = sub.subject_id
        WHERE a.date = ?
          AND s.active = 1
          AND sub.active = 1
        ORDER BY s.roll_no, sub.subject_name
    """, (date,))

    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("No attendance records found for this date")
        return

    print("\nDate-wise Attendance:")
    print("Name | Roll | Subject | Status")
    for r in rows:
        print(r[0], r[1], r[2], r[3])

def status_menu():
    while True:
        print("""
--- View / Status Menu ---
1. List Active Students
2. List Inactive Students
3. List Active Subjects
4. List Inactive Subjects
5. Attendance Percentage (Single Student)
6. Subject-wise Attendance Percentage (All Students)
7. Date-wise Attendance (All Students & Subjects)
0. Back
""")
        ch = input("Choice: ").strip()

        if ch == "1":
            list_students(1)
        elif ch == "2":
            list_students(0)
        elif ch == "3":
            list_subjects(1)
        elif ch == "4":
            list_subjects(0)
        elif ch == "5":
            attendance_percentage()
        elif ch == "6":
            subject_wise_attendance_percentage()
        elif ch == "7":
            date_wise_attendance()
        elif ch == "0":
            break
        else:
            print("Invalid choice")


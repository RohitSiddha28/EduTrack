# 📚 Attendance Management System (Python + SQL)

A menu-driven Attendance Management System built using **Python** and **SQLite**, designed with proper database modeling, soft deletes, and analytical SQL queries. 

This project focuses on **backend logic, data integrity, and real-world system design**, rather than UI.

---

## 🚀 Features

### 👨‍🎓 Student Management
* Add new students.
* **Soft delete** (deactivate) students.
* Reactivate inactive students.
* Prevent duplicate roll numbers.
* Preserve historical attendance data even after deactivation.

### 📘 Subject Management
* Add new subjects.
* **Soft delete** (deactivate) subjects.
* Reactivate inactive subjects.
* Prevent duplicate subject entries.

### 🗓️ Attendance Management
* Mark attendance (Present / Absent).
* **Validation:** Prevent duplicate attendance for the same student, subject, and date.
* **Integrity:** Allow attendance only for *active* students and subjects.

### 📊 Attendance Analytics
* Individual student attendance percentage per subject.
* Subject-wise attendance percentage of all students.
* Date-wise attendance report (all students, all subjects).
* Active / Inactive student and subject listings.

---

## 🧠 Design Highlights
* **Soft Delete Pattern:** Uses an `active` flag (0/1) instead of hard deletion (`DELETE FROM`) to ensure historical data remains intact for reporting.
* **Database Constraints:** Enforces data integrity at the database level (UNIQUE, CHECK).
* **Modular Architecture:** Code is split into logical modules (constructive, destructive, analytics) for better maintainability.
* **SQL Aggregation:** Utilizes `GROUP BY` and `CASE WHEN` for generating dynamic reports.

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Database:** SQLite (Chosen for rapid development and portability).
* **SQL Concepts Used:**
    * Joins (INNER, LEFT)
    * Aggregate functions (COUNT, SUM, AVG)
    * Constraints (UNIQUE, CHECK, FOREIGN KEYS)
    * Soft Delete Logic
    * Parameterized Queries (Security)

> **Note:** The project is designed to be database-agnostic. It can be migrated to **MySQL** or **PostgreSQL** with minimal changes to the connection string and schema syntax.

---

## 📁 Project Structure

```text
attendance_system/
│
├── main.py              # Main application entry point (Menu System)
├── constructive.py      # Add / create operations (INSERT)
├── destructive.py       # Activate / deactivate operations (UPDATE flags)
├── status.py            # View and analytics operations (SELECT / AGGREGATE)
├── db_setup.py          # Database schema creation
├── reset_db.py          # Reset all data (development utility)
└── attendance.db        # SQLite database (auto-generated)
```
---
## ⚙️ Setup & Run

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd attendance_system
```

### 2️⃣ Create Database & Tables
Run the setup script to initialize the attendance.db file and create the necessary tables.
```bash
python db_setup.py
```

### 3️⃣ Run the Application
Launch the main menu interface.
```bash
python main.py
```
---
## 📋 Menu Overview
The application is divided into three main logical sections to keep the interface clean:

* **Add / Create** Operations (New Students, New Subjects, Mark Attendance)

* **Activate / Deactivate** Operations (Soft Delete/Restore Students or Subjects)

* **View / Status** Operations (Analytics, Reports, Lists)
---
## 🔒 Data Integrity & Design Decisions
* **Soft Delete:** Students and subjects are deactivated rather than deleted. This ensures that if a student leaves mid-semester, their previous attendance records are not lost and analytics remain accurate.

* **Database Constraints Uniqueness:** Prevents duplicate roll numbers or subject codes.

* **Composite Keys/Unique Constraints:** Prevents marking attendance twice for the same student in the same subject on the same date.

* **Security Parameterized Queries:** All SQL commands use placeholders (?) to prevent SQL Injection attacks.
---
## 🧪 Resetting the Database (Optional)
To clear all data (students, subjects, attendance) while keeping the table schema intact, run:

```bash
python reset_db.py
```
* **Note:** Useful during development and testing phases.
---
## 📌 Future Enhancements
* Export reports to CSV/Excel.

* Role-based access control (Admin vs. Teacher).

* Web interface using Flask or FastAPI.

* Performance optimization using database indexing.

* Migration to PostgreSQL for production environments.
---
## 📝 License
This project is open for learning and personal use.
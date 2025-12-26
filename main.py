from constructive import constructive_menu
from destructive import destructive_menu
from status import status_menu

def main():
    while True:
        print("""
=== Attendance Management System ===
1. Add / Create Operations
2. Activate / Deactivate Operations
3. View / Status Operations
0. Exit
""")
        ch = input("Choice: ").strip()

        if ch == "1":
            constructive_menu()
        elif ch == "2":
            destructive_menu()
        elif ch == "3":
            status_menu()
        elif ch == "0":
            print("Goodbye")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

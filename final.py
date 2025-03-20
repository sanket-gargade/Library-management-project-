





from adminfunctions import Admin
from userfunction import User

def main_menu():
    while True:
        print("\n--- Library Management System ---")
        print("1. Admin Login")
        print("2. User Login")
        print("3. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            admin = Admin()
            if admin.login():  # Login called once
                admin_menu(admin)  # Pass the instance
            else:
                print("Admin login failed, please try again.")
        
        elif choice == 2:
            user = User()
            if user.login():  # Login called once
                user_menu(user)  # Pass the instance
            else:
                print("User login failed, please try again.")

        elif choice == 3:
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

def admin_menu(admin):  # Accept the logged-in admin instance
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Update Book")
        print("6. Issue Book")
        print("7. Return Book")
        print("8. Back to Main Menu")
        
        choice = int(input("Enter your choice: "))
        admin = Admin()
        if choice == 1:
            admin.addbook()
        elif choice == 2:
            admin.display()
        elif choice == 3:
            bookid = int(input("Enter book ID to search: "))
            admin.search(bookid)
        elif choice == 4:
            bookid = int(input("Enter book ID to delete: "))
            admin.delete(bookid)
        elif choice == 5:
            bookid = int(input("Enter book ID to update: "))
            admin.update(bookid)
        elif choice == 6:
            bookid = int(input("Enter book ID to issue: "))
            user_id = input("Enter your user ID: ")
            admin.issuebook(bookid, user_id)
        elif choice == 7:
            bookid = int(input("Enter book ID to return: "))
            user_id = input("Enter your user ID: ")
            admin.returnbook(bookid, user_id)
        elif choice == 8:
            break
        else:
            print("Invalid choice. Please try again.")

def user_menu(user):  # Accept the logged-in user instance
    while True:
        print("\n--- User Menu ---")
        print("1. Issue Book")
        print("2. Return Book")
        print("3. View Book Count")
        print("4. Back to Main Menu")
        
        choice = int(input("Enter your choice: "))
        user = User()
        if choice == 1:
            bookid = int(input("Enter book ID to issue: "))
            user_id = input("Enter your user ID: ")
            user.issuebook(bookid, user_id)
        elif choice == 2:
            bookid = int(input("Enter book ID to return: "))
            user_id = input("Enter your user ID: ")
            user.returnbook(bookid, user_id)
        elif choice == 3:
            user_id = input("Enter your user ID: ")
            action = input("Enter action (view): ")
            user.book_count(user_id, action)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")




if __name__ == "__main__":
    main_menu()

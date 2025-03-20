import os
from datetime  import datetime


class User :
    def __init__(self):
        self.user_credentials = {"user": "userpass"}  # User username:password
        
    def login(self):
        print("User Login")
        username = input("Username: ")
        password = input("Password: ")
        
        if self.user_credentials.get(username) == password:
            print("Login successful!")
            return True
        else:
            print("Invalid credentials.")
            return False
     



    def issuebook(self, bookid, user_id):
     try:
        isfound = False

        
        with open("data.txt", "r") as fp:
            for x in fp:
                sep_text = x.strip().split(",")  
                if str(bookid) == sep_text[0]:  
                    isfound = True

                    
                    if os.path.exists("issuebook.txt"):
                        with open("issuebook.txt", "r") as f1:
                            for x in f1:
                                issued_data = x.strip().split(",")
                                if str(bookid) == issued_data[0]:
                                    print(f"Book with ID {bookid} is already issued.")
                                    return

                    
                    issue_date = datetime.now().strftime("%Y-%m-%d")
                    issue_record = (
                        f"bookid: {sep_text[0]}\n"
                        f"bookname: {sep_text[1]}\n"
                        f"bookauthor: {sep_text[2]}\n"
                        f"user_id: {user_id}\n"
                        f"issue_date: {issue_date}\n"
                    )

                    with open("issuebook.txt", "a") as fi:
                        fi.write(issue_record + "\n")  

                    print(f"Book with ID {bookid} successfully issued to {user_id} on {issue_date}.")
                    return

        if not isfound:
            print(f"Book with ID {bookid} not found in the library.")

     except Exception as e:
        print(f"An error occurred while issuing the book: {e}")


    # def returnbook(self, bookid, user_id):
    #  try:
    #     isfound = False  # Flag to check if the book was found
    #     penalty = 0
    #     allowed_days = 1  # Maximum allowed borrowing period (in days)
    #     penalty_rate = 10  # Penalty per extra day (in currency)
    #     current_date = datetime.now().strftime("%Y-%m-%d")  # Get the current date
    #     updated_records = []  # List to hold updated book records
    #     book_record = []  # Temporary list to hold a single book record

    #     # Read the 'issuebook.txt' file to find the book records
    #     with open("issuebook.txt", "r") as fp:
    #         for x in fp:
    #             collect = x.strip()
    #             if collect:  # Collect lines for a record
    #                 book_record.append(collect)
    #             else:  # Process a complete record when an empty line is found (assuming empty line separates records)
    #                 if book_record:
    #                     # Extract the book details from the record
    #                     record_bookid = book_record[0].split(":")[1].strip()
    #                     record_user_id = book_record[3].split(":")[1].strip()
    #                     issue_date = book_record[4].split(":")[1].strip()
    #                     return_date = next(
    #                         (item.split(":")[1].strip() for item in book_record if "return_date" in item),
    #                         None
    #                     )

    #                     # Check if this is the book being returned by the specified user
    #                     if record_bookid == str(bookid) and record_user_id == user_id:
    #                         isfound = True  # Mark that we found the book to return

    #                         # If the book is already returned, inform the user
    #                         if return_date:
    #                             print(f"Book ID {bookid} has already been returned on {return_date}.")
    #                             updated_records.append("\n".join(book_record) + "\n\n")  # Append the unmodified record
    #                         else:
    #                             # Calculate the penalty if the return is late
    #                             issue_date = datetime.strptime(issue_date, "%Y-%m-%d")
    #                             return_date = datetime.strptime(current_date, "%Y-%m-%d")
    #                             days_diff = (return_date - issue_date).days

    #                             # If the book is returned late, apply a penalty
    #                             if days_diff > allowed_days:
    #                                 penalty = (days_diff - allowed_days) * penalty_rate
    #                                 print(f"\nLate return! Penalty of Rs. {penalty} applied.")
    #                             else:
    #                                 print("No penalty. Book returned on time.")

    #                             # Mark the book as returned by adding the return_date
    #                             book_record.append(f"return_date: {current_date}")
    #                             updated_records.append("\n".join(book_record) + "\n\n")
    #                     else:
    #                         # If it's not the book we are looking for, simply keep the record unchanged
    #                         updated_records.append("\n".join(book_record) + "\n\n")

    #                     book_record = []  # Reset for the next record

    #     # If the book wasn't found, inform the user
    #     if not isfound:
    #         print("No such issued book found for this user.")
    #     else:
    #         # Write the updated records back to the file
    #         with open("issuebook.txt", "w") as fp:
    #             fp.writelines(updated_records)
    #         print("Book returned successfully!")

    #  except Exception as e:
    #     print("An error occurred while returning the book:", e)






    def returnbook(self, bookid, user_id):
     try:
        isfound = False
        penalty = 0
        allowed_days =    1  # Maximum allowed borrowing period
        penalty_rate =    10  # Penalty per extra day
        current_date =    datetime.now().strftime("%Y-%m-%d")
        updated_records = []
        book_record =     []
        
        with open("issuebook.txt", "r") as fp:
            for x in fp:
                collect = x.strip()
                if collect:  # Collect lines for a record
                    book_record.append(collect)
                else:  # Process a complete record when an empty line is found
                    if book_record:
                        bookid = book_record[0].split(":")[1].strip()
                        user_id = book_record[3].split(":")[1].strip()
                        issue_date = book_record[4].split(":")[1].strip()
                        return_date = next(
                            (item.split(":")[1].strip() for item in book_record if "return_date" in item), 
                            None
                        )

                        # Check if this is the book being returned
                        if bookid == str(bookid) and user_id == user_id:
                            isfound = True

                            if return_date:
                                print(f"Book ID {bookid} has already been returned on {return_date}.")
                                updated_records.append("\n".join(book_record) + "\n\n")
                            else:
                                issue_date = datetime.strptime(issue_date, "%Y-%m-%d")
                                return_date = datetime.strptime(current_date, "%Y-%m-%d")
                                days_diff = (return_date - issue_date).days

                                if days_diff > allowed_days:
                                    penalty = (days_diff - allowed_days) * penalty_rate
                                    print ("\n")
                                    print(f"Late return! Penalty of Rs. {penalty} applied.")
                                else:
                                    print("No penalty. Book returned on time.")

                                # Mark the book as returned
                                book_record.append(f"return_date: {current_date}")
                                updated_records.append("\n".join(book_record) + "\n\n")
                        else:
                            updated_records.append("\n".join(book_record) + "\n\n")
                        
                        book_record = []  # Reset for the next record

        if not isfound:
            print("No such issued book found for this user.")
        else:
            with open("issuebook.txt", "w") as fp:
                fp.writelines(updated_records)
            print("Book returned successfully!")

     except Exception as e:
        print("An error occurred while returning the book:", e)



    
    
    
    def book_count(self, user_id, action):
      try:
        file_path = "issuebook.txt"
        issued_count = 0
        returned_count = 0

        if os.path.exists(file_path):
            with open(file_path, "r") as fp:
                book_record = []
                for line in fp:
                    line = line.strip()
                    if line:  # Add lines to the current record
                        book_record.append(line)
                    else:  # Process complete record when an empty line is encountered
                        if book_record:  # Check if the record is not empty
                            # Extract relevant fields from the record
                            record_user_id = book_record[3].split(":")[1].strip()
                            return_date = next(
                                (item.split(":")[1].strip() for item in book_record if "return_date" in item), 
                                None
                            )
                            
                            # Count books for the given user_id
                            if record_user_id == user_id:
                                issued_count += 1
                                if return_date:
                                    returned_count += 1
                            
                        book_record = []  # Reset for the next record

                # Process the last record in the file (if no trailing newline)
                if book_record:
                    record_user_id = book_record[3].split(":")[1].strip()
                    return_date = next(
                        (item.split(":")[1].strip() for item in book_record if "return_date" in item), 
                        None
                    )
                    if record_user_id == user_id:
                        issued_count += 1
                        if return_date:
                            returned_count += 1

        if action == "view":
            print(f"User {user_id} has issued {issued_count} books and returned {returned_count} books.")
        else:
            print("Invalid action for this method. Use 'view' to see book counts.")

      except Exception as e:
        print(f"An error occurred while counting books: {e}")
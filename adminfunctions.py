import os
from datetime  import datetime
from Book import Book

class Admin:

    def __init__(self):
        self.admin_credentials = {"admin": "adminpass"}  # Admin username:password
        
    def login(self):
        print("Admin Login")
        username = input("Username: ")
        password = input("Password: ")
        
        if self.admin_credentials.get(username) == password:
            print("Login successful!")
            return True
        else:
            print("Invalid credentials.")
            return False
    
   

    def addbook(self):
        try:
            bookid = int(input("Enter a bookid: "))
            bookname = input("Enter a bookname: ")
            bookauthor = input("Enter a bookauthor: ")

            s = Book(bookid, bookname, bookauthor) 

            with open("data.txt", "a") as f1:
                f1.write(str(s))
            print("Book added successfully!")

        except Exception as e:
            print("An error occurred while adding the book:", e)




    def display(self):
        try:
            if os.path.exists("data.txt"):
                with open("data.txt", "r") as f1:
                    for x in f1:
                        sep_text = x.split(",")
                        print("bookid : " + sep_text[0])
                        print("bookname : " + sep_text[1])
                        print("bookauthor : " + sep_text[2])
            else:
                print("File not found")

        except Exception as e:
            print("An error occurred while displaying the books:",e)




    def search(self, bookid):
        try:
            with open("data.txt", "r") as fp:
                for x in fp:
                    sep_text = x.split(",")
                    if str(bookid) == sep_text[0]:
                        print("bookid : " + sep_text[0])
                        print("bookname : " + sep_text[1])
                        print("bookauthor : " + sep_text[2])
                        break
                else:
                    print("Book not found")

        except Exception as e:
            print("An error occurred while searching the book: ",e)





    def delete(self, bookid):
        try:
            container = []
            isfound = False    #This means no book with the given bookid was found in the file.
            with open("data.txt", "r") as fp:
                for x in fp:
                    sep_text = x.split(",")
                    if str(bookid) != sep_text[0]:
                        container.append(x)
                    else:
                        isfound = True  #When the book with the given bookid is found,

            if not isfound:     #if the isfound variable is still False. This means no book with the given bookid was found in the file.
                print("Book not found")

            else:     #If isfound is True, meaning the book was found and deleted from the list
                with open("data.txt", "w") as fp:
                    for x in container:
                        fp.write(x)
                print("Book deleted successfully!")

        except Exception as e:
            print("An error occurred while deleting the book:", e)





  



    
    def update(self, bookid):
     try:
        container = []
        isfound = False

        with open("data.txt", "r") as fp:
            for x in fp:
                sep_text = x.strip().split(",")

                if str(bookid) == sep_text[0]:
                    isfound = True
                    while True:
                        print("1. Update the book name")
                        print("2. Update the book author name")
                        print("3. Save and exit")

                        ch = int(input("Enter the choice to perform the task: "))

                        if ch == 1:
                            new_name = input("Enter a new name of the book to update: ")
                            if len(sep_text) > 1:
                                sep_text[1] = new_name
                            else:
                                print("Error: Missing book name field in data.")
                        elif ch == 2:
                            new_author = input("Enter a new name of the book author: ")
                            if len(sep_text) > 2:
                                sep_text[2] = new_author
                            else:
                                print("Error: Missing book author field in data.")
                        elif ch == 3:
                            # Save updated record and exit update loop
                            print("Exiting update menu.")
                            break
                        else:
                            print("Invalid choice, try again.")

                    # After updates, add the updated record back to the container
                    container.append(",".join(sep_text) + "\n")
                else:
                    container.append(x)

        if not isfound:
            print("Book not found")
        else:
            with open("data.txt", "w") as fp:
                fp.writelines(container)

            print("Book updated successfully!")

     except Exception as e:
        print("An error occurred while updating the book:", e)







    # def issuebook(self, bookid, user_id):
    #  try:
    #     isfound = False

        
    #     with open("data.txt", "r") as fp:
    #         for x in fp:
    #             sep_text = x.strip().split(",")  
    #             if str(bookid) == sep_text[0]:  
    #                 isfound = True

                    
    #                 if os.path.exists("issuebook.txt"):  #Checking if the book is already issued,presumably holds the records of all books that have been issued.
    #                     with open("issuebook.txt", "r") as f1:
    #                         for x in f1:
    #                             issued_data = x.strip().split(",")
    #                             if str(bookid) == issued_data[0]:
    #                                 print(f"Book with ID {bookid} is already issued.")
    #                                 return

                    
    #                 issue_date = datetime.now().strftime("%Y-%m-%d")   #Issuing the book
    #                 issue_record = (
    #                     f"bookid: {sep_text[0]}\n"
    #                     f"bookname: {sep_text[1]}\n"
    #                     f"bookauthor: {sep_text[2]}\n"
    #                     f"user_id: {user_id}\n"
    #                     f"issue_date: {issue_date}\n"
    #                 )

    #                 with open("issuebook.txt", "a") as fi:
    #                     fi.write(issue_record + "\n")  

    #                 print(f"Book with ID {bookid} successfully issued to {user_id} on {issue_date}.")
    #                 return

    #     if not isfound:
    #         print(f"Book with ID {bookid} not found in the library.")

    #  except Exception as e:
    #     print(f"An error occurred while issuing the book: {e}")







    # def returnbook(self, bookid, user_id):
    #  try:
    #     isfound = False
    #     penalty = 0
    #     allowed_days =    1  # Maximum allowed borrowing period
    #     penalty_rate =    10  # Penalty per extra day
    #     current_date =    datetime.now().strftime("%Y-%m-%d")
    #     updated_records = []
    #     book_record =     []
        
    #     with open("issuebook.txt", "r") as fp:  #store information about books that have been issued
    #         for x in fp:
    #             collect = x.strip()
    #             if collect:  # Collect lines for a record
    #                 book_record.append(collect)
    #             else:  # Process a complete record when an empty line is found
    #                 if book_record:
    #                     bookid = book_record[0].split(":")[1].strip()
    #                     user_id = book_record[3].split(":")[1].strip()
    #                     issue_date = book_record[4].split(":")[1].strip()
    #                     return_date = next(
    #                         (item.split(":")[1].strip() for item in book_record if "return_date" in item), 
    #                         None   #searches through the book_record to find the return_date
    #                     )          # If there is no return_date in the record, it defaults to None

    #                     # Check if this is the book being returned
    #                     if bookid == str(bookid) and user_id == user_id:
    #                         isfound = True

    #                         if return_date:
    #                             print(f"Book ID {bookid} has already been returned on {return_date}.")
    #                             updated_records.append("\n".join(book_record) + "\n\n")
    #                         else:
    #                             issue_date = datetime.strptime(issue_date, "%Y-%m-%d")
    #                             return_date = datetime.strptime(current_date, "%Y-%m-%d")
    #                             days_diff = (return_date - issue_date).days

    #                             if days_diff > allowed_days:
    #                                 penalty = (days_diff - allowed_days) * penalty_rate
    #                                 print(f"Late return! Penalty of Rs. {penalty} applied.")
    #                             else:
    #                                 print("No penalty. Book returned on time.")

    #                             # Mark the book as returned
    #                             book_record.append(f"return_date: {current_date}")
    #                             updated_records.append("\n".join(book_record) + "\n\n")
    #                     else:
    #                         updated_records.append("\n".join(book_record) + "\n\n")
                        
    #                     book_record = []  # Reset for the next record

    #     if not isfound:
    #         print("No such issued book found for this user.")
    #     else:
    #         with open("issuebook.txt", "w") as fp:
    #             fp.writelines(updated_records)
    #         print("Book returned successfully!")

    #  except Exception as e:
    #     print("An error occurred while returning the book:", e)




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
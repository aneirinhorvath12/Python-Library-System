'''
bookcheckout.py checks out a specific book given a valid book ID and User ID.
If either the user ID or book ID is invalid in some way an error will be returned.

Aneirin Horvath, 5 December 2020
'''


def available_book_update(book_ID,ISBN,Title,Author,purchase_date,member_ID):

    ''' Write to database text file.
        Find the line in the book database text file
        Create a string combining the parameters of this function available_book_update...
        which are generated in the function book_checkout and are passed into
        available_book_update when it is called in book_checkout
        Write this string to the appropriate line in the database text file.'''

    books_database = open("database.txt", "r")
    list_of_lines = books_database.readlines()
    list_of_lines[int(book_ID)-1001] = str(book_ID) + ":" + str(ISBN) + ":" + Title + ":" + Author+ ":" + purchase_date + ":" +str(member_ID) + "\n"
    
    books_database = open("database.txt", "w")
    books_database.writelines(list_of_lines)
    books_database.close


def book_checkout(member_ID, book_ID):

    ''' book_checkout has 2 parameters member_ID and book_ID which are...
    entered by the user in the Tkinter GUI.
    First the function finds the correct book in the book database text file
    If the book is not in the file an error message is sent to the user
    Then the details are are cleaned and split
    If the book is availabe the book detail components are passed into..
    the function available_book_update where the file is updated
    A message is sent to the user to tell them the book is available.
    If the book is unavailable the user is notified of this.'''

    books_database = open("database.txt", "r")
    # Find the correct book in book database
    for book_details in books_database:
        if book_ID == book_details[0:4]:
            # Check if the book is available
            book_details_clean = book_details.strip()
            book_details_split = book_details_clean.split(":")
            if book_details_split[5] == '0':
                # Update database with User ID to checkout the book
                ISBN = book_details_split[1]
                Title = book_details_split[2]
                Author = book_details_split[3]
                purchase_date = book_details_split[4]

                available_book_update(book_ID,ISBN,Title,Author,purchase_date,member_ID)
                books_database.close
                return("Available: File Updated")
            else:
                books_database.close
                return("Currently Unavailable")

    books_database.close
    return("Book ID is Invalid")
    

# Testing
if __name__ == "__main__":
    print(book_checkout('1023', '1002'))


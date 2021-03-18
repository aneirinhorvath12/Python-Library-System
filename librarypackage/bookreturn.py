'''
bookreturn.py gives the user the ability to return a previously checked out book and make it available again
If the book ID is invalid an error message will be returned

Aneirin Horvath, 5 December 2020
'''

def return_book_update(book_ID, ISBN, Title, Author, purchase_date):

    ''' Write to the database text file
        Find the line in the book database text file
        Create a string combining the parameters of this function return_book_update...
        which are generated in the function book_return and are passed into
        return_book_update when it is called in book_return
        Write this string to the appropriate line in the database text file.'''

    book_database = open("database.txt", "r")
    list_of_lines = book_database.readlines()
    list_of_lines[int(book_ID)-1001] = str(book_ID) + ":" + str(ISBN) + ":" + Title + ":" + Author+ ":" + purchase_date + ":" + "0" + "\n"

    book_database= open("database.txt", "w")
    book_database.writelines(list_of_lines)
    book_database.close


def book_return(book_ID):
    ''' book_return has 1 parameter book_ID which is entered by the user in the Tkinter GUI
        First the function finds the correct book in the book database text file
        If the book is not in the file an error message is sent to the user
        Then the details are are cleaned and split
        If the book is already returned an error message will be sent to the user
        Otherwise the book detail components are passed into the function return_book_update
        where the file is updated
        A message is sent to the user to tell them the book has been returned sucessfully '''
    
    books_database = open("database.txt", "r")
    # Find the correct book in book database
    for book_details in books_database:
        if book_ID == book_details[0:4]:
            # Check if the book is available
            book_details_clean = book_details.strip()
            book_details_split = book_details_clean.split(":")
            if book_details_split[5] == '0':
                books_database.close
                return("ERROR: THIS BOOK HAS ALREADY BEEN RETURNED")
            else:
                # Update database to return the book 
                ISBN = book_details_split[1]
                Title = book_details_split[2]
                Author = book_details_split[3]
                purchase_date = book_details_split[4]

                return_book_update(book_ID,ISBN,Title,Author, purchase_date)
                books_database.close
                return("Book Successfully Returned")
    
    books_database.close
    return("Book ID is Invalid")

# Testing
if __name__ == "__main__":
    print(book_return('1023'))

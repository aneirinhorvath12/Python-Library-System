'''
booksearch.py searches for a book title and returns to the user all the information about...
any copies of that book in the library

Aneirin Horvath, 3 December 2020
'''


def book_search(search_book_name):
    ''' book_search has 1 parameter search_book_name which is inputed
        by the user in the Tkinter GUI
        It then checks each line in the book database for the book title
        When it is found, the details of the book are cleaned and appended to
        the list books.
        Once all books in the file of that title are found the list containing the information
        is returned.
    '''
    books = []
    book_database = open("database.txt", "r")
    for book_details in book_database:
        if search_book_name in book_details:
            book_details_clean = book_details.strip()
            book_details_split = book_details_clean.split(':')
            books.append(book_details_split)     
    book_database.close
    return(books)

# Testing
if __name__ == "__main__":
    print(book_search('QED'))

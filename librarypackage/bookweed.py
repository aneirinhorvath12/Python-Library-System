'''
bookweed.py returns the number of times a book title inputted...
by the user in the Tkinter GUI, has been checked out,
this will help the user decide which book titles are popular...
and which ones to remove.

Aneirin Horvath, 15 December 2020
'''


def weeding(book_name):
    ''' The function weeding has 1 parameter, book_name...
        inputted by the user in the Tkinter GUI.
        Weeding first finds the ID's of any copies of that book and adds
        them to a list of the book ID's.
        It then loops through entries into the logfile and increments a
        counter whenever the ID of that book title is found.
        Weeding returns the number of times the copies of that book
        have been checked out '''
    book_ID = []
    book_database = open("database.txt", "r")
    # Find the ID's of any copies of this book
    for book_details in book_database:
        if book_name in book_details:
            book_details_clean = book_details.strip()
            book_details_strip = book_details_clean.split(':')
            book_ID.append(book_details_strip[0])
    book_database.close()
    number_of_checkouts = 0
    logfile = open("logfile.txt", "r")
    # Find entries into the log file containing the book ID's 
    for log_entry in logfile:
        for ID in book_ID:
            if ID == log_entry[:4]:
                number_of_checkouts += 1
    logfile.close()
    return number_of_checkouts

# Testing
if __name__ == "__main__":
    print(weeding('QED'))

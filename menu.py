'''
menu.py imports the functions from each module in the library package
it combines their functionality into a Tkinter GUI

Aneirin Horvath, 16 December 2020
'''
print("hello World")
import sys
sys.path.append('librarypackage')

# Import modules
from tkinter import *
from booksearch import *
from bookcheckout import *
from bookreturn import *
from bookweed import *


# Tkinter
window = Tk()
window.title("Aneirin Horvath Library")
window.geometry("900x400")

# Define Functions
def book_search_call(book_name):
    command_output.delete('1.0', END)
    # Check the book name is a valid entry
    if len(book_name) > 0:
        response = book_search(book_name)
        command_output.insert(END, response)
    else:
        command_output.insert(END, "Please enter a valid book name")

def book_checkout_call(member_ID,book_ID):
    command_output.delete('1.0', END)
    # Check the User ID is 4 digits and return an error message if not
    if len(member_ID) == 4 and member_ID.isdigit():
        response = book_checkout(member_ID,book_ID)
        command_output.insert(END, response)
    else:
        command_output.insert(END, "Invalid Member ID")

def book_return_call(book_ID):
    command_output.delete('1.0', END)
    response = book_return(book_ID)
    command_output.insert(END, response)

def weeding_call(book_name):
    command_output.delete('1.0', END)
    response = weeding(book_name)
    command_output.insert(END, response)

# Create GUI components
lbl_Book_ID = Label(window, text = "Book ID:")
lbl_Book_Name = Label(window, text = "Book Name:")
lbl_User_ID = Label(window, text = "User ID:")

txt_Book_ID = Entry(window, width = 10)
txt_Book_Name = Entry(window, width = 20)
txt_User_ID = Entry(window, width = 10)

command_output = Text(window, height = 10,  width = 50) 

btn_book_search = Button(window, text = "Book Search",
                         command =lambda:book_search_call(txt_Book_Name.get()) )
btn_book_checkout = Button(window, text = "Book Checkout",
                           command =lambda:book_checkout_call(txt_User_ID.get(), txt_Book_ID.get()))
btn_book_return = Button(window, text = "Book Return",
                         command = lambda:book_return_call(txt_Book_ID.get()))
btn_weeding = Button(window, text = "Weeding",
                     command = lambda: weeding_call(txt_Book_Name.get()))




# Define locations of components
btn_book_search.grid(column = 1, row = 4)
btn_book_checkout.grid(column = 2, row = 4)
btn_book_return.grid(column = 3, row = 4)
btn_weeding.grid(column = 4, row = 4)
lbl_Book_ID.grid(column = 1, row = 0)
lbl_Book_Name.grid(column = 1, row = 1)
lbl_User_ID.grid(column = 1, row = 2)
txt_Book_ID.grid(column = 2, row = 0)
txt_Book_Name.grid(column = 2, row = 1)
txt_User_ID.grid(column = 2, row = 2)
command_output.grid(column = 8, row = 1)

window.mainloop()

# Import the required libraries
from tkinter import *
from tkinter import messagebox

# Define a function to add numbers
def add_numbers():
    try:  
        result = float(num1.get()) + float(num2.get())
        result = round(result, 4)
        label4.config(text = result)
    except:  
        messagebox.showerror('Error Encountered', 'Error: Please enter a valid input!')

# Define a function to subtract numbers
def subtract_numbers():
    try:
        result = float(num1.get()) - float(num2.get())
        result = round(result, 4)
        label4.config(text = result)
    except:
        messagebox.showerror('Error Encountered', 'Error: Please enter a valid input!')

# Define a function to multiply numbers
    # try
    # catch

# Define a function to divide numbers
    # try
    # catch

# Define a function to clear the content of textbox 1 and textbox 2


window = Tk()  # Create an instance of tkinter frame or window
window.title("Python Simple Calculator")  # Title of the Window

# Create a label for first number
label1 = Label(window, text = "First Number: ")
label1.grid(row = 0, column = 1)

# Create a textbox for first number
num1 = Entry(window)
num1.grid(row = 0, column = 2)

# Create a label for second number
label2 = Label(window, text = "Second Number: ")
label2.grid(row = 1, column = 1)

# Create a textbox for second number
num2 = Entry(window)
num2.grid(row = 1, column = 2)

# Create label for Result
label3 = Label(window, text = "Result: ")
label3.grid(row = 2, column = 1)

# Display result
label4 = Label(window, text = "")
label4.grid(row = 2, column = 2)
               
# Create a button for addition of first and second number
# Create a button for subtraction of first and second number
# Create a button for multiplication of first and second number
# Create a button for division of first and second number
# Create a button for clearing the content of textbox 1 and textbox 2
# Create an exit button

# mainloop
window.mainloop()
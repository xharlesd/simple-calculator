# Bernido, Charles David P. | BSCPE 1-5
# Assignment 5 


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
def multiply_numbers():
    try: 
        result = float(num1.get()) * float(num2.get())
        result = round(result, 4)
        label4.config(text = result)
    except:
        messagebox.showerror('Error Encountered', 'Error: Please enter a valid input!')

# Define a function to divide numbers
def division_numbers():
    try:
        result = float(num1.get()) / float(num2.get())
        result = round(result, 4)
        label4.config(text = result)
    except ZeroDivisionError:
        messagebox.showerror('Error Encountered', 'Error: Dividing by zero is not allowed!')
    except:
        messagebox.showerror('Error Encountered', 'Error: Please enter a valid input!')

# Define a function to clear the content of textbox 1 and textbox 2
def clear_textbox():
    num1.delete(0,END)
    num2.delete(0,END)

def exit_button():
    messagebox.askquestion("askquestion", "Are you sure?")
    window.quit()

window = Tk()  # Create an instance of tkinter frame or window
window.title("Python Simple Calculator")  # Title of the Window
window.config(bg = "#D8F9FF")

# Create a label for first number
label1 = Label(window, text = "1st Number: ", font=("Calibri",16,"bold"), bg = "#D8F9FF", fg = "#0B0B45")
label1.grid(row = 0, column = 1, padx = 10, pady = 10)

# Create a textbox for first number
num1 = Entry(window, font=("Arial",13), fg = "#0B0B45", justify = CENTER)
num1.grid(row = 0, column = 2)

# Create a label for second number
label2 = Label(window, text = "2nd Number: ", font=("Calibri",16,"bold"), bg = "#D8F9FF", fg = "#0B0B45")
label2.grid(row = 1, column = 1, padx = 10)

# Create a textbox for second number
num2 = Entry(window, font=("Arial",13), fg = "#0B0B45", justify = CENTER)
num2.grid(row = 1, column = 2)

# Create label for Result
label3 = Label(window, text = "Result: ", font=("Helvetica",14,"bold"), bg = "#D8F9FF", fg = "#0B0B45")
label3.grid(row = 2, column = 1, padx = 10, pady = 10)

# Display result
label4 = Label(window, text = "", font=("Arial",14,"bold"), bg = "#D8F9FF", fg = "#0B0B45", justify = CENTER)
label4.grid(row = 2, column = 2)
               
# Create a button for addition of first and second number
button1 = Button(window, text = "Add", width = 10, font=("Georgia",13,"bold"), bg = "#ffffe0", command = add_numbers)
button1.grid(row = 3, column = 1, padx = 15, pady = 5)

# Create a button for subtraction of first and second number
button2 = Button(window, text = "Subtract", width = 10, font=("Georgia",13,"bold"), bg = "#ffffe0", command = subtract_numbers)
button2.grid(row = 3, column = 2, padx = 5, pady = 5)

# Create a button for multiplication of first and second number
button3 = Button(window, text = "Multiply", width = 10, font=("Georgia",13,"bold"), bg = "#ffffe0", command = multiply_numbers)
button3.grid(row = 4, column = 1, padx = 5, pady = 5)

# Create a button for division of first and second number
button4 = Button(window, text = "Divide", width = 10, font=("Georgia",13,"bold"), bg = "#ffffe0", command = division_numbers)
button4.grid(row = 4, column = 2, padx = 5, pady = 5)

# Create a button for clearing the content of textbox 1 and textbox 2
button5 = Button(window, text = "Clear", width = 10, font=("Calibri",12,"bold"), bg = "#90EE90", command = clear_textbox)
button5.grid(row = 5, column = 1, padx = 5, pady = 20)

# Create an exit button
button6 = Button(window, text = "Exit", width = 10, font=("Calibri",12,"bold"), bg = "#90EE90", command = exit_button)
button6.grid(row = 5, column = 2, padx = 5, pady = 20)

# mainloop
window.mainloop()
from tkinter import * 
from fpdf import FPDF

# Create the main window object
root = Tk()
root.title('Invoice Generator')  # Set the title of the window

# Dictionary storing medicines and their prices
medicines = {
    'Medicine A': 10,  # Medicine A costs 10 units
    'Medicine B': 20,  # Medicine B costs 20 units
    'Medicine C': 15,  # Medicine C costs 15 units
    'Medicine D': 25   # Medicine D costs 25 units
}

invoice_items = []  # List to store selected medicines, quantities, and totals


# Function to add selected medicine and quantity to the invoice
def add_medicine():
    selected_medicine = medicine_listbox.get(ANCHOR)  # Get the selected medicine from the listbox
    quantity = int(quantity_entry.get())  # Get the quantity entered by the user and convert it to an integer
    price = medicines[selected_medicine]  # Get the price of the selected medicine from the dictionary
    item_total = price * quantity  # Calculate the total price for the selected medicine
    invoice_items.append((selected_medicine, quantity, item_total))  # Append the selected medicine, quantity, and total to the invoice list
    total_amount_entry.delete(0, END)  # Clear the total amount entry field
    total_amount_entry.insert(END, str(calculate_total()))  # Insert the updated total amount
    update_invoice_text()  # Update the invoice display text


# Function to calculate the total amount for all medicines in the invoice
def calculate_total():
    total = 0.0  # Initialize total amount to 0
    for item in invoice_items:  # Iterate over each item in the invoice
        total = total + item[2]  # Add the total price of each item to the overall total
    return total  # Return the calculated total


# Function to update the invoice display in the text widget
def update_invoice_text():
    invoice_text.delete(1.0, END)  # Clear the text widget
    for item in invoice_items:  # Iterate over each item in the invoice
        invoice_text.insert(END, f"Medicine: {item[0]}, Quantity: {item[1]}, Total: {item[2]}\n")  # Insert the medicine details in the text widget


# Function to generate the invoice as a PDF
def generate_invoice():
    customer_name = customer_entry.get()  # Get the customer name entered by the user

    pdf = FPDF()  # Create a PDF object
    pdf.add_page()  # Add a page to the PDF
    pdf.set_font('Helvetica', size=12)  # Set the font to Helvetica with a size of 12
    pdf.cell(0, 10, txt='Invoice', ln=True, align='C')  # Add the title "Invoice" centered at the top of the page
    pdf.cell(0, 10, txt='Customer: ' + customer_name, ln=True, align='L')  # Add the customer name to the PDF
    pdf.cell(0, 10, txt='', ln=True)  # Add an empty line for spacing

    for item in invoice_items:  # Iterate over each item in the invoice
        medicine_name, quantity, item_total = item  # Unpack the item's details
        pdf.cell(0, 10, txt=f'Medicine: {medicine_name}, Quantity: {quantity}, Total: {item_total}', ln=True, align='L')  # Add the medicine details to the PDF

    pdf.cell(0, 10, txt='Total Amount: ' + str(calculate_total()), ln=True, align='L')  # Add the total amount to the PDF

    pdf.output('invoice.pdf')  # Save the PDF as "invoice.pdf"


# GUI setup for medicine selection
medicine_label = Label(root, text='Medicine: ')  # Label for the medicine listbox
medicine_label.pack()  # Add the label to the window

medicine_listbox = Listbox(root, selectmode=SINGLE)  # Create a listbox to display the medicines
for medicine in medicines:  # Iterate over each medicine in the dictionary
    medicine_listbox.insert(END, medicine)  # Add each medicine to the listbox
medicine_listbox.pack()  # Add the listbox to the window

# GUI setup for quantity entry
quantity_label = Label(root, text='Quantity')  # Label for the quantity entry field
quantity_label.pack()  # Add the label to the window

quantity_entry = Entry(root)  # Create an entry field for the user to input the quantity
quantity_entry.pack()  # Add the entry field to the window

# Button to add the selected medicine and quantity to the invoice
add_button = Button(root, text='Add Medicine', command=add_medicine)  # Button to add the selected medicine to the invoice
add_button.pack()  # Add the button to the window

# GUI setup for displaying the total amount
total_amount_label = Label(root, text='Total Amount')  # Label for the total amount entry field
total_amount_label.pack()  # Add the label to the window

total_amount_entry = Entry(root)  # Create an entry field to display the total amount
total_amount_entry.pack()  # Add the entry field to the window

# GUI setup for customer name entry
customer_label = Label(root, text='Customer Name: ')  # Label for the customer name entry field
customer_label.pack()  # Add the label to the window

customer_entry = Entry(root)  # Create an entry field for the user to input the customer name
customer_entry.pack()  # Add the entry field to the window

# Button to generate the invoice as a PDF
generate_button = Button(root, text='Generate Invoice', command=generate_invoice)  # Button to generate the invoice
generate_button.pack()  # Add the button to the window

# Text widget to display the invoice details
invoice_text = Text(root, height=10, width=50)  # Create a text widget to display the invoice details
invoice_text.pack()  # Add the text widget to the window

# Start the main event loop of the application
root.mainloop()  # Keep the application window open

Invoice Generator Application

Description

This is a simple Python-based Invoice Generator using the Tkinter library for the GUI and FPDF for generating PDF invoices. The program allows users to select medicines from a predefined list, enter the quantity, and automatically calculate the total cost. Users can also generate a PDF invoice for the selected items.

                -----------------------------------------------------------------------------------------------------------
Features

    1. Select medicines from a predefined list.
    2. Enter quantity for each selected medicine.
    3. Display the total cost of the selected medicines.
    4. Generate a PDF invoice that includes the customer's name, selected medicines, their quantities, and the total amount.

                -----------------------------------------------------------------------------------------------------------
Prerequisites

    Before running the application, ensure you have the following installed:

        1. Python 3.x
        2. Tkinter (This comes pre-installed with Python)
        3. FPDF Library
        You can install the FPDF library using pip if you haven't already:
            bash: pip install fpdf
How to Use
1. Select Medicine:
    Choose a medicine from the list displayed in the Listbox widget.
2. Enter Quantity:
    Type the desired quantity in the Entry widget next to "Quantity".
3. Add Medicine:
    Click the "Add Medicine" button to add the selected medicine and quantity to the invoice.
    The total amount will be updated automatically, and the selected items will be displayed in the Text widget.
4. Generate Invoice:
    Enter the customer’s name in the Entry widget next to "Customer Name".
    Click the "Generate Invoice" button to create a PDF invoice.
    The invoice will be saved as invoice.pdf in the current working directory.

                -----------------------------------------------------------------------------------------------------------
Code Overview

1. add_medicine():
    Adds the selected medicine and quantity to the invoice_items list and updates the total amount.
2. calculate_total():
    Calculates the total cost by summing up the total price for each selected medicine.
3. update_invoice_text():
    Updates the displayed list of selected medicines, quantities, and totals in the text box.
4. generate_invoice():
    Generates a PDF invoice with customer details, medicine list, and the total cost.

                -----------------------------------------------------------------------------------------------------------
Files

1. invoice.py: This is the main Python file that contains the code for the application.

                -----------------------------------------------------------------------------------------------------------
Output

1. invoice.pdf: The generated PDF file containing the invoice details.

                -----------------------------------------------------------------------------------------------------------
Example of Generated Invoice

Invoice
Customer: John Doe

Medicine: Medicine A, Quantity: 2, Total: 20
Medicine: Medicine C, Quantity: 1, Total: 15

Total Amount: 35

                -----------------------------------------------------------------------------------------------------------
Future Enhancements

1. Allow users to remove medicines from the invoice.
2. Add more flexible pricing or discount options.
3. Improve the UI with additional styling and validation.# Invoice-Generator-Application

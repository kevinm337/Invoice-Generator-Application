from tkinter import * 
from fpdf import FPDF



root=Tk()
root.title('Invoice Generator')

medicines={
    'Medicine A':10,
    'Medicine B':20,
    'Medicine C':15,
    'Medicine D':25
}

invoice_items=[]


def add_medicine():
    selected_medicine=medicine_listbox.get(ANCHOR)
    quantity=int(quantity_entry.get())
    price=medicines[selected_medicine]
    item_total=price*quantity
    invoice_items.append((selected_medicine,quantity,item_total))
    total_amount_entry.delete(0,END)
    total_amount_entry.insert(END,str(calculate_total()))
    update_invoice_text()
    

def calculate_total():
    total=0.0
    for item in invoice_items:
        total=total + item[2]
    return total


def update_invoice_text():
    invoice_text.delete(1.0,END)
    for item in invoice_items:
        invoice_text.insert(END,f"Medicine: {item[0]}, Quantity: {item[1]}, Total: {item[2]}\n")

def generate_invoice():
    customer_name = customer_entry.get()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Helvetica', size=12)
    pdf.cell(0, 10, txt='Invoice', ln=True, align='C')
    pdf.cell(0, 10, txt='Customer: ' + customer_name, ln=True, align='L')
    pdf.cell(0, 10, txt='', ln=True)  # Empty line for spacing

    for item in invoice_items:
        medicine_name, quantity, item_total = item
        pdf.cell(0, 10, txt=f'Medicine: {medicine_name}, Quantity: {quantity}, Total: {item_total}', ln=True, align='L')

    pdf.cell(0, 10, txt='Total Amount: ' + str(calculate_total()), ln=True, align='L')

    pdf.output('invoice.pdf')




medicine_label=Label(root,text='Medicine: ')
medicine_label.pack()

medicine_listbox=Listbox(root,selectmode=SINGLE)
for medicine in medicines:
    medicine_listbox.insert(END,medicine)
medicine_listbox.pack()

quantity_label=Label(root,text='Quantity')
quantity_label.pack( )
quantity_entry=Entry(root)
quantity_entry.pack()

add_button=Button(root,text='Add Medicine',command=add_medicine)
add_button.pack()

total_amount_label=Label(root,text='Total Amount')
total_amount_label.pack()

total_amount_entry=Entry(root)
total_amount_entry.pack()

customer_label=Label(root,text='Customer Name: ')
customer_label.pack()
customer_entry=Entry(root)
customer_entry.pack()

generate_button=Button(root,text='Generate Invoice',command=generate_invoice)
generate_button.pack()

invoice_text=Text(root,height=10,width=50)
invoice_text.pack()


root.mainloop()
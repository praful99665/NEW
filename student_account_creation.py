first_name = doc.first_name
middle_name = doc.middle_name
last_name = doc.last_name
N_name = doc.name
# frappe.msgprint(str(lead))
last_five_digits = N_name[-5:]

# Convert the last 5 digits to an integer (if needed)
Id = int(last_five_digits)

# frappe.msgprint(f"Last 5 digits: {last_five_digits}, Converted Id: {Id}")


# Concatenate the names to form the full name
full_name = " ".join([name for name in [first_name, middle_name, last_name] if name])


existing_account = frappe.get_all("Account", filters={"account_name":full_name+" - "+str(Id)})

if existing_account:
    frappe.msgprint("Account already exists.")
    doc.custom_student_account = existing_account[0].name
else:
#     # Create a new account with the student's name
    new_account = frappe.new_doc("Account")
    new_account.account_name = full_name+" - "+str(Id)
    new_account.parent_account = "Accounts Receivable - W"
    new_account.account_type = "Receivable"
    new_account.insert()
    
    frappe.msgprint("New account created successfully.")
    doc.custom_student_account = new_account.name

frappe.msgprint(str(doc.custom_student_account))
# ....................................................


# .........................................

# student_name = doc.custom_full_name

# # Check if an account with the same name already exists
# existing_account = frappe.get_all("Account", filters={"account_name": student_name})

# if existing_account:
#     frappe.msgprint("Account already exists.")
#     doc.custom_student_account = existing_account[0].name
# else:
#     # Create a new account with the student's name
#     new_account = frappe.new_doc("Account")
#     new_account.account_name = student_name
#     new_account.parent_account = "Accounts Receivable - W"
#     new_account.account_type = "Receivable"
#     new_account.insert()
    
#     frappe.msgprint("New account created successfully.")
#     doc.custom_student_account = new_account.name

# frappe.msgprint(str(doc.custom_student_account))






# ......................
Student_Account = None
std = doc.student
student = doc.student_name
structure = doc.fee_structure
prog = doc.program
batch = doc.custom_batch
year = doc.academic_year
std_account = doc.receivable_account
# frappe.msgprint(str(std_account)) 

Y = frappe.get_doc("Student",std)
# frappe.msgprint(str(Y.custom_student_account))

if Y:
    frappe.msgprint(str(Y.custom_student_account))
    Student_Account = Y.custom_student_account
    doc.receivable_account= Student_Account


# stud_fees = frappe.get_list('Fees',filters={'student_name':student,'program':prog,'custom_batch':batch,'academic_year':year,'receivable_account':Student_Account})
stud_fees = frappe.get_list('Fees',filters={'student_name':student,'receivable_account':Student_Account})

frappe.msgprint(str(len(stud_fees)))

if len(stud_fees) > 0:
    frappe.throw("Fees already exist for this student. Document submission aborted.")
    frappe.validate = False
    












# ...............................................
# Student_Account = None
# student = doc.student_name
# structure = doc.fee_structure
# prog = doc.program
# batch = doc.custom_batch
# year = doc.academic_year
# std_account = doc.receivable_account
# # frappe.msgprint(str(std_account))

# Y = frappe.get_list("Student",filters ={"student_name":student})
# # frappe.msgprint(str(Y))
# for i in Y:
#     # frappe.msgprint(str(i.name))
#     xx = frappe.get_doc('Student' ,i.name)
#     frappe.msgprint(str(xx.custom_student_account))

#     if xx:
#         frappe.msgprint(str(xx.custom_student_account))
#         Student_Account = xx.custom_student_account
#         doc.receivable_account=xx.custom_student_account


# stud_fees = frappe.get_list('Fees',filters={'student_name':student,'program':prog,'custom_batch':batch,'academic_year':year,'receivable_account':Student_Account})
# frappe.msgprint(str(len(stud_fees)))

# if len(stud_fees) > 0:
#     frappe.throw("Fees already exist for this student. Document submission aborted.")
#     frappe.validate = False
    


    



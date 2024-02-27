tot_unpaid_stud = []
child_table_data = []
new_group = None
M = None
N = None
tt_mnt = 0;
studname = []
stud_accounts = []
studentname = doc.student_name
prog = doc.program
batch = doc.custom_batch
student_account = doc.receivable_account
frappe.msgprint(str(studentname))
frappe.msgprint(str(prog))
frappe.msgprint(str(batch))

group= frappe.get_list('Student Group',filters={'batch':batch})
# frappe.msgprint(str(group))
for i in group:
    # frappe.msgprint(str(i.name))
    N = i.name
    
T= frappe.get_list('Total Unpaid Students',filters={'student_groups':N})

if len(T)==1:
    # frappe.msgprint(str('doc found'))
    for j in T:
        # frappe.msgprint(str(j.name))
        M = j.name
            
            
    student_doc = frappe.get_doc('Total Unpaid Students',M)
    for i in student_doc.custom_unpaid_students:
        studname.append(i.studentnam_e)
        stud_accounts.append(i.accounts)
    if student_account not in stud_accounts:
        g_total= doc.grand_total
        outstanding= doc.outstanding_amount
        paid_amount1= g_total-outstanding
                    
        new_row = student_doc.append('custom_unpaid_students', {})
        new_row.studentnam_e = studentname
        new_row.course_fee = g_total
        new_row.paid_amount = paid_amount1
        new_row.amounts = outstanding
        new_row.accounts = student_account
        new_row.save()
        frappe.msgprint(str('Row Added Successfully'))
        
        
        
    for k in student_doc.custom_unpaid_students:
        tt_mnt = tt_mnt + k.amounts
    student_doc.total_outstanding = tt_mnt;
    student_doc.save()
        
        
    # tt_mnt = student_doc.total_outstanding
    # frappe.msgprint(str(tt_mnt))
    # tt_mnt = tt_mnt + outstanding
    # student_doc.total_outstanding = tt_mnt
    
        
        
    # else:
    #     frappe.msgprint(str('already exsist'))
    #     for k in student_doc.custom_unpaid_students:
    #         frappe.msgprint(k.studentnam_e)
    #         if k.studentnam_e == studentname:
    #             g_total= doc.grand_total
    #             outstanding= doc.outstanding_amount
    #             paid_amount1= g_total-outstanding
    #             k.studentnam_e= studentname
    #             k.paid_amount = paid_amount1
    #             k.course_fee = g_total
    #             k.amounts = outstanding
    #             k.save()
    #     frappe.msgprint('Row updated successfully.')
        
        
        









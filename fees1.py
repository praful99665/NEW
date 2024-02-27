# ......................
tot_unpaid_stud = []
child_table_data = []
new_group = None
tt_mnt = 0;
studentname = doc.student_name
prog = doc.program
batch = doc.custom_batch
account_name = doc.receivable_account 
frappe.msgprint(str(account_name))
# frappe.msgprint(str(studentname))
# frappe.msgprint(str(prog))
# frappe.msgprint(str(batch))

group= frappe.get_list('Student Group',filters={'batch':batch})
# frappe.msgprint(str(group))
for i in group:
    # frappe.msgprint(str(i.name))
    new_group = i.name
    
    T= frappe.get_list('Total Unpaid Students',filters={'student_groups':i.name})
    # frappe.msgprint(str(T))
    # frappe.msgprint(str(len(T)))
    if len(T)==0:
        frappe.msgprint(str('No document found'))
        
        # Create a new document
        new_unpaid_doc = frappe.new_doc('Total Unpaid Students')
        new_unpaid_doc.student_groups = i.name
        new_unpaid_doc.program = prog
        new_unpaid_doc.st_grp = i.name
        new_unpaid_doc.save()
        
        new_unpaid_doc1= frappe.get_doc('Total Unpaid Students',new_unpaid_doc.name)
        # frappe.msgprint(str(new_unpaid_doc))
    
        g_total= doc.grand_total
        outstanding= doc.outstanding_amount
        paid_amount1= g_total-outstanding    
    
        
        if not new_unpaid_doc1.custom_unpaid_students:
        # Add values to the child table for the first time
            new_row = new_unpaid_doc1.append('custom_unpaid_students', {})
            new_row.studentnam_e = studentname
            new_row.paid_amount = paid_amount1 # Replace with the desired amount
            new_row.course_fee = g_total
            new_row.amounts = outstanding
            new_row.accounts = account_name
            new_row.insert()
        
            frappe.msgprint(str('New document created successfully and Row updated successfully'))
            
            
                
        for k in new_unpaid_doc1.custom_unpaid_students:
            tt_mnt = tt_mnt + k.amounts
            new_unpaid_doc1.total_outstanding = tt_mnt;
            new_unpaid_doc1.save()
            
        # else:
        #     frappe.msgprint('doc already exsist')
            
    # else:
        
    #     frappe.msgprint(str('Document found'))

    #     for j in T:
    #         unpaid_doc= frappe.get_doc('Total Unpaid Students',j.name)
    #         frappe.msgprint(str(unpaid_doc))
    #         for k in unpaid_doc.custom_unpaid_students:
    #             frappe.msgprint(k.studentnam_e)
    #             if k.studentnam_e == studentname:
    #                 g_total= doc.grand_total
    #                 outstanding= doc.outstanding_amount
    #                 paid_amount1= g_total-outstanding
    #                 k.studentnam_e= studentname
    #                 k.paid_amount = paid_amount1
    #                 k.course_fee = g_total
    #                 k.amounts = outstanding
    #         unpaid_doc.save()
    #         frappe.msgprint('Row updated successfully.')
# ................................................................................   


        

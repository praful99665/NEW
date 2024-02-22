# .............
partyname = doc.party_name
references = doc.references
party_acc= doc.paid_from
R_name = None
group = None
total_amount=0
total_paid_mnt=0
# frappe.msgprint(str(partyname))
# frappe.msgprint(str(references))
if references:
    for i in references:
        # frappe.msgprint(str(i.reference_name))
        R_name = i.reference_name
    fees= frappe.get_doc('Fees',R_name)
    # frappe.msgprint(str(fees.student_name))
    
    # frappe.msgprint(str(fees.outstanding_amount))
    outstanding_amount= fees.outstanding_amount
    
    frappe.msgprint(str(fees.grand_total))
    total = fees.grand_total
    
    paid_amount =total - outstanding_amount
    # frappe.msgprint(str(fees.custom_batch))
    
    
    groups= frappe.get_list('Student Group',filters={'batch':fees.custom_batch})
    # frappe.msgprint(str(groups))
    for j in groups:
        group=j.name
    # frappe.msgprint(str(group))
    unpaid_doc= frappe.get_list('Total Unpaid Students',filters={'student_groups':group})
    # frappe.msgprint(str(unpaid_doc))
    new_unpaid_doc=frappe.get_doc('Total Unpaid Students',unpaid_doc)
    # frappe.msgprint(str(new_unpaid_doc))
    # frappe.msgprint(str(new_unpaid_doc.total_outstanding))
    
    for k in new_unpaid_doc.custom_unpaid_students:
        # frappe.msgprint(str(k.studentnam_e))
        if k.accounts == party_acc:
            k.paid_amount = paid_amount
            k.course_fee = total
            k.amounts = outstanding_amount
            k.accounts = party_acc
            k.save()
            frappe.msgprint('Row updated successfully.')
        
    for k in new_unpaid_doc.custom_unpaid_students:
        # frappe.msgprint(str(k.amounts))
        total_amount  = total_amount+k.amounts
        total_paid_mnt = total_paid_mnt+k.paid_amount
    frappe.msgprint(str(total_amount))
    frappe.msgprint(str(total_paid_mnt))
    new_unpaid_doc.total_outstanding = total_amount
    new_unpaid_doc.total_cullected = total_paid_mnt
    
        
    new_unpaid_doc.save()
# ....................................//
    # if partyname not in k.studentnam_e:
    #     new_row = new_unpaid_doc.append('custom_unpaid_students', {})
    #     new_row.studentnam_e = partyname
    #     new_row.course_fee = total
    #     new_row.paid_amount = paid_amount
    #     new_row.amounts = outstanding_amount
    #     new_row.save()
    #     frappe.msgprint(str('Row Added Successfully'))


    















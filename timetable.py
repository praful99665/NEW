# .
group = doc.student_group
course = doc.course
instructor = doc.instructor_name
sheduled_date = doc.schedule_date
course = doc.course
RooM = doc.room
cs_list = []
cs_details = []
cs= frappe.get_list("Course Schedule",filters = {'student_group':group})
frappe.msgprint(str(cs))


for  i in cs:
    # frappe.msgprint(str(i.name))
    new_cs= frappe.get_doc("Course Schedule",i.name)

    cs_details.append({'instructor_name': new_cs.instructor_name,
                        'schedule_date': new_cs.schedule_date,
                        'from_time': new_cs.from_time,
                        'to_time': new_cs.to_time,
                        'room': new_cs.room})
    


sorted_cs_list = sorted(cs_details, key=lambda x: x['schedule_date'])
# for i in sorted_cs_list:
#     frappe.msgprint(str(i))

batches = frappe.get_doc('Student Group',group)
Batch = batches.batch
Student_group = frappe.get_list("Student Time Table",filters={"st_gp":group,"cours":course})
frappe.msgprint(str(len(Student_group)))
if len(Student_group) == 0:
    frappe.msgprint(str('No Doc Found'))


    new_std_gp = frappe.new_doc('Student Time Table')
    new_std_gp.std_grp = group
    new_std_gp.batch = Batch
    new_std_gp.cours = course
    new_std_gp.st_gp = group
    new_std_gp.save()
    frappe.msgprint(str('Created New Doc'))

    current_doc= frappe.get_doc("Student Time Table",group)

    if not current_doc.table_1:
        for i in sorted_cs_list:
            new_row = current_doc.append('table_1', {})
            new_row.instructor_name = i['instructor_name']
            new_row.schedule_date = i['schedule_date'] 
            new_row.room = i['room']
            new_row.from_time = i['from_time']
            new_row.to_time = i['to_time']  
            new_row.insert()
            frappe.msgprint(str('Row updated successfully'))



elif len(Student_group) > 0:


    current_doc = frappe.get_doc("Student Time Table", group)

#
    if current_doc.table_1:
        current_doc.set('table_1', [])
        for i in sorted_cs_list:
            new_row = current_doc.append('table_1', {})
            new_row.instructor_name = i['instructor_name']
            new_row.schedule_date = i['schedule_date'] 
            new_row.room = i['room']
            new_row.from_time = i['from_time']
            new_row.to_time = i['to_time']  
            new_row.insert()
            frappe.msgprint(str('Row updated successfully'))
    current_doc.save()
            





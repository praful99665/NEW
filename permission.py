# .
student_group_name = None
student = doc.student
studentName = doc.student_name
program = doc.program
year = doc.academic_year
batch = doc.student_batch_name

# frappe.msgprint(str(student))


stud = frappe.get_doc("Student",student)
if stud:
    # frappe.msgprint(str(stud.user))
    # frappe.msgprint(str(stud.custom_student_account))
    gmail_name = stud.user
    
else:
    frappe.msgprint("Student not found.")
    
new_permission = frappe.new_doc("User Permission")
new_permission.user = gmail_name
new_permission.allow = "Student"
new_permission.for_value = student  # Use doc.name instead of "doc.name"
new_permission.insert()
frappe.msgprint("Student User permission created successfully.*")



new_permission = frappe.new_doc("User Permission")
new_permission.user = gmail_name
new_permission.allow = "Student Batch Name"
new_permission.for_value = batch  # Use doc.name instead of "doc.name"
new_permission.insert()
frappe.msgprint("Student Batch Name User permission created successfully.*")

student_group = frappe.get_list("Student Group",filters={'batch':batch})
# frappe.msgprint(str(student_group))
for i in student_group:
    frappe.msgprint(str(i.name))
    StudentGroup = frappe.get_doc("Student Group",i.name)
    frappe.msgprint(str(StudentGroup.instructors))
    for j in StudentGroup.instructors:
        frappe.msgprint(str(j.instructor))

        new_permission = frappe.new_doc("User Permission")
        new_permission.user = gmail_name
        new_permission.allow = "Instructor"
        new_permission.for_value = j.instructor # Use doc.name instead of "doc.name"
        new_permission.insert()
        frappe.msgprint("Instructor User permission created successfully.*")


    new_permission = frappe.new_doc("User Permission")
    new_permission.user = gmail_name
    new_permission.allow = "Program"
    new_permission.for_value = StudentGroup.program  # Use doc.name instead of "doc.name"
    new_permission.insert()
    frappe.msgprint("Program User permission created successfully.*")
    
    # new_permission = frappe.new_doc("User Permission")
    # new_permission.user = gmail_name
    # new_permission.allow = "Student Time Table"
    # new_permission.for_value = i.name  # Use doc.name instead of "doc.name"
    # new_permission.insert()
    # frappe.msgprint("Student Time Table permission created successfully.*")
        
    program = frappe.get_doc("Program",StudentGroup.program)
    # frappe.msgprint(str(program.courses))
    for k in program.courses:
        new_permission = frappe.new_doc("User Permission")
        new_permission.user = gmail_name
        new_permission.allow = "Course"
        new_permission.for_value = k.course  # Use doc.name instead of "doc.name"
        new_permission.insert()
        frappe.msgprint("Course permission created successfully.*")
        
        

    
        

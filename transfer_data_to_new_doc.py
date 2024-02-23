frappe.ui.form.on('C_opportunity', {
	refresh(frm) {
	   var Course = frm.doc.course;
	   var G_program ;
        Course.forEach(function(i){
            G_program = i.course;
        });
                        frm.add_custom_button(__('Create Student Applicant'), function() {
                        
                        frappe.new_doc('Student Applicant',{
                        "first_name" : frm.doc.first_name,
                        "middle_name":frm.doc.middle_name,
                        "last_name" : frm.doc.last_name,
                        // "gender" : "",
                        // "source" : "",
                        "student_mobile_number" : frm.doc.mob,
                        "student_email_id" : frm.doc.email,
                        "program": G_program,
                        "custom_lead": frm.doc.lead_id,
                        "custom_opp_name": frm.doc.name,
                        "address_line_1": frm.doc.address,
                        "city": frm.doc.city,
                        "gender":frm.doc.gender,
                    });
                

                    });
    }
});



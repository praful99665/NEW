frappe.ui.form.on('Topics_c', {
    completion: function(frm, cdt, cdn) {
        var topicTable = frm.doc.topic_table;
        var doc = locals[cdt][cdn];

        if (doc.completion && !doc.t_date) {
            // Set today's date in the 't_date' field for the unchecked checkbox row
            frappe.model.set_value(cdt, cdn, 't_date', frappe.datetime.nowdate());
        } else if (!doc.completion && doc.t_date) {
            // Reset the 't_date' field only if it is not already set
            frappe.model.set_value(cdt, cdn, 't_date', null);
        }

        // Calculate the completion percentage and update the 'percent' field (your existing code)
        var totalCheckboxes = topicTable.length;
        var checkedCount = topicTable.filter(row => row.completion).length;
        var percentage = (checkedCount / totalCheckboxes) * 100;

        if (percentage === 0) {
            frm.set_value('percent', 'Not Started');
        } else if (percentage === 100) {
            frm.set_value('percent', 'Successfully Completed');
        } else {
            frm.set_value('percent', percentage.toFixed(1) + '%');
        }

        // Logging information in the console (your existing code)
        console.log('Total Checkboxes:', totalCheckboxes);
        console.log('Checked Count:', checkedCount);
        console.log('Percent:', frm.doc.percent);

        // Save the form (your existing code)
        frm.save();
    }
});

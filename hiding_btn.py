
frappe.listview_settings['Student Time Table'] = {
    refresh: function(listview) {
        // Check if the user has the 'HR Manager' role
        if (frappe.user.has_role('HR Manager')) {
            // If the user has the 'HR Manager' role, hide the 'Create' button
            listview.page.clear_primary_action();
        }
        
        if (frappe.user.has_role('Student')) {
            // If the user has the 'Student' role, hide the 'Create' button
            listview.page.clear_primary_action();
        }

        // Check if the user has the 'Instructor' role
        if (frappe.user.has_role('Instructor')) {
            // If the user has the 'Instructor' role, perform specific actions
            console.log('User is an Instructor');
        }
    }
};

        


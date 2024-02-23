frappe.ui.form.on('C_Lead', {
    refresh: function(frm) {
        // Add a custom button to delete the document based on Full Name
        frm.add_custom_button(__('Delete Document'), function() {
            var full_name = frm.doc.name;
            console.log(full_name);
            
            // Search for the document based on Full Name
            frappe.call({
                method: 'frappe.client.get_list',
                args: {
                    'doctype': 'C_Lead', // Specify the correct doctype here
                    'filters': {
                        'name': full_name
                    },
                    'fields': ['name']
                },
                callback: function(response) {
                    if (response.message && response.message.length > 0) {
                        var doc_name = response.message[0].name;
                        
                        // Confirm with the user before deleting the document
                        frappe.confirm(
                            __('Are you sure you want to delete this document?'),
                            function() {
                                // If the user confirms, delete the document
                                frappe.call({
                                    method: 'frappe.client.delete',
                                    args: {
                                        'doctype': 'C_Lead',
                                        'name': doc_name
                                    },
                                    callback: function(response) {
                                        if (!response.exc) {
                                            frappe.msgprint(__('Document deleted successfully.'));
                                            // Redirect the user to the list view after deletion
                                            frappe.set_route('List', frm.doctype);
                                        } else {
                                            frappe.msgprint(__('An error occurred while deleting the document.'));
                                        }
                                    }
                                });
                            }
                        );
                    } else {
                        frappe.msgprint(__('Document not found.'));
                    }
                }
            });
        });
    }
});


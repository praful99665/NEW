frappe.ui.form.on('Payment Entry', {
    refresh(frm) {
        frm.set_query('paid_from', function() {
            return {
                "filters": {
                    "is_group":0,
                    
                }
            };
        });
        
            frm.set_query('paid_to', function() {
            return {
                "filters": {
                    "is_group":0,
                    
                }
            };
        });
    }
});


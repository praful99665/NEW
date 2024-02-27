frappe.ui.form.on('Student Applicant', {
    custom_create_account: function(frm) {
        if (frm.doc.custom_create_account === 1) {
            var first = frm.doc.first_name || '';
            var middle = frm.doc.middle_name || '';
            var last = frm.doc.last_name || '';
            var doc_name = frm.doc.name;
            var last_five_digits = doc_name.slice(-5);
            var lead_no = frm.doc.custom_lead;
            var last_three_digits_lead = lead_no.slice(-3); // Extract last three digits from lead_no
            var account_name = first.trim();
            
            // Append middle name if not empty
            if (middle.trim() !== '') {
                account_name += ' ' + middle.trim();
            }
            
            // Append last name if not empty
            if (last.trim() !== '') {
                account_name += ' ' + last.trim();
            }
            
            // Append last three digits of lead_no
            account_name += ' - ' + last_three_digits_lead;
            
            // Check if the account already exists
            frappe.call({
                method: 'frappe.client.get_list',
                args: {
                    doctype: 'Account',
                    filters: { 'account_name': account_name }
                },
                callback: function(response) {
                    if (response.message && response.message.length > 0) {
                        // Account already exists, set the existing account to custom_account field
                        frm.set_value('custom_account', response.message[0].name);
                        frappe.msgprint("Account already exists with the name: " + account_name + ". Setting existing account.");
                        // Save the document after a delay of 1 second
                        setTimeout(function() {
                            frm.save();
                        }, 1000);
                    } else {
                        // Account doesn't exist, create a new one
                        createNewAccount(account_name, frm);
                    }
                }
            });
        }
    }
});

function createNewAccount(account_name, frm) {
    var new_account = frappe.model.get_new_doc("Account");
    new_account.account_name = account_name;
    new_account.parent_account = "Temporary Accounts - W";
    new_account.account_type = ""; // Set your desired account type
    frappe.db.insert(new_account).then(function(response) {
        frappe.msgprint("New account created successfully: " + response.name);
        // Set the new account in the custom_account field
        frm.set_value('custom_account', response.name);
        // Save the document after a delay of 1 second
        setTimeout(function() {
            frm.save();
        }, 1000);
    }).catch(function(err) {
        console.error(err);
        frappe.msgprint("Failed to create account.");
    });
}



// ......................

// frappe.ui.form.on('Student Applicant', {
//     custom_create_account: function(frm) {
//         if (frm.doc.custom_create_account === 1) {
//             var first = frm.doc.first_name || '';
//             var middle = frm.doc.middle_name || '';
//             var last = frm.doc.last_name || '';
//             var doc_name = frm.doc.name;
//             var last_five_digits = doc_name.slice(-5);
//             var lead_no = frm.doc.custom_lead;
//             var last_three_digits_lead = lead_no.slice(-3); // Extract last three digits from lead_no
//             var account_name = first.trim();
            
//             // Append middle name if not empty
//             if (middle.trim() !== '') {
//                 account_name += ' ' + middle.trim();
//             }
            
//             // Append last name if not empty
//             if (last.trim() !== '') {
//                 account_name += ' ' + last.trim();
//             }
            
//             // Append last three digits of lead_no
//             account_name += ' ' + last_three_digits_lead;
            
//             // Check if the account already exists
//             frappe.call({
//                 method: 'frappe.client.get_list',
//                 args: {
//                     doctype: 'Account',
//                     filters: { 'account_name': account_name }
//                 },
//                 callback: function(response) {
//                     if (response.message && response.message.length > 0) {
//                         // Account already exists, set the existing account to custom_account field
//                         frm.set_value('custom_account', response.message[0].name);
//                         frappe.msgprint("Account already exists with the name: " + account_name + ". Setting existing account.");
//                         // Save the document after a delay of 1 second
//                         setTimeout(function() {
//                             frm.save();
//                         }, 1000);
//                     } else {
//                         // Account doesn't exist, create a new one
//                         createNewAccount(account_name, frm);
//                     }
//                 }
//             });
//         }
//     }
// });

// function createNewAccount(account_name, frm) {
//     var new_account = frappe.model.get_new_doc("Account");
//     new_account.account_name = account_name;
//     new_account.parent_account = "Temporary Accounts - W";
//     new_account.account_type = ""; // Set your desired account type
//     frappe.db.insert(new_account).then(function(response) {
//         frappe.msgprint("New account created successfully: " + response.name);
//         // Set the new account in the custom_account field
//         frm.set_value('custom_account', response.name);
//         // Save the document after a delay of 1 second
//         setTimeout(function() {
//             frm.save();
//         }, 1000);
//     }).catch(function(err) {
//         console.error(err);
//         frappe.msgprint("Failed to create account.");
//     });
// }



// // ...................
// frappe.ui.form.on('Student Applicant', {
//     custom_create_account: function(frm) {
//         if (frm.doc.custom_create_account === 1) {
//             var first = frm.doc.first_name || '';
//             var middle = frm.doc.middle_name || '';
//             var last = frm.doc.last_name || '';
//             var doc_name = frm.doc.name;
//             var last_five_digits = doc_name.slice(-5);
//             var Id = parseInt(last_five_digits);
            
//             var account_name = first.trim();
            
//             // Append middle name if not empty
//             if (middle.trim() !== '') {
//                 account_name += ' ' + middle.trim();
//             }
            
//             // Append last name if not empty
//             if (last.trim() !== '') {
//                 account_name += ' ' + last.trim();
//             }
            
//             // Append Id
//             account_name += ' ' + Id;
            
//             // Check if the account already exists
//             frappe.call({
//                 method: 'frappe.client.get_list',
//                 args: {
//                     doctype: 'Account',
//                     filters: { 'account_name': account_name }
//                 },
//                 callback: function(response) {
//                     if (response.message && response.message.length > 0) {
//                         // Account already exists, set the existing account to custom_account field
//                         frm.set_value('custom_account', response.message[0].name);
//                         frappe.msgprint("Account already exists with the name: " + account_name + ". Setting existing account.");
//                         // Save the document after a delay of 1 second
//                         setTimeout(function() {
//                             frm.save();
//                         }, 1000);
//                     } else {
//                         // Account doesn't exist, create a new one
//                         createNewAccount(account_name, frm);
//                     }
//                 }
//             });
//         }
//     }
// });

// function createNewAccount(account_name, frm) {
//     var new_account = frappe.model.get_new_doc("Account");
//     new_account.account_name = account_name;
//     new_account.parent_account = "Temporary Accounts - W";
//     new_account.account_type = ""; // Set your desired account type
//     frappe.db.insert(new_account).then(function(response) {
//         frappe.msgprint("New account created successfully: " + response.name);
//         // Set the new account in the custom_account field
//         frm.set_value('custom_account', response.name);
//         // Save the document after a delay of 1 second
//         setTimeout(function() {
//             frm.save();
//         }, 1000);
//     }).catch(function(err) {
//         console.error(err);
//         frappe.msgprint("Failed to create account.");
//     });
// }


// ................
// frappe.ui.form.on('Student Applicant', {
//     custom_create_account: function(frm) {
//         if (frm.doc.custom_create_account === 1) {
//             var first = frm.doc.first_name || '';
//             var middle = frm.doc.middle_name || '';
//             var last = frm.doc.last_name || '';
//             var doc_name = frm.doc.name;
//             var last_five_digits = doc_name.slice(-5);
//             var Id = parseInt(last_five_digits);
            
//             var account_name = first.trim();
            
//             // Append middle name if not empty
//             if (middle.trim() !== '') {
//                 account_name += ' ' + middle.trim();
//             }
            
//             // Append last name if not empty
//             if (last.trim() !== '') {
//                 account_name += ' ' + last.trim();
//             }
            
//             // Append Id
//             account_name += ' ' + Id;
            
//             // Check if the account already exists
//             frappe.call({
//                 method: 'frappe.client.get_list',
//                 args: {
//                     doctype: 'Account',
//                     filters: { 'account_name': account_name }
//                 },
//                 callback: function(response) {
//                     if (response.message && response.message.length > 0) {
//                         // Account already exists, do something (e.g., display a message)
//                         frappe.msgprint("Account already exists with the name: " + account_name);
//                     } else {
//                         // Account doesn't exist, create a new one
//                         createNewAccount(account_name, frm);
//                     }
//                 }
//             });
//         }
//     }
// });

// function createNewAccount(account_name, frm) {
//     var new_account = frappe.model.get_new_doc("Account");
//     new_account.account_name = account_name;
//     new_account.parent_account = "Temporary Accounts - W";
//     new_account.account_type = ""; // Set your desired account type
//     frappe.db.insert(new_account).then(function(response) {
//         frappe.msgprint("New account created successfully: " + response.name);
//         // Set the new account in the custom_account field
//         frm.set_value('custom_account', response.name);
//         // Save the document after a delay of 1 second if custom_account is not empty
//         if (frm.doc.custom_account) {
//             setTimeout(function() {
//                 frm.save();
//             }, 1000); // 1000 milliseconds = 1 second
//         }
//     }).catch(function(err) {
//         console.error(err);
//         frappe.msgprint("Failed to create account.");
//     });
// }


// ..............

// frappe.ui.form.on('Student Applicant', {
//     custom_create_account: function(frm) {
//         if (frm.doc.custom_create_account === 1) {
//             var first = frm.doc.first_name || '';
//             var middle = frm.doc.middle_name || '';
//             var last = frm.doc.last_name || '';
//             var doc_name = frm.doc.name;
//             var last_five_digits = doc_name.slice(-5);
//             var Id = parseInt(last_five_digits);
            
//             var account_name = first.trim();
            
//             // Append middle name if not empty
//             if (middle.trim() !== '') {
//                 account_name += ' ' + middle.trim();
//             }
            
//             // Append last name if not empty
//             if (last.trim() !== '') {
//                 account_name += ' ' + last.trim();
//             }
            
//             // Append Id
//             account_name += ' ' + Id;
            
//             var new_account = frappe.model.get_new_doc("Account");
//             new_account.account_name = account_name;
//             new_account.parent_account = "Temporary Accounts - W";
//             new_account.account_type = ""; // Set your desired account type
//             frappe.db.insert(new_account).then(function(response) {
//                 frappe.msgprint("New account created successfully: " + response.name);
//                 // Set the new account in the custom_account field
//                 frm.set_value('custom_account', response.name);
//                 // Save the document after a delay of 1 second if custom_account is not empty
//                 if (frm.doc.custom_account) {
//                     setTimeout(function() {
//                         frm.save();
//                     }, 1000); // 1000 milliseconds = 1 second
//                 }
//             }).catch(function(err) {
//                 console.error(err);
//                 frappe.msgprint("Failed to create account.");
//             });
//         }
//     }
// });



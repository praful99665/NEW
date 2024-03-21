# ,

# Example usage
email = doc.custom_email
recipients = email
subject = "Test Email"
message = "This is a test email sent from a server-side script in ERPNext."

# Send email
try:
    frappe.sendmail(recipients=recipients, subject=subject, message=message)
    frappe.msgprint("Email sent successfully")
except Exception as e:
    frappe.log_error(frappe.get_traceback(), _("Failed to send email"))
    frappe.msgprint(f"Failed to send email: {e}")


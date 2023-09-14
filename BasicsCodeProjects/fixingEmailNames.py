from fixingEmailNamesAssets import *

correct_emails = ""

def correcting_emails(emails):
    new_correct_email = ""
    simple_email = ""
    email_list = []
    for element in emails:
        if element != "\n":
            simple_email += element.lower()
        else:
            email_list.append(simple_email)
            simple_email = ""
            
    for email in email_list:
        if ("uol" in email or "yahoo" in email or "gmail" in email) and "-" not in email:
            new_correct_email += email + "\n"
        
    return new_correct_email

 
correct_emails = correcting_emails(emails)
print(correct_emails)
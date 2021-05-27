import smtplib, ssl

'''
For this to work you need a gmail account
and also enable this feature:
https://myaccount.google.com/lesssecureapps
'''

EMAIL = "youremail@gmail.com"
PASSWORD = "YOURPASSWORD"

context = ssl.create_default_context()
port = 465  # For SSL

def send_email(recipient, subject, message):
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(EMAIL, PASSWORD)

        server.sendmail(EMAIL, recipient, f"Subject: {subject}\n\n{message}")
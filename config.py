'''
Account info for the email account you're going to send the reminder from
For this to work you need a gmail account
and also enable this feature:
https://myaccount.google.com/lesssecureapps

Note: it maybe makes sense to make a separate email
      for this task if you don't trust this to input
      your real email and password
'''
SENDER_EMAIL = 'youremail@gmail.com'
SENDER_PASSWORD = 'yourpassword'

# Recipient email (can be the same as above)
RECIPIENT_EMAIL = 'youremail@gmail.com'

# Email subject, can be anything
EMAIL_SUBJECT = 'emailsubject'

'''
The date format which should be in the email
See https://strftime.org/ for further info

this would produce dates like this: 
01.06. 12:00
'''
DATE_FORMAT = '%d.%m. %H:%M' 
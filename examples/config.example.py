'''
Account info for the email account you're going to send the reminder from
For this to work you need a gmail account
and also enable this feature:
https://myaccount.google.com/lesssecureapps

Note: it maybe makes sense to make a separate email
      for this task if you don't trust this to input
      your real email and password
'''
SENDER_EMAIL = 'example@gmail.com'
SENDER_PASSWORD = 'P@ssW0rd'

# Recipient email (can be the same as above)
RECIPIENT_EMAIL = 'example@gmail.com'

# Email subject, can be anything
EMAIL_SUBJECT = 'Daily Reminder'

'''
The date format which should be in the email
See https://strftime.org/ for further info

This would only show the time
      for example: 12:00
'''
DATE_FORMAT = '%H:%M' 
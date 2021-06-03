import smtplib, ssl
from datetime import datetime

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

def parse(filename):
    today = datetime.now()

    send = []

    with open(filename, 'r') as f:
        for idx, line in enumerate(f.readlines()):
            line = line.strip().split(' ')

            if len(line) <= 5:
                continue;

            minute = line[0]
            hour   = line[1]
            d_day  = line[2]
            month  = line[3]
            w_day  = line[4]
            content = ' '.join(line[5:])

            if not minute.isdigit() and minute != '*':
                return f"Error: Line {idx + 1}, 1st value has to be a digit!"

            if not hour.isdigit() and hour != '*':
                return f"Error: Line {idx + 1}, 2nd value has to be a digit!"

            if not d_day.isdigit() and d_day != '*':
                return f"Error: Line {idx + 1}, 3rd value has to be a digit!"
            
            if not month.isdigit() and month != '*':
                return f"Error: Line {idx + 1}, 4th value has to be a digit, month strings are not supported yet!"
            
            if not w_day.isdigit() and w_day != '*':
                return f"Error: Line {idx + 1}, 5th value has to be a digit, weekday strings are not supported yet!"

            #TODO: implement month and weekday strings
            if (str(today.date().day) == d_day or d_day == '*') and \
               (str(today.date().month) == month or month == '*') and \
               (str(today.date().weekday()) == w_day or w_day == '*'):

                event_time = ''

                if minute == '*' and hour == '*':
                    event_time = 'whole day'
                elif minute == '*' and hour != '*':
                    event_time = f'{hour:02d}:00'
                elif minute != '*' and hour == '*':
                    event_time = f'00:{minute:02d}'
                else:
                    event_time = f'{int(hour):02d}:{int(minute):02d}'

                send.append({
                    'line': idx,
                    'time': event_time,
                    'content': content,
                })

    return send

import smtplib, ssl
from datetime import datetime

from config import *

# taken from https://stackoverflow.com/questions/7390170/parsing-crontab-style-lines
from croniter import croniter

context = ssl.create_default_context()
port = 465  # For SSL

def send_email(message):
    with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)

        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, f'Subject: {EMAIL_SUBJECT}\n\n{message}')

def parse(filename):
    today = datetime.now()
    output = []

    with open(filename, 'r') as f:
        for idx, line in enumerate(f.readlines()):
            if line.startswith('#'):
                continue

            line = line.strip().split(' ')

            if len(line) <= 5:
                continue;

            try:
                cron_input = '* * ' + ' '.join(line[2:5])
                content = ' '.join(line[5:])

                cron = croniter(cron_input, today)
                cron_original = croniter(' '.join(line[:5]), today)

                next_date = cron.get_next(datetime).date()
                original_time = cron_original.get_next(datetime).time()

                # If cron matches, then add this to the list
                if next_date == today.date():
                    cron_time = datetime(next_date.year, next_date.month, next_date.day, \
                        original_time.hour, original_time.minute).strftime(DATE_FORMAT)

                    output.append([cron_time, content])
            except:
                return f'Error in line {idx + 1}!'

    return output

def generate_email(input):
    output = ''

    for line in input:
        # line[0] is the time and line[1] is the content, for more info see the function above
        output += f'[{line[0]}] {line[1]}\n'

    # ouput[:-1] to remove the last newline character
    return output[:-1]

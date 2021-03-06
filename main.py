from util import *

def run():
    tasks = parse('tasks.txt')

    email = ''

    if isinstance(tasks, list):
        email = generate_email(tasks)
    else:
        email = tasks

    send_email(email)


if __name__ == '__main__':
    run()
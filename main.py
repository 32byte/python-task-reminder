from util import *

def run():
    tasks = parse('tasks.txt')

    email = generate_email(tasks)

    send_email(email)


if __name__ == '__main__':
    run()
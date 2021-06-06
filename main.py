from util import *

def run():
    tasks = parse('data.txt')

    email = generate_email(tasks)

    send_email(email)


if __name__ == '__main__':
    run()
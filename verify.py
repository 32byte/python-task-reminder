from util import *

def run():
    tasks = parse('tasks.txt')

    if isinstance(tasks, list):
        print('File is valid!')
    else:
        print(tasks)

if __name__ == '__main__':
    run()
import sys

todo_list = []

def print_menu():
    print('Hi! You\'ve made it to the console todo list!')
    print('To view your to-do list, type !todo or /todo')
    print('If you want to add a task, enter !add or /add')
    print('If you want to delete a task, type !delete or /delete')
    print('If you want to exit the program, type !quit or /quit')

def show_tasks():
            if len(todo_list) == 0:
                print('No tasks.')
            else:
                for i, task in enumerate(todo_list, start=1):
                    print(f'{i}. {task}')
def add_task():
        user_add_task = input('Enter a task: ')
        todo_list.append(user_add_task)
        print(f'Task "{user_add_task}" added!')
def delete_task():
        try:
             user_delete_task = int(input('Enter task number: '))
             if 0 < user_delete_task <= len(todo_list):
                  todo_list.pop(user_delete_task - 1)
                  print(f'Task №{user_delete_task} has been removed!')
             else:
                   print('Invalid task number!')
        except: 
              print('Error: Please enter a valid number!')
def quit_func():
        print('Goodbye, good luck!')
        sys.exit()

def handle_command(command):
        if command == '!todo' or command == '/todo':
            show_tasks()
        elif command == '!add' or command == '/add':
            add_task()
        elif command == '!delete' or command == '/delete':
            delete_task()
        elif command == "!quit" or command == "/quit":
            quit_func()
        else:
            print('You entered an invalid command!')

print_menu()

while True:
    command = input('Enter the command: ')
    handle_command(command)
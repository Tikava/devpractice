from task import Task
import time

class TaskManagerUI:
    def __init__(self, task_list):
        self.task_list = task_list

    def start(self):
        action = ''
        while action.lower() not in ['quit', 'q']:
            action = input(
                '\nAdd - to add task to list\n'
                'Remove - to remove the task from list\n'
                'Show - to get task list\n'
                'Update - to update info\n'
                'Quit - to exit\n:'
            )
            match action.lower():
                case 'add':
                    self.add_task()
                case 'remove':
                    self.remove_task()
                case 'show':
                    self.show_tasks()
                case 'update':
                    self.update_task()
                case 'quit':
                    print('Quitting the task manager')
                    break
                case default:
                    print('\nYou have to enter a valid action (Add/Remove/Show/Update/Quit)')

    def add_task(self):
        print('Please enter task details below:')
        task_title = input('Title: ')
        task_description = input('Short description: ')
        task_date = input('Date(YYYY-MM-DD): ')
        if self.validate_task(task_title, task_description, task_date):
            task = Task(task_title, task_description, task_date)
            self.task_list.add_task(task)
            print('Your task has been added')
        else:
            print('Invalid task details')

    def update_task(self):
        print('Below given list of tasks, to update a task from your list, enter the title of the task')
        self.show_tasks()
        task_title = input('Title: ')
        task = self.task_list.get_task(task_title)
        if task:
            print('Please enter new task details below:')
            new_task_title = input('Title: ')
            new_task_description = input('Short description: ')
            new_task_date = input('Date(YYYY-MM-DD): ')

            if self.validate_task(new_task_title, new_task_description, new_task_date):
                self.task_list.remove_task(task_title)

                new_task = Task(new_task_title, new_task_description, new_task_date)

                self.task_list.add_task(new_task)

                print('Your task has been updated')
            else:
                print('Invalid task details')
        else:
            print('Task not found')

    def validate_task(self, title, description, date):
        if not title or not description or not date:
            return False
        try:
            time.strptime(date, '%Y-%m-%d')
        except ValueError:
            return False
        return True


    def remove_task(self):
        print('Below given list of tasks, to remove a task from your list, enter the title of the task')
        self.show_tasks()
        task_title = input('Title: ')
        self.task_list.remove_task(task_title)
        print('Your task has been removed')

    def show_tasks(self):
        tasks = self.task_list.get_tasks()
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"Task {i}:")
                print(f"Title: {task.get_title()}")
                print(f"Description: {task.get_description()}")
                print(f"Date: {task.get_date()}")
                print("-" * 20)
        else:
            print("No tasks found.")


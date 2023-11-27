from .file_manager import FileManager
import json
from .task import Task
from exceptions.exceptions import InvalidTaskError, TaskNotFoundError

class TaskList:
    
    def __init__(self, file_name):
        self.file_manager = FileManager(file_name)
    
    def add_task(self, task):
        if not isinstance(task, Task):
            raise InvalidTaskError("The task must be an instance of Task")
        
        tasks = self.get_tasks()
        tasks.append(task)
        self.file_manager.write_data(json.dumps([task.to_dict() for task in tasks]))
        
    def get_tasks(self):
        tasks_str = self.file_manager.read_data()
        if tasks_str:
            tasks = json.loads(tasks_str)
            return [Task(task['title'], task['description'], task['date']) for task in tasks]        
        return []
    
    def get_task(self, task_title):
        if not isinstance(task_title, str):
            raise ValueError("The task title must be a string")
        
        tasks = self.get_tasks()
        for task in tasks:
            if task.get_title() == task_title:
                return task
        raise TaskNotFoundError(f"A task with title {task_title} was not found.")
    
    def remove_task(self, task_title):
        if not isinstance(task_title, str):
            raise ValueError("The task title must be a string")
        
        tasks = self.get_tasks()
        task = self.get_task(task_title)
        if task:
            updated_tasks = [task for task in tasks if task.get_title() != task_title]
            self.file_manager.write_data(json.dumps([task.to_dict() for task in updated_tasks]))
        else:
            raise TaskNotFoundError(f"A task with title {task_title} was not found.")
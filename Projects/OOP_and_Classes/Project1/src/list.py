from file_manager import FileManager
import json
from task import Task

class TaskList:
    
    def __init__(self, file_name):
        self.file_manager = FileManager(file_name)
    
    def add_task(self, task):
        tasks = self.get_tasks()
        tasks.append(task.to_dict())
        self.file_manager.write_data(json.dumps(tasks))
        
    def get_tasks(self):
        tasks_str = self.file_manager.read_data()
        if tasks_str:
            tasks = json.loads(tasks_str)
            return [Task(task['title'], task['description'], task['date']) for task in tasks]        
        return []
    
    def get_task(self, task_title):
        tasks = self.get_tasks()
        for task in tasks:
            if task.get_title() == task_title:
                return task
        return None
    
    def remove_task(self, task_title):
        tasks = self.get_tasks()
        updated_tasks = [task for task in tasks if task.get_title() != task_title]
        self.file_manager.write_data(json.dumps(updated_tasks))


from src.ui import TaskManagerUI
from src.list import TaskList

task_list = TaskList('task_list.json')
ui = TaskManagerUI(task_list)
ui.start()
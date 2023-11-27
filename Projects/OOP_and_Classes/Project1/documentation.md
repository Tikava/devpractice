# Task Manager

## Description

This project is a simple task manager implemented in Python. It allows users to add, update, remove, and view tasks.

## Classes

### Task

The `Task` class represents a task with a title, description, and date. It provides getter and setter methods for each attribute, as well as a `to_dict` method that converts the task into a dictionary.

### FileManager

The `FileManager` class manages reading and writing data to a file. It provides a `read_data` method that reads data from a file and returns it as a string, and a `write_data` method that writes a string to a file.

### TaskList

The `TaskList` class manages a list of tasks. It uses a `FileManager` to save the tasks to a file. It provides methods to add a task (`add_task`), get all tasks (`get_tasks`), get a specific task by title (`get_task`), and remove a task by title (`remove_task`).

### TaskManagerUI

The `TaskManagerUI` class provides a command-line interface for managing tasks. It uses a `TaskList` to manage the tasks. It provides a `start` method that starts the user interface and handles user input. It also provides methods to add a task (`add_task`), update a task (`update_task`), remove a task (`remove_task`), and show all tasks (`show_tasks`).

## Usage

To use the task manager, create a `TaskList` and a `TaskManagerUI`, then call the `start` method of the `TaskManagerUI`. Here's an example:

```python
task_list = TaskList('task_list.json')
ui = TaskManagerUI(task_list)
ui.start()
```

This will start the task manager and allow the user to add, update, remove, and view tasks. The tasks are saved in a file named 'task_list.json'.
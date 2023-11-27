import os
from exceptions.exceptions import FileManagerError

class FileManager:
    def __init__(self, file_name):
        script_directory = os.path.dirname(os.path.realpath(__file__))
        project_directory = os.path.dirname(script_directory)
        resources_directory = os.path.join(project_directory, 'resources')
        self.file_path = os.path.join(resources_directory, file_name)

    def read_data(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
            return content
        except OSError as e:
            raise FileManagerError(self.file_path, e.strerror)

    def write_data(self, data):
        try:
            with open(self.file_path, 'w') as file:
                file.write(data)
        except OSError as e:
            raise FileManagerError(self.file_path, e.strerror)

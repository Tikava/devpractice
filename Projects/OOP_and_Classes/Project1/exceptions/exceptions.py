import errno

class FileManagerError(OSError):
    def __init__(self, file_path, message):
        super().__init__(errno.ENOENT, message)
        self.file_path = file_path
        
class InvalidTaskError(Exception):
    pass

class TaskNotFoundError(Exception):
    pass
class Task:
    
    def __init__(self, title, description, date):
        self.title = title
        self.description = description
        self.date = date
    
    def set_title(self, title):
        self.title = title
    
    def get_title(self):
        return self.title
    
    def set_description(self, description):
        self.description = description
    
    def get_description(self):
        return self.description
    
    def set_date(self, date):
        self.date = date

    def get_date(self):
        return self.date
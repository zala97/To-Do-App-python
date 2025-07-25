import time
from datetime import datetime

# Docstring by Alimate


class Task:
    
    # get current date and time 
    current_date_time = datetime.today().ctime()

    def __init__(self, title, desctiption, priority, date, state, create_at):
        self.title = title
        self.description = desctiption
        self.priority = priority
        self.date = date
        self.state = state
        self.create_at = create_at

    # to representation the task (optional)
    def __repr__(self):
        return f"Task({self.title} , {self.description} , {self.priority} , {self.date} , {self.state} , {self.create_at})"
    # Add task function
    def Add_Task(self):
        """
        Create the sturcture of the task and pass it to the server side
        """
        # forming the structure of the data to send to the server side
        data_structure = {
            "Title": f"{self.title}",
            "Desc": f"{self.description}",
            "Priority": f"{self.priority}",
            "Date": f"{self.date}",
            "state": f"{self.state}",
            "Create at": f"{self.current_date_time}",
        }
        return data_structure
    # for removing task from the task_list
    def Remove_Task(self):
        pass
    # for editing the tasks
    def Edit_Task(self):
        pass
    # Reminder's , need to be modified later , maybe it will moved from this class 
    def Reminders(self):
        pass
    # to fetch list of all tasks (pendings and dones)
    def get_list_of_task(self):
        # for solving the circular import Error we import in this method
        from backend.server import fetch_tasks
        fetch_tasks()

# creating an object (task) for the first time (example)
task = Task('task number 1' , 'this is the test' , 'Medium' , '7/25/2025' , state='Pending' , create_at=Task.current_date_time)


import time
from datetime import datetime
# Docstring by Alimate
def Add_Task():
    '''
        Create the sturcture of the task and pass it to the server side
    '''
    # get the currnet date and time
    current_date_time = datetime.today()

    data_structure = {
        "Title" : '',
        "Desc" : '',
        "Priority" : '',
        "Date" : '',
        "Create at" : f'{current_date_time}'
    }

def Remove_Task():
    pass

def Edit_Task():
    pass

def Reminders():
    pass

def Get_list_of_Tasks():
    pass
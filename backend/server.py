import requests
import redis
from datetime import datetime
from time import sleep
from Features.feature import Task

# connect to the redis server for implement the db
R = redis.Redis(host="localhost", port=6379, decode_responses=True)


def fetch_tasks():
    print("Fetching tasks ...")
    sleep(2)
    # fetching task id from the server
    taks_id = R.lrange("tasks_id", 0, -1)
    # iterate on the list and get all detail of the tasks
    print(taks_id)
    for tid in taks_id:
        task = R.hgetall(f"task:{tid}")
        print(f"Task ID : {tid}")
        print(f"Title : {task.get('Title')}")
        print(f"Desc : {task.get('Desc')}")
        print(f"Date : {task.get('Date')}")
        print(f"Create at : {task.get('create at')}")
        print("--------------------------------------------------")


fetch_tasks()


def set_connection():

    id_session = R.incr("task:id")
    # create the sturcture of the tasks
    # maybe it changed
    print("processing ...")
    sleep(2)
    try:
        R.hset(f"task:{id_session}", mapping=Task().Add_Task())
        print("Task added Successfully.")
    except Exception as err:
        print(f"Error is : {err}")
    finally:
        print("done")

    # pushing the tasks into the list to fetch them anytime
    R.rpush("tasks_id", id_session)


# set_connection()

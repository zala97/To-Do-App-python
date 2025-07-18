import requests
import redis
from random import randint



hash_list = []
print(hash_list)
def RandomNumber():
    rand_number = randint(1 , 1000)
    return rand_number

def set_connection():
    R = redis.Redis(host='localhost' , port=6379 , decode_responses=True)
    id_session = RandomNumber()    
    # print(id_session)
    hash_list.append(id_session)

    R.hset(f'user_request:{id_session}' , mapping={
        'Title' : f'test1',
        'Desc' : f'test2',
        'Date' : f'test3'
    })

    print(R.hgetall('user_request:528'))


set_connection()


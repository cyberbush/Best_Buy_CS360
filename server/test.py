import requests
# using requests library to test backend without using frontend

def query():
    response = requests.get('http://localhost:5000/users_db')
    print(response.json())

query()

# add new item
data = {'name':'new name', 'description':'new description', 'status':'new status'}
response = requests.post('http://localhost:5000/users_db', json = data)
query()

# update the old item
data = {'name':'Change name', 'description':'new description', 'status':'new status', 'id':1}
response = requests.post('http://localhost:5000/users_db', json= data)
query()

# remove item
data = {'delete': True, 'id':1}
response = requests.post('http://localhost:5000/users_db', json= data)
query()
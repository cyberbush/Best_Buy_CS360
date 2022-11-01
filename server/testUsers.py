import requests
# using requests library to test backend without using frontend

def query():
    response = requests.get('http://localhost:5000/api/users')
    print(response.json())

query()

# sign up
data = {'firstName':'first', 'lastName':'last', 'email':'test@gmail.com', 'password':'123456'}
response = requests.post('http://localhost:5000/api/signup', json = data)
print(response.json())
query()

# login
data = {'firstName':'first', 'lastName':'last', 'email':'test@gmail.com', 'password':'123456'}
response = requests.post('http://localhost:5000/api/login', json= data)
print(response.json())

# remove user
data = {'delete': True, 'id':2}
response = requests.post('http://localhost:5000/api/users', json= data)
query()
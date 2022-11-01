import requests
# using requests library to test backend without using frontend

def query():
    response = requests.get('http://localhost:5000/products_db')
    print(response.json())

query()

# add new item
data = {'name':'new name', 'price':0.0, 'description':'new description', 'category':'new category', 'status':'new status'}
response = requests.post('http://localhost:5000/products_db', json = data)
query()

# update the old item
data = {'name':'Change name', 'price':10.50, 'description':'new description', 'category':'new category', 'status':'new status', 'id':3}
response = requests.post('http://localhost:5000/products_db', json= data)
query()

# remove item
data = {'delete': True, 'id':3}
response = requests.post('http://localhost:5000/products_db', json= data)
query()
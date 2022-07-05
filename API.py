import requests

def get_phone(name):
    phone = requests.get(f'http://localhost:5000/api?action=phone&name={name}')
    return phone.text

def get_name(phone):
    name = requests.get(f'http://localhost:5000/api?action=name&phone={phone}')
    return name.text
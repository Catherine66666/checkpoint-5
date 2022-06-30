import requests

def get_phone(name):
    phone = requests.get(f'http://localhost:5000/api?action=phone&name={name}')
    return phone.text


#def get_phone(name):
    #r = requests.get('http://localhost:5000')
    #result = r.text
    #return result

import os
import requests
import json

import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

def test_get_employees():

    url = os.getenv('API_URL')

    response = requests.get(url)

    if response.status_code == 200:
        assert response.status_code == 200 and response.text is not None
    else:
        assert False

def test_get_employee():

    url = os.getenv('API_URL')

    params = {'nome': 'natan'}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        assert response.status_code == 200 and response.text is not None
    else:
        assert False

def test_create_employee():

    url = os.getenv('API_URL')

    data = {
        "matricula": "1181177100",
        "nome": "natan Nascimento",
        "email": "natan.oliveira@souunit.com.br"
    }

    response = requests.post(url, data=json.dumps(data))

    if response.status_code == 201:
        assert response.status_code == 201 and response.text is not None
    else:
        assert False  

def test_update_employee():

    url = os.getenv('API_URL')

    matricula = 1181177100

    data = {
        "nome": "Natan Nascimento",
        "email": "natan.nascimento@souunit.com.br"
    }

    response = requests.put(url + f'/{str(matricula)}' , data=json.dumps(data))
    
    if response.status_code == 200:
        assert response.status_code == 200 and response.text is not None
    else:
        assert False  

def test_delete_employee():

    url = os.getenv('API_URL')

    matricula = 1181177100

    response = requests.delete(url + f'/{str(matricula)}')

    assert response.status_code == 200
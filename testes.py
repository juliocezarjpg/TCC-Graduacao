import requests
import time

HEROKU = 'https://tcc-julio.herokuapp.com'

while True:
    response = requests.get(HEROKU + '/api/v1/data_download')
    print(response.status_code)
    if response.status_code == '200':
        print(response.json())
    time.sleep(0.5)

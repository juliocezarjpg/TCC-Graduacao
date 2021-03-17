import requests
import time

HEROKU = 'https://tcc-julio.herokuapp.com'

while True:
    response = requests.get(HEROKU + '/api/v1/data_download')
    if response.json():
        print(response)
    time.sleep(0.5)

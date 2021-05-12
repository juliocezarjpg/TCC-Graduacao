import requests
import time

HEROKU = 'https://tcc-julio.herokuapp.com'

# while True:
#     response = requests.get(HEROKU + '/api/v1/data_download')
#     if response.json():
#         print(response.json())
#     time.sleep(0.5)

response = requests.post('http://127.0.0.1:5000/api/v1/img_upload', data={"testesteste"})
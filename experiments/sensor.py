import random
import time

import requests as requests

while True:
    # generate a random value
    value = random.randint(1, 100)

    # connect to the server
    # send post data to the server
    url = 'http://127.0.0.1:8000/experiments/sensor/add'
    data = {'value': value}
    result = requests.post(url, data)
    print(result)

    # delay 5 min
    time.sleep(300)



import random
import time
from prometheus_client import start_http_server, Gauge

random_number_metric = Gauge('random_number', 'Random number generated every 30 sec')

def generate_random_number():
    return random.randint(1, 10)

if __name__ == '__main__':
    start_http_server(8000)
    
    while True:
        random_number = generate_random_number()
        print('Random number is: ', random_number)
        random_number_metric.set(random_number)
        
        time.sleep(30)
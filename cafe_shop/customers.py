import time
from threading import Thread


class Customer(Thread):
    def __init__(self, num_customer):
        super().__init__()
        self.num_customer = num_customer

    def run(self):
        time.sleep(1)
        print(f'Посетитель номер {self.num_customer} покушал и ушёл.')


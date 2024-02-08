import queue
import random
import time

from cafe_shop.customers import Customer


class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables

    def customer_arrival(self):
        customers = []
        for i in range(20):
            customer = Customer(i + 1, self)
            customers.append(customer)
            print(f'Посетитель номер {customer.number} прибыл')
            customer.start()
            time.sleep(1)
        for cust in customers:
            cust.join()

    def serve_customer(self, customer):
        for table in self.tables:
            if not table.is_busy:
                print(f'Посетитель номер {customer.number} сел за стол {table.number}')
                table.switch()
                time.sleep(5)
                table.switch()
                print(f'Посетитель номер {customer.number} покушал и ушёл.')
                if not self.queue.empty():
                    self.serve_customer(self.queue.get())
                return
        print(f'Посетитель номер {customer.number} ожидает свободный стол')
        self.queue.put(customer)

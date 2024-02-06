import queue
import random
# import time

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
            # time.sleep(1)
            _ = 3 ** (random.randint(50, 70) * 10_000)
        for cust in customers:
            cust.join()

    def serve_customer(self, customer):
        self.queue.put(customer)
        for table in self.tables:
            if not table.is_busy:
                while not self.queue.empty():
                    cust = self.queue.get()
                    print(f'Посетитель номер {cust.number} сел за стол {table.number}')
                    table.switch()
                    _ = 3 ** (random.randint(50, 70) * 100_000)
                    # time.sleep(5)
                    table.switch()
                    print(f'Посетитель номер {cust.number} покушал и ушёл.')
                    return
        print(f'Посетитель номер {customer.number} ожидает свободный стол')

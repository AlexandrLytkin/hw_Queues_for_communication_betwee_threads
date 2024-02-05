import queue
import time

from cafe_shop.customers import Customer


class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = list(tables)

    def customer_arrival(self):
        for i in range(20):
            customer = Customer(i + 1)
            self.serve_customer(customer)
            time.sleep(0.1)

    def serve_customer(self, customer):
        print(f'Посетитель номер {customer.num_customer} прибыл')
        # if not any(table.is_busy for table in self.tables):
        for table in self.tables:
            if not table.is_busy:
                print(f'Посетитель номер {customer.num_customer} сел за стол {table.number}')
                if self.queue.empty():
                    table.switch()
                    customer.run()
                    # table.switch()
                    break

                else:
                    cust = self.queue.get()
                    table.switch()
                    cust.run()
                    table.switch()
                    break

        else:
            print(f'Посетитель номер {customer.num_customer} ожидает свободный стол')
            self.queue.put(customer)

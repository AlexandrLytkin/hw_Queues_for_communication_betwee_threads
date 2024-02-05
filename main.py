import threading

from cafe_shop.cafees import Cafe
from cafe_shop.tables import Table

table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)

customer_arrival_thread.start()

customer_arrival_thread.join()

print('Посещения закончились кафе закрыто на ремонт')

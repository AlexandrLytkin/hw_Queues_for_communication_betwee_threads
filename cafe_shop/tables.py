class Table:
    def __init__(self, number, is_busy=False):
        self.number = int(number)
        self.is_busy = is_busy

    def switch(self):
        self.is_busy = not self.is_busy

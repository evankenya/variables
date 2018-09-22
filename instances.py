class worker:
    raise_amount = 1.05
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
    def allworkers(self):
        return '{} , {}, {} '.format(self.first, self.last, self.pay)
    def amount_raised(self):
        self.pay = int (self.pay * self.raise_amount)
worker_1 = worker ('Evans', 'Ongera', 30000)
worker_2 = worker ('Kanini', 'Obaga', 25000)
print (worker_1.allworkers())
print (worker_2.allworkers())
      #or
print (worker_1.pay)
worker_1.amount_raised()
print (worker_1.pay)
      #or
print (worker_2.pay)
worker_2.amount_raised()
print (worker_2.pay)
      #or
print (worker.raise_amount)
print (worker_1.raise_amount)
print (worker_2.raise_amount)
      #or
print (worker_1.raise_amount)
worker.amount_raised
print (worker_1.raise_amount)
      #or
print (worker_1.raise_amount)
worker.amount_raised
print (worker_1.raise_amount)
      #or
print (worker.__dict__)
      #or
print (worker_1.__dict__)
      #or
print (worker_2.__dict__)
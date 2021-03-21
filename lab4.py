import random
import os
import time
import functools


class Cashier:
    def __init__(self, name):
        self.name = name
        self.is_busy = False

    def serv(self, b):
        self.b = b
        self.is_busy = True

    def pass_(self, t):
        if self.b != None:
            self.b.amount -= t
            if self.b.amount == 0:
                self.b = None
                self.is_busy = False


class Buyer:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


buyers = []
for i in range(random.randint(10, 30)):
    buyers.append(Buyer(f"Buyer {i}", random.randint(1, 6)))

cashier = []
for i in range(random.randint(4, 5)):
    cashier.append(Cashier(f"Cashier {i}"))


def print_queue():
    os.system("clear")
    for c in cashier:
        print(c.name)
        print(f"\t Is Busy: {c.is_busy}")
        if c.is_busy:
            print(f"\tServing: {c.b.name}")
            print(f"\tProducts left: {c.b.amount}")

    print("\n Buyers left:")

    for b in buyers:
        print(f"{b.name} {b.amount}")


while True:
    for c in cashier:
        if not c.is_busy and len(buyers) > 0:
            c.serv(buyers.pop(0))

    print_queue()

    m = 10000
    for c in cashier:
        if c.b != None:
            if c.b.amount < m:
                m = c.b.amount
    time.sleep(m)
    for c in cashier:
        c.pass_(m)
    if len(buyers) == 0 and not functools.reduce(lambda a, b: a or b, map(lambda x: x.is_busy, cashier), False):
        break

print_queue()

print("All buyers are served")

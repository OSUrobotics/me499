import random

class GumballMachine:
    def __init__(self, capacity=50, required_coins=2):
        self.capacity = capacity
        self.required_coins = required_coins

        # These are state variables which are always initialized to a specific value
        self.current_gumballs = capacity
        self.current_coins = 0

    def spin_knob(self):
        if self.current_coins < self.required_coins:
            raise Exception('There are not enough coins in the machine!')

        self.current_coins -= self.required_coins
        self.current_gumballs -= 1
        return random.choice(['Red', 'Blue', 'Green'])

    def insert_coin(self, num_coins = 1):
        if num_coins < 0:
            raise ValueError('You can\'t remove coins from the machine!')

        self.current_coins += num_coins

    def refill(self):
        self.current_gumballs = self.capacity

    def __repr__(self):
        base = '<GumballMachine - Costs {} coins per play ({} currently inserted, {}/{} gumballs remaining)>'
        return base.format(self.required_coins, self.current_coins, self.current_gumballs, self.capacity)

    def __str__(self):
        return self.__repr__()

if __name__ == '__main__':
    machine = GumballMachine(30, 5)
    machine.insert_coin(12)
    machine.spin_knob()
    machine.spin_knob()
    try:
        machine.spin_knob()
    except Exception as e:
        print(e)

    print(machine)
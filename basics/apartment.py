class Apartment:
    size = ''
    cost = ''

    def __init__(self, size, cost):
        self.size = size
        self.cost = cost

    def calculate(self):
        """
        This function calculates sqm cost of apt
        """
        if self.size.isdecimal() and self.cost.isdecimal():
            return int(self.cost)/int(self.size)
        else:
            print("Invalid values.")
            exit()

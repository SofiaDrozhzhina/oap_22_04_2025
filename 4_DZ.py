class MinStat:
    def __init__(self):
        self.values = []

    def add_number(self, number):
        self.values.append(number)

    def result(self):
        return min(self.values) if self.values else None


class MaxStat:
    def __init__(self):
        self.values = []

    def add_number(self, number):
        self.values.append(number)

    def result(self):
        return max(self.values) if self.values else None


class AverageStat:
    def __init__(self):
        self.values = []

    def add_number(self, number):
        self.values.append(number)

    def result(self):
        return sum(self.values) / len(self.values) if self.values else None



class Capitals:
    def __init__(self):
        self.time_zone = {'Europe': {'Paris', 'London'}, 'US': {'Washington'}, 'Asia': {'Jerusalem'}}
        self.city = self.create_capital_arr()

    def create_capital_arr(self):
        arr = []
        for value in self.get_mainland_capitals().values():
            for capital in value:
                arr.append(capital)
        return arr

    def get_mainland_capitals(self):
        return self.time_zone

    def get_capitals(self):
        return self.city

    def add_capital(self, capital, mainland):
        if capital not in self.get_capitals():
            if mainland in self.get_mainland_capitals().keys():
                self.get_mainland_capitals()[mainland].append(capital)
                self.city.append(capital)
            else:
                self.get_mainland_capitals().update({mainland, capital})
                self.city.append(capital)

    def get_mainland_by_capital(self, capital):
        for key in self.get_mainland_capitals():
            if capital in self.get_mainland_capitals()[key]:
                return key




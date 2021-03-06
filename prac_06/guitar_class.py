YEAR = 2020
class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        if self.is_vintage == True:
            vintage_status = "(vintage)"
        else:
            vintage_status = ""
        return("{} ({}) : worth ${} {}").format(self.name, self.year, self.cost, vintage_status)

    def get_age(self):
        return(YEAR-self.year)

    def is_vintage(self):
        if self.get_age() > 50:
            return True
        else:
            return False
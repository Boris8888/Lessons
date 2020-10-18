class Worker:
    def __init__(self):
        self.name = "Boris"
        self.surname = "Chuprov"
        self.position = "Engineer"
        self.income = {"wage": 10000, "bonus": 10}


class Position(Worker):
    def get_full_name(self):
        print(f"{position.name} {position.surname}")

    def get_total_income(self):
        print("Зароботная плата сотрудника",
              position.income.get("wage") + (position.income.get("wage") * position.income.get("bonus") / 100))


position = Position()
position.get_full_name()
position.get_total_income()

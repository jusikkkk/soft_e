class Tomato:
    states = {'Плод отсутствует': 0,
    'Находится в стадии цветения': 1,
    'Помидор зелёный': 2,
    'Помидор красный': 3}

    def __init__(self, index):
        self._index = index  # защищенный атрибут
        self._sate = self.states['Плод отсутствует']  # защищенный атрибут

    def grow(self):
        if self._sate < 3:
            self._sate += 1

    def is_ripe(self):
        a = False
        if self._sate == 3:
            a = True
            return a
        else:
            return a


class TomatoBash:
    def __init__(self, count):
        self.tomatoes = [Tomato(index) for index in range(1, count+1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        isripe = all([tomato.is_ripe() for tomato in self.tomatoes])
        return isripe

    def give_away_all(self):
        self.tomatoes.clear()


class Gardener:
    def __init__(self, name, plant):
        self.name = name  # публичный атрибут
        self._plant = plant  # защищенный атрибут

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Вы собрали урожай!")
        else:
            print("Не все томаты созрели!")

    def knowledge_base(self):
        print("                  Справка")
        print(f"Садоводческая организация 'Ромашка' подтверждает, что {self.name}\n"
              f"действително является членом данного товарищества и за ним закреплён\n"
              f"помидорный куст\n")

bushka = TomatoBash(7)
griha_gardener = Gardener("Гриша", bushka)
Gardener.knowledge_base(griha_gardener)

griha_gardener.work()
griha_gardener.harvest()
griha_gardener.work()
griha_gardener.work()
griha_gardener.harvest()











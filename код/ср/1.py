class Julia:
    __slots__ = ['name']

    def __init__(self, name):
        if name == "Юля":
            self.name = f"Да, я {name}"
        else:
            self.name = f"Я не {name}, а Юля"

person1 = Julia('Аня')
person2 = Julia('Юля')
print(person1.name)
print(person2.name)
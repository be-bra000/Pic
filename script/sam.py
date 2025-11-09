class Tomato:
    stages = ('росток', 'цветение', 'зеленый', 'красный')

    def __init__(self, number):
        self.number = number
        self.stage = self.stages[0]

    def grow(self):
        current_stage_index = self.stages.index(self.stage)
        if current_stage_index < len(self.stages) - 1:
            self.stage = self.stages[current_stage_index + 1]

    def is_ready(self):
        return self.stage == 'красный'

class TomatoBush:
    def __init__(self, count):
        self.tomatoes = []
        for i in range(count):
            self.tomatoes.append(Tomato(i))

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def check_all_ready(self):
        for tomato in self.tomatoes:
            if not tomato.is_ready():
                return False
        return True

    def collect_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, tomato_bush):
        self.name = name
        self.tomato_bush = tomato_bush

    def care(self):
        if len(self.tomato_bush.tomatoes) == 0:
            print("На кусте нет помидоров для ухода!")
        else:
            self.tomato_bush.grow_all()
            print(f"{self.name} позаботился о растениях")

    def collect(self):
        if len(self.tomato_bush.tomatoes) == 0:
            print("Собирать нечего - куст пуст!")
        else:
            if self.tomato_bush.check_all_ready():
                self.tomato_bush.collect_all()
                print(f"{self.name} собрал прекрасный урожай!")
            else:
                print("Нужно подождать - еще не все помидоры созрели")

    @staticmethod
    def garden_guide():
        print("Советы по выращиванию томатов:")
        print("• Регулярно поливайте растения утром или вечером")
        print("• Удаляйте боковые побеги для лучшего роста")
        print("• Подкармливайте растения каждые 2 недели")
        print("• Собирайте урожай когда плоды полностью покраснеют\n")

Gardener.garden_guide()
bush = TomatoBush(8)
gardener = Gardener("Алексей", bush)
gardener.care()
gardener.collect()
gardener.care()
gardener.collect()
gardener.care()
gardener.collect()
gardener.care()
gardener.collect()
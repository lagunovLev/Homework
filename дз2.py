from abc import abstractmethod, ABC


class Animal(ABC):
    def __init__(self, name, species_name, height, mass, is_predator, is_pet):
        self.name = name
        self.species_name = species_name
        self.height = height
        self.mass = mass
        self.is_predator = is_predator
        self.is_pet = is_pet

    def greet(self):
        return (f"Я - {self.species_name}, меня зовут {self.name}. Мой рост - {self.height}, вес - {self.mass}. "
                f"Я {"не" if not self.is_predator else ""} хищник, {"прирученный" if self.is_pet else "дикий"}")

    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def sound(self):
        pass


class Elephant(Animal, ABC):
    def __init__(self, name):
        super().__init__(name, "Слон", "3 метра", "5 тонн", False, False)

    def walk(self):
        return "Топ-топ"

    def sound(self):
        return "УУУуууууууу!"


class Spider(Animal, ABC):
    def __init__(self, name):
        super().__init__(name, "Паук", "4 миллиметра", "30 грамм", False, False)

    def walk(self):
        return ""

    def sound(self):
        return "УУУуууууууу!"

    def make_web(self):
        return \
            ("      #    #    ##     \n"
             "   ##########  ##      \n"
             " ##   #       #  ###   \n"
             "  ##   ######   #   #  \n"
             "  #   ## ##  #####  #  \n"
             "  #  # #######    # #  \n"
             " ####   #   #  ###  ## \n"
             "#    ##########   ##   \n"
             "       #      #        \n")


animal = Elephant("Тотоша")
print(animal.greet())
animal = Spider("Евгений")
print(animal.make_web())
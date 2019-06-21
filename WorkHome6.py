class Animal:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def AllInfo(self):
        print(f'{self.name} и твой вес {self.weight}')

    def getFeed(self, name):
        print(f'Я {self.name} и меня надо покормить')

    def GetCollectEggs(self, id_animals,
                       name):  # показываю если у каждого класса определить индекс, то можно передать его в метод класса Animal. чтоб не описывать данный метод в каждом классе
        if id_animals == 1 or id_animals == 6 or id_animals == 4:
            print(f'Я {self.name} и у меня необходимо собирать яйца')

    def GetVoice(self, id_animals, voice):
        if id_animals == 1:
            print(f'Я {self.name}  и я  {voice}')
        if id_animals == 2:
            print(f'Я {self.name}  и я  {voice}')
        if id_animals == 3:
            print(f'Я {self.name}  и я  {voice}')
        if id_animals == 4:
            print(f'Я {self.name}  и я  {voice}')
        if id_animals == 5:
            print(f'Я {self.name}  и я  {voice}')
        if id_animals == 6:
            print(f'Я {self.name}  и я  {voice}')


class Geese(Animal):  # гусей
    ids = 1  # идентификатор для каждого класса животного
    voice = 'Гогочу'  # опледеляю для каждого класса тип голоса


class Сows(Animal):  # корову
    ids = 2
    voice = 'Мычу'

    def GetMilk(self, name):
        print(f'Я {self.name} и меня надо подоить')


class Sheeps(Animal):  # овец
    ids = 3
    voice = 'Блеею'

    def GetToCut(self, name):
        print(f'Я {self.name} и меня надо подстригать')


class Сhickens(Animal):  # кур
    ids = 4
    voice = 'Кудахчу'


class Goats(Animal):  # коз
    ids = 5
    voice = 'Блеею'

    def GetMilk(self, name):
        print(f'Я {self.name} и меня надо подоить')


class Ducks(Animal):  # утку
    ids = 6
    voice = 'Крякаю'

    def __str__(self):
        return str({
            'name': self.name,
            'size': self.weight,

        })


Geese1 = Geese('Серый', '10')
Geese2 = Geese('Белый', '15')
Сows1 = Сows('Манька', '90')
Sheeps1 = Sheeps('Барашек', '30')
Sheeps2 = Sheeps('Кудрявый', '28')
Сhickens1 = Сhickens('Ко-Ко', '3')
Сhickens2 = Сhickens('Кукареку', '2')
Goats1 = Goats('Рога', '12')
Goats2 = Goats('Копыто', '16')
Ducks1 = Ducks('Кряква', '4')

Geese1.GetVoice(Geese1.ids, Geese1.voice)
Geese2.GetVoice(Geese2.ids, Geese2.voice)
Сows1.GetVoice(Сows1.ids, Сows1.voice)
Sheeps1.GetVoice(Sheeps1.ids, Sheeps1.voice)
Sheeps2.GetVoice(Sheeps2.ids, Sheeps2.voice)
Сhickens1.GetVoice(Сhickens1.ids, Сhickens1.voice)
Сhickens2.GetVoice(Сhickens2.ids, Сhickens2.voice)
Goats1.GetVoice(Goats1.ids, Goats1.voice)
Goats2.GetVoice(Goats2.ids, Goats2.voice)
Ducks1.GetVoice(Ducks1.ids, Ducks1.voice)
####

Geese1.getFeed(Geese1.name)
Geese2.getFeed(Geese2.name)
Сows1.getFeed(Сows1.name)
Sheeps1.getFeed(Sheeps1.name)
Sheeps2.getFeed(Sheeps2.name)
Сhickens1.getFeed(Сhickens1.name)
Сhickens2.getFeed(Сhickens2.name)
Goats1.getFeed(Goats1.name)
Goats2.getFeed(Goats2.name)
Ducks1.getFeed(Ducks1.name)
####

Goats1.GetMilk(Goats1.name)
Goats2.GetMilk(Goats2.name)
Сows1.GetMilk(Сows1.name)

##
Sheeps1.GetToCut(Sheeps1.name)
Sheeps2.GetToCut(Sheeps2.name)
###

Geese1.GetCollectEggs(Geese1.ids, Geese1.name)
Geese2.GetCollectEggs(Geese2.ids, Geese2.name)

Ducks1.GetCollectEggs(Ducks1.ids, Ducks1.name)

Сhickens1.GetCollectEggs(Сhickens1.ids, Сhickens1.name)
Сhickens2.GetCollectEggs(Сhickens2.ids, Сhickens2.name)

lists = list()

lists.append(Geese1.__dict__)
lists.append(Geese2.__dict__)
lists.append(Сows1.__dict__)
lists.append(Sheeps1.__dict__)
lists.append(Sheeps2.__dict__)
lists.append(Сhickens1.__dict__)
lists.append(Сhickens2.__dict__)
lists.append(Goats1.__dict__)
lists.append(Goats2.__dict__)
lists.append(Ducks1.__dict__)

all_weight = 0
max_weight = 0
for item in lists:
    for key, value in item.items():
        if key == 'weight':
            all_weight += int(value)
            if int(value) > max_weight:
                max_weight = int(value)
print(f'Общий вес животных: {all_weight}')
print(f'Максимальный вес животного: {max_weight}')


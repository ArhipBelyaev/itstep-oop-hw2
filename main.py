import random



nameuser = input("Write your name: ")

class Student:
    def __init__(self, nameuser):
        self.nameuser = nameuser
        self.happiness = 50
        self.progress = 0
        self.active = True
        self.money = 0
        self.years_lived = 0

    def to_study(self):
        print('Time to study!')
        self.progress += 0.30
        self.happiness -= 8

    def to_sleep(self):
        print('ZZZZZZ!')
        self.happiness += 1

    def to_chill(self):
        print('Chill time!')
        self.happiness += 1
        self.progress -= 0.2
        self.money -= 40

    def to_money(self):
        print('money-money-money-money')
        self.happiness += 1
        self.progress += 0.1
        self.money += 25

    def to_work_money(self):
        self.happiness += 1
        self.progress += 0.1
        self.money += 25

    def is_active(self):
        if self.progress < -0.5:
            print('Vidrahuvaly((((')
            self.active = False
        elif self.happiness <= 0:
            print('Depression!')
            self.active = False
        elif self.progress > 10:
            print('Passes externally...')
            self.active = False
        elif self.money < -5:
            print('Go to work!!!')
            self.to_work_money()
        elif self.money < -6:
            amount = abs(self.money) * 10
            print(f'Add {amount} to money!')
            self.money += amount
        elif self.progress < 0:
            print('Problems with studying!')
            self.to_study()

    def status(self):
        print(f'Happiness: {self.happiness}')
        print(f'Progress: {round(self.progress, 2)}')
        print(f'Money: {round(self.money, 2)}$')

    def live_a_day(self, day):
        day_str = f'Day {day} of {self.nameuser} life'
        print(f"{day_str:=^50}")
        d3 = random.randint(1, 4)
        if d3 < 1:
            self.to_study()
        elif d3 < 2:
            self.to_sleep()
        elif d3 == 3:
            self.to_chill()
        elif d3 == 4:
            self.to_money()
        self.status()
        self.is_active()

        if day % 365 == 0 and day > 0:
            self.years_lived += 1
            print(f'Congratulations, you have lived for {self.years_lived} year(s)!')
            self.active = False

name = Student(nameuser=nameuser)
for day in range(1, 366):
    if name.active:
        name.live_a_day(day)
    else:
        break
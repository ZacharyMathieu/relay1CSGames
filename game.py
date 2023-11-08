import random


class Game:
    def __init__(self):
        self.projectName = "Projet"
        self.gamer = ""
        self.programmer = []
        self.tester = []
        self.week = 0
        self.budget = 100000
        self.progression = 0.0
        self.soustraitance = 0
        self.sortieAnticiper = False
        self.weekSinceSortieAnticiper = 0
        self.coutSoustraitance = 0

    def nextWeek(self):
        self.week += 1
        if self.week == 52:
            raise Exception("Game over")
        for programmer in self.programmer:
            programmer.nextWeek()
            self.progression += programmer.progression
            self.budget -= programmer.prix

        for tester in self.tester:
            tester.nextWeek()
            self.progression += tester.progression
            self.budget -= tester.prix

        if self.coutSoustraitance != 0:
            self.budget -= self.coutSoustraitance
            self.coutSoustraitance = 0

        if self.sortieAnticiper:
            self.weekSinceSortieAnticiper += 1
            self.budget -= 1000 * self.weekSinceSortieAnticiper
        if self.budget < 0:
            raise Exception("Game over")
        if self.progression >= 100:
            raise Exception("You win")

    def changeName(self, name):
        self.projectName = name

    def changeGamer(self, name):
        self.gamer = name

    def tricher(self):
        self.budget += 10000

    def addProgrammer(self):
        self.programmer.append(Programmer())

    def addTester(self):
        self.tester.append(Tester())

    def sousTraiter(self):
        if self.soustraitance >= 3:
            return
        self.soustraitance += 1
        self.coutSoustraitance += 2000
        self.progression += random.randint(1, 6)

    def sortieAnticiper(self):
        if self.sortieAnticiper:
            return
        self.sortieAnticiper = True
        self.budget += 15000

    def getBudget(self):
        coutProgrammer = 0
        for programmer in self.programmer:
            coutProgrammer += programmer.prix
        coutTester = 0
        for tester in self.tester:
            coutTester += tester.prix

        return {"budget": self.budget, "coutProgrammer": self.coutProgrammer, "coutTester": self.coutTester,
                "coutSoustraitance": self.coutSoustraitance,
                "coutAccesAnticiper": 1000 * (self.weekSinceSortieAnticiper + 1),
                "bilan": self.budget - coutProgrammer - coutTester - self.coutSoustraitance - 1000 * (
                        self.weekSinceSortieAnticiper + 1)}


class Programmer:
    def __init__(self):
        self.prix = 1200
        self.semaine = 0
        self.progression = 1

    def nextWeek(self):
        self.semaine += 1
        if self.semaine == 4:
            self.progression = 1.4


class Tester:
    def __init__(self):
        self.prix = 800
        self.semaine = 0
        self.progression = 0.4

    def nextWeek(self):
        self.semaine += 1
        if self.semaine == 2:
            self.progression = 0.6

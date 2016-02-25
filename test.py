"""id = -1
weapons = {'gun': 10, 'knife': 5}
healt = {'gun': 20, 'knife': 40}
robots = {}


class Robo:

    def __init__(self, color, weap):
        global id
        id = id+1
        self.__weap = weap
        self.__id = id
        if weap in weapons and color not in robots:
            self.__color = color
            self.__damge = weapons[weap]
            self.__healt = healt[weap]
            robots.__setitem__(self.__color, self)
        else:
            raise 'Non hai scelto un arma valida o colore già in uso'
            del self

    @property
    def damge(self):
        return self.__damge

    @property
    def healt(self):
        return self.__healt

    @healt.setter
    def healt(self, damge):
        self.__healt = damge

    def attak(self, enemycolor):
        if enemycolor in robots:
            enemy = robots[enemycolor]
            enemy.healt -= self.__damge

    def __str__(self):
        return "Colore: %s ID: %s Weap: %s Damge: %s Healt: %s" % (self.__color, self.__id, self.__weap,
                                                                   self.__damge, self.__healt)


if __name__ == '__main__':
    rosso = Robo("red", "knife")
    blu = Robo("blu", "gun")
    print(blu.healt)
    rosso.attak("blu")
    print(blu)
    print(blu.damge)
    print(blu.healt)


----test control--------------------------------------------------------------------------------------------------------
import Control

game = Control.Control(10)
griglia = game.refresh()
game.createrobot("red", "gun")
game.createrobot("blu", "knife")
# exception game.createrobo("blu", "gun")
# exception game.createrobot("green", "blabla")
print(game.refresh())
print("-" * 90)
game.move(4, 5, "red")
print(game.refresh())
game.move(11, 2, "red")
print("-" * 90)
print(game.refresh())
game.move(5, 7, "were")
game.move(4, 5, "blu")
print("-" * 90)
print(game.refresh())
game.attack("red", "blu")
game.attack("red", "blu")
game.attack("red", "blu")
game.attack("red", "blu")
game.attack("blu", "blu")
print(game.refresh())
------------------------------------------------------------------------------------------------------------------------

def attack(self, atk, defen):
        if atk in self.__robots and defen in self.__robots:
            att = self.__robots[atk]
            dff = self.__robots[defen]
            dff.healt -= att.damge()
            if dff.healt <= 0:
                del self.__robots[defen]
                self.__grid.delete(defen)
                print("Robot  %s  distrutto" % defen)
"""
import ControlView

game = ControlView.Application
game.start(game)

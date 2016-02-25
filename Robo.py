class Robo:
    def __init__(self, name, weap, id, damge, life):
        self.__weap = weap
        self.__id = id
        self.__name = name
        self.__damge = damge
        self.__healt = life

    def damge(self):
        return self.__damge

    @property
    def healt(self):
        return self.__healt

    @healt.setter
    def healt(self, damge):
        self.__healt = damge

    def __str__(self):
        return "Name: %s Weap: %s Damge: %s Healt: %s" % (self.__name, self.__weap, self.__damge, self.__healt)

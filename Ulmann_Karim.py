#Author Karim Ulmann

class Characters:
    def __init__(self, name, strength):
        self.name = name

        self.strength = strength

    def getName(self):
        return self._name

    def setName(self, name):
        if type(name) != str:
            print('type ERROR')
        else:
            self._name = name

    def getStrength(self):
        return self._strength

    def setStrength(self, strength):  # [0.0-5.0]:
        if type(strength) != float:
            print('type ERROR')
        else:
            if strength < 0.0:
                self._strength = 0.0
            elif strength > 5.0:
                self._strength = 5.0
            else:
                self._strength = strength

    def __str__(self):
        return "%s %s" % (str(self._name), str(self._strength))

    def __gt__(self, other):  # general skeleton of __gt__ to be overridden in subclasses
        if issubclass(self.__class__, Characters) and issubclass(other.__class__, Characters):
            if self._strength > other._strength:
                return True
            else:
                return False
        else:
            print('type ERROR')

    def fight(self, other):
        myCurrent_power = self.getStrength()
        otherCurrent_power = other.getStrength()
        if not isinstance(other, Characters):
            print('type ERROR')

        elif self > other:
            self.setStrength(myCurrent_power + 1)
            print(self.__str__())

        elif other > self:
            other.setStrength(otherCurrent_power + 1.0)
            print(other.__str__())

        else:
            self.setStrength(myCurrent_power - 0.5)
            other.setStrength(otherCurrent_power - 0.5)

    # Declare properties for our attributes
    name = property(getName, setName)
    strength = property(getStrength, setStrength)


class Orc(Characters):
    def __init__(self, name, strength, weapon):
        super().__init__(name, strength)

        self.weapon = weapon

    def getWeapon(self):
        return self._weapon

    def setWeapon(self, weapon):
        if type(weapon) != bool:
            print('type ERROR')
        else:
            self._weapon = weapon

    def __str__(self):
        return "%s %s" % (Characters.__str__(self), self._weapon)

    def __gt__(self, other):  # self will be orc, but other can be human.
        try:
            peoples = [Archer, Knight, Humans, Characters]
            if other.__class__ not in peoples:  # check if other is not a human
                if self._weapon is True and other._weapon is True or self._weapon is False and other._weapon is False:  # other must be Orc
                    if self._strength > other._strength:
                        return True
                    else:
                        return False
                elif self._weapon is False and other._weapon is True:
                    return False
                elif self._weapon is True and not other._weapon:
                    return True
            elif other.__class__ in peoples:  # other must be human here
                if self._weapon is False:  # human will always have weapon
                    return False
                else:
                    if self._strength > other._strength:
                        return True
                    else:
                        return False
        except:
            print('type ERROR')

    def fight(self, other):
        if not isinstance(other, Characters):
            print('type ERROR')
        else:
            Characters.fight(self, other)

    # Declare properties for our attributes
    weapon = property(getWeapon, setWeapon)


class Humans(Characters):
    def __init__(self, name, strength, kingdom):
        super().__init__(name, strength)

        self.kingdom = kingdom

    def getKingdom(self):
        return self._kingdom

    def setKingdom(self, kingdom):
        if type(kingdom) != str:
            print('type ERROR')
            self._kingdom = None
        else:
            self._kingdom = kingdom

    def __str__(self):
        return "%s %s" % (Characters.__str__(self), self._kingdom)

    def __gt__(self, other):
        if issubclass(self.__class__, Characters) and issubclass(other.__class__, Characters):
            if issubclass(other.__class__, Orc):
                if other._weapon is False:
                    return True
            return Characters.__gt__(self, other)

        else:
            print('type ERROR')

    def fight(self, other):
        world = [Orc, Knight, Archer, Humans]
        if other.__class__ not in world:
            print('type ERROR')

        elif isinstance(other, Humans):  # check if other is a human
            print('fight ERROR')

        else:
            if other._weapon:
                Characters.fight(self, other)
            else:
                self.setStrength(self.getStrength() + 1)
                print(self.__str__())

    # Declare properties for our attributes
    kingdom = property(getKingdom, setKingdom)


class Archer(Humans):
    def __init__(self, name, strength, kingdom):
        super().__init__(name, strength, kingdom)


class Knight(Humans):
    def __init__(self, name, strength, kingdom, archers_list):
        super().__init__(name, strength, kingdom)

        if type(archers_list) != list:
            print('type ERROR')
        else:
            self.archers_list = archers_list

    def getArchers_list(self):
        return self._archers_list

    def setArchers_list(self, archers_list):
        # (for example, Aragorn 3.3 Gondor [archer1 2.1 Gondor, archer2 4.2 Gondor])
        # input is a list so work from there
        if type(archers_list) != list:
            print('type ERROR')

        else:
            if archers_list == []:
                self._archers_list = []
            testlist = []
            for i in archers_list:
                if not isinstance(i, Archer):
                    print("archers list ERROR")
                    # 16:2417 Nov at 16:24
                    # Does this not mean that we just remove any archers from the list that aren't from the same kingdom,
                    # but still assign the archers from the correct kingdom? -> Yes if all the elements are archers
                else:  # list now can only contain archers
                    if i.__str__() not in testlist:  # test for duplicates
                        if i._kingdom == self._kingdom:  # must be of the same kingdom
                            testlist.append(i)

                        else:  # only errors exists below
                            print("archers list ERROR")

            self._archers_list = testlist

    def __str__(self):
        return "%s [%s]" % (Humans.__str__(self), ', '.join(map(str, self._archers_list)))

    # Declare properties for our attributes
    archers_list = property(getArchers_list, setArchers_list)

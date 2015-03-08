# Seikou Role Playing Game Kit (Abilities)
#
# Author: Marcus T. Taylor <mtaylor3121@gmail.com>
# Website: https://github.com/mtaylor33/seikous-character-generator
# Copyright: 2012, 2015
#

from math import floor

# Races
SCG_RACE_DRAGONBORN = 'Dragonborn'
SCG_RACE_DWARF = 'Dwarf'
SCG_RACE_ELADRIN = 'Eladrin'
SCG_RACE_ELF = 'Elf'
SCG_RACE_HALFELF = 'Half-elf'
SCG_RACE_HALFLING = 'Halfling'
SCG_RACE_HUMAN = 'Human'
SCG_RACE_TIEFLING = 'Tiefling'


class Abilities:

    def __init__(self, **kwargs):
        if 'race' in kwargs.keys():
            self._race = kwargs['race']
        else:
            self._race = 'Human'
        if 'strength' in kwargs.keys():
            self.__set_strength(kwargs['strength'])
        else:
            self.__set_strength(16)
        if 'dexterity' in kwargs.keys():
            self.__set_dexterity(kwargs['dexterity'])
        else:
            self.__set_dexterity(14)
        if 'constitution' in kwargs.keys():
            self.__set_constitution(kwargs['constitution'])
        else:
            self.__set_constitution(13)
        if 'intelligence' in kwargs.keys():
            self.__set_intelligence(kwargs['intelligence'])
        else:
            self.__set_intelligence(12)
        if 'wisdom' in kwargs.keys():
            self.__set_wisdom(kwargs['wisdom'])
        else:
            self.__set_wisdom(11)
        if 'charisma' in kwargs.keys():
            self.__set_charisma(kwargs['charisma'])
        else:
            self.__set_charisma(10)

    def __get_race(self):
        """Returns the racial value."""
        return self._race

    def __set_charisma(self, value):
        """Sets charisma score value.

        Args:
            value: Value to set charisma score to.

        """
        if self.__get_race() == SCG_RACE_HALFLING \
                or self.__get_race() == SCG_RACE_HALFELF \
                or self.__get_race() == SCG_RACE_TIEFLING:
            self._charisma = int(value) + 2
        else:
            self._charisma = int(value)

    def __set_constitution(self, value):
        """Sets constitution score value.

        Args:
            value: Value to set constitution score to.

        """
        if self.__get_race() == SCG_RACE_DRAGONBORN \
                or self.__get_race() == SCG_RACE_DWARF \
                or self.__get_race() == SCG_RACE_HALFELF:
            self._constitution = int(value) + 2
        else:
            self._constitution = int(value)

    def __set_dexterity(self, value):
        """Sets dexterity score value.

        Args:
            value: Value to set dexterity score to.

        """
        if self.__get_race() == SCG_RACE_ELADRIN \
                or self.__get_race() == SCG_RACE_ELF \
                or self.__get_race() == SCG_RACE_HALFLING:
            self._dexterity = int(value) + 2
        else:
            self._dexterity = int(value)

    def __set_intelligence(self, value):
        """Sets intelligence score value.

        Args:
            value: Value to set intelligence score to.

        """
        if self.__get_race() == SCG_RACE_ELADRIN \
                or self.__get_race() == SCG_RACE_TIEFLING:
            self._intelligence = int(value) + 2
        else:
            self._intelligence = int(value)

    def __set_strength(self, value):
        """Sets strength score value.

        Args:
            value: Value to set strength score to.

        """
        if self.__get_race() == SCG_RACE_DRAGONBORN:
            self._strength = int(value) + 2
        else:
            self._strength = int(value)

    def __set_wisdom(self, value):
        """Sets wisdom score value.

        Args:
            value: Value to set wisdom score to.

        """
        if self.__get_race() == SCG_RACE_DWARF \
                or self.__get_race() == SCG_RACE_ELF:
            self._wisdom = int(value) + 2
        else:
            self._wisdom = int(value)

    def get_charisma(self):
        """Returns charisma score value."""
        return self._charisma

    def get_constitution(self):
        """Returns constitution score value."""
        return self._constitution

    def get_dexterity(self):
        """Returns dexterity score value."""
        return self._dexterity

    def get_intelligence(self):
        """Returns intelligence score value."""
        return self._intelligence

    @staticmethod
    def get_modifier(value):
        """Returns modifier for specified ability type.

        Args:
            value: The value to retrieve a modifier for.
        Returns:
            The modifier for the requested score.

        """
        return floor((value - 10)/2)

    def get_strength(self):
        """Returns strength score value."""
        return self._strength

    def get_wisdom(self):
        """Returns wisdom score value."""
        return self._wisdom

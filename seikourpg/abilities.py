# Seikou Role Playing Game Kit (Abilities)
#
# Author: Marcus T. Taylor <mtaylor3121@gmail.com>
# Website: https://github.com/mtaylor33/seikourpg
# Copyright: 2012, 2015
#

from math import floor
import sqlite3
from seikourpg.settings import *


class Abilities:

    def __init__(self, **kwargs):
        if 'race' in kwargs:
            self._race = kwargs['race']
        else:
            self._race = 'Human'
        if 'strength' in kwargs:
            self._strength = kwargs['strength']
        else:
            self._strength = 15
        if 'dexterity' in kwargs:
            self._dexterity = kwargs['dexterity']
        else:
            self._dexterity = 14
        if 'constitution' in kwargs:
            self._constitution = kwargs['constitution']
        else:
            self._constitution = 13
        if 'intelligence' in kwargs:
            self._intelligence = kwargs['intelligence']
        else:
            self._intelligence = 12
        if 'wisdom' in kwargs:
            self._wisdom = kwargs['wisdom']
        else:
            self._wisdom = 10
        if 'charisma' in kwargs:
            self._charisma = kwargs['charisma']
        else:
            self._charisma = 8
        # Apply racial bonuses, if applicable
        bonus = self.__get_bonus()
        if 'strength' in bonus:
            self.__set_strength(bonus['strength'])
        if 'dexterity' in bonus:
            self.__set_dexterity(bonus['dexterity'])
        if 'constitution' in bonus:
            self.__set_constitution(bonus['constitution'])
        if 'intelligence' in bonus:
            self.__set_intelligence(bonus['intelligence'])
        if 'wisdom' in bonus:
            self.__set_wisdom(bonus['wisdom'])
        if 'charisma' in bonus:
            self.__set_charisma(bonus['charisma'])

    def __get_bonus(self):
        """Retrieves racial ability score bonuses.

        Returns:
            Returns a dictionary of ability score bonuses.

        """
        settings = Settings()
        conn = sqlite3.connect(settings.get_database())
        cursor = conn.cursor()
        sql = 'SELECT strength,dexterity,constitution,' \
              'intelligence,wisdom,charisma FROM races ' \
              'WHERE name=:race'
        cursor.execute(sql, {'race': self.__get_race()})
        bonuses = cursor.fetchall()
        conn.close()
        bonus_list = {}
        for bonus in bonuses:
            strength = bonus[0]
            if strength is not 0:
                bonus_list['strength'] = strength
            dexterity = bonus[1]
            if dexterity is not 0:
                bonus_list['dexterity'] = dexterity
            constitution = bonus[2]
            if constitution is not 0:
                bonus_list['constitution'] = constitution
            intelligence = bonus[3]
            if intelligence is not 0:
                bonus_list['intelligence'] = intelligence
            wisdom = bonus[4]
            if wisdom is not 0:
                bonus_list['wisdom'] = wisdom
            charisma = bonus[5]
            if charisma is not 0:
                bonus_list['charisma'] = charisma
        return bonus_list

    def __get_race(self):
        """Returns the racial value."""
        return self._race

    def __set_charisma(self, value):
        """Sets charisma score value.

        Args:
            value: Value to set charisma score to.

        """
        self._charisma += int(value)

    def __set_constitution(self, value):
        """Sets constitution score value.

        Args:
            value: Value to set constitution score to.

        """
        self._constitution += int(value)

    def __set_dexterity(self, value):
        """Sets dexterity score value.

        Args:
            value: Value to set dexterity score to.

        """
        self._dexterity += int(value)

    def __set_intelligence(self, value):
        """Sets intelligence score value.

        Args:
            value: Value to set intelligence score to.

        """
        self._intelligence += int(value)

    def __set_strength(self, value):
        """Sets strength score value.

        Args:
            value: Value to set strength score to.

        """
        self._strength += int(value)

    def __set_wisdom(self, value):
        """Sets wisdom score value.

        Args:
            value: Value to set wisdom score to.

        """
        self._wisdom += int(value)

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

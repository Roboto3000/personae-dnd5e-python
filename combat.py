# Seikou Role Playing Game Kit (Combat)
#
# Author: Marcus T. Taylor <mtaylor3121@gmail.com>
# Website: https://github.com/mtaylor33/seikous-character-generator
# Copyright: 2012, 2015
#

from math import floor


class Combat:

    # Attack types
    ATTACK_TYPE_BASE = 200
    ATTACK_TYPE_MELEE = 201
    ATTACK_TYPE_RANGED = 202

    # Save types
    SAVE_TYPE_FORTITUDE = 300
    SAVE_TYPE_REFLEX = 301
    SAVE_TYPE_WILL = 302

    def __init__(self, **kwargs):
        if 'race' in kwargs.keys():
            self._race = kwargs['race']
        else:
            self._race = 'Human'
        if 'class_' in kwargs.keys():
            self._class = kwargs['class_']
        else:
            self._class = 'Fighter'
        if 'level' in kwargs.keys():
            self._level = int(kwargs['level'])
        else:
            self._level = 1
        self.__set_hp()
        self._hp = self.get_hp()
        if 'charisma' in kwargs.keys():
            self._charisma = int(kwargs['charisma'])
        else:
            self._charisma = 10
        if 'constitution' in kwargs.keys():
            self._constitution = int(kwargs['constitution'])
        else:
            self._constitution = 10
        if 'dexterity' in kwargs.keys():
            self._dexterity = int(kwargs['dexterity'])
        else:
            self._dexterity = 10
        if 'intelligence' in kwargs.keys():
            self._intelligence = int(kwargs['intelligence'])
        else:
            self._intelligence = 10
        if 'strength' in kwargs.keys():
            self._strength = int(kwargs['strength'])
        else:
            self._strength = 10
        if 'wisdom' in kwargs.keys():
            self._wisdom = int(kwargs['wisdom'])
        else:
            self._wisdom = 10

    def __get_class(self):
        """Returns class value."""
        return self._class

    def __get_level(self):
        """Returns the level value."""
        return self._level

    @staticmethod
    def __get_modifier(value):
        """Returns modifier for specified ability type.

        Args:
            value: The value to retrieve a modifier for.
        Returns:
            The modifier for the requested score.

        """
        return floor((value - 10)/2)

    def __get_race(self):
        """Returns the racial value."""
        return self._race

    def __set_hp(self):
        """Sets hit points for character based on class."""
        base_value = {
            'Cleric': 12,
            'Fighter': 15,
            'Paladin': 15,
            'Ranger': 12,
            'Rogue': 12,
            'Warlock': 12,
            'Warlord': 12,
            'Wizard': 10
        }
        additional_value = {
            'Cleric': 5,
            'Fighter': 6,
            'Paladin': 6,
            'Ranger': 5,
            'Rogue': 5,
            'Warlock': 5,
            'Warlord': 5,
            'Wizard': 4
        }
        try:
            if self.__get_class() not in base_value or additional_value:
                raise IndexError
        except IndexError:
            self._class = 'Fighter'
        finally:
            hit_points = 0
            base_hp = base_value[self.__get_class()]
            bonus_hp = self.__get_modifier(self._constitution)
            if self.__get_level() >= 1:
                hit_points = base_hp + bonus_hp
            if self.__get_level() > 1:
                base_hp = additional_value[self.__get_class()]
                addition = (self.__get_level() - 1) * (base_hp + bonus_hp)
                hit_points += addition
            self._hp = hit_points

    def get_ac(self):
        """Returns armor class value.

        Returns:
            Returns the armor class value.

        """
        base = floor(self.__get_level()/2)
        if base < 1:
            base = 1
        return base + 10

    def get_attack(self, attack_type):
        """Returns base, melee or ranged attack values.

        Args:
            attack_type: The requested attack type.
        Returns:
            Returns the value for the requested attack type.

        """
        base = floor(self.__get_level()/2)
        if base < 1:
            base = 1
        if attack_type is self.ATTACK_TYPE_MELEE:
            return base + self.__get_modifier(self._strength)
        if attack_type is self.ATTACK_TYPE_RANGED:
            return base + self.__get_modifier(self._dexterity)
        if attack_type is self.ATTACK_TYPE_BASE:
            return base

    def get_hp(self):
        """Returns the hit point value."""
        return self._hp

    def get_save(self, save_type):
        """Returns value for specified save type.

        Args:
            save_type: The type of save to be requested.
        Returns:
            Returns the value of the requested save.

        """
        base = floor(self.__get_level()/2)
        if base < 1:
            base = 1
        if save_type is self.SAVE_TYPE_FORTITUDE:
            return base + self.__get_modifier(self._constitution)
        if save_type is self.SAVE_TYPE_REFLEX:
            return base + self.__get_modifier(self._dexterity)
        if save_type is self.SAVE_TYPE_WILL:
            return base + self.__get_modifier(self._wisdom)
        return base

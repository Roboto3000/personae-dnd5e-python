# Seikou Role Playing Game Kit (Feats)
#
# Author: Marcus T. Taylor <mtaylor3121@gmail.com>
# Website: https://github.com/mtaylor33/seikourpg
# Copyright: 2012, 2015
#

import sqlite3
from seikourpg.settings import *


class Feats:

    def __init__(self, **kwargs):
        if 'class_' in kwargs:
            self._class = kwargs['class_']
        else:
            self._class = 'Fighter'
        if 'level' in kwargs:
            self._level = int(kwargs['level'])
        else:
            self._level = 1
        if 'charisma' in kwargs:
            self._charisma = int(kwargs['charisma'])
        else:
            self._charisma = 8
        if 'constitution' in kwargs:
            self._constitution = int(kwargs['constitution'])
        else:
            self._constitution = 13
        if 'dexterity' in kwargs:
            self._dexterity = int(kwargs['dexterity'])
        else:
            self._dexterity = 14
        if 'intelligence' in kwargs:
            self._intelligence = int(kwargs['intelligence'])
        else:
            self._intelligence = 12
        if 'strength' in kwargs:
            self._strength = int(kwargs['strength'])
        else:
            self._strength = 15
        if 'wisdom' in kwargs:
            self._wisdom = int(kwargs['wisdom'])
        else:
            self._wisdom = 10

    def __get_proficiencies(self):
        """Returns a list of required proficiencies for a feat.

        Returns:
            Returns a list of required armor/weapon proficiencies.
        """
        settings = Settings()
        conn = sqlite3.connect(settings.get_database())
        cursor = conn.cursor()
        sql = "SELECT armors,weapons FROM classes WHERE name=:class"
        cursor.execute(sql, {'class': self.__get_class()})
        proficiency_list = cursor.fetchone()
        proficiency_list = (proficiency_list[0][:], proficiency_list[1][:])
        proficiency_list = '|'.join(proficiency_list)
        conn.close()
        proficiency_list = proficiency_list.split('|')
        if '-' in proficiency_list:
            proficiency_list.remove('-')
        return proficiency_list

    def __get_charisma(self):
        """Returns charisma value."""
        return self._charisma

    def __get_class(self):
        """Returns class value."""
        return self._class

    def __get_constitution(self):
        """Returns constitution value."""
        return self._constitution

    def __get_dexterity(self):
        """Returns dexterity value."""
        return self._dexterity

    def __get_intelligence(self):
        """Returns intelligence value."""
        return self._intelligence

    def __get_level(self):
        """Returns level value."""
        return self._level

    @staticmethod
    def __get_requirements(feat_name):
        """Get requirements for the requested feat.

        Args:
            feat_name: The feat to retrieve requirements for.
        Returns:
            Returns dictionary of requested requirements for feat.

        """
        settings = Settings()
        conn = sqlite3.connect(settings.get_database())
        cursor = conn.cursor()
        sql = "SELECT proficiency,strength,dexterity," \
            "constitution,intelligence,wisdom,charisma " \
            "FROM feats WHERE name=:feat"
        cursor.execute(sql, {'feat': feat_name})
        _requirements = cursor.fetchall()
        _requirements = _requirements[0][:]
        conn.close()
        requirements = {
            'proficiency': _requirements[0],
            'strength': _requirements[1],
            'dexterity': _requirements[2],
            'constitution': _requirements[3],
            'intelligence': _requirements[4],
            'wisdom': _requirements[5],
            'charisma': _requirements[6]
        }
        return requirements

    def __get_strength(self):
        """Returns strength value."""
        return self._strength

    def __get_wisdom(self):
        """Returns wisdom value."""
        return self._wisdom

    @staticmethod
    def get_feats():
        """Generates a dictionary of acceptable selections.

        Returns:
            Returns a dictionary of acceptable feats.

        """
        settings = Settings()
        conn = sqlite3.connect(settings.get_database())
        cursor = conn.cursor()
        feats_list = []
        cursor.execute("SELECT name FROM feats")
        feats = cursor.fetchall()
        conn.close()
        for feat_item in feats:
            feat_name = feat_item[0][:]
            feats_list.append(feat_name)
        feats_list.sort()
        feats_dict = {}
        index = 1
        for feat_name in feats_list:
            feats_dict[index] = feat_name
            index += 1
        return feats_dict

    def has_requirements(self, feat_name):
        """Checks if requirements met for feat.

        Args:
            feat_name: The feat to retrieve requirements for.
        Returns:
            Returns True if requirements met, False if not.

        """
        # Ritual Caster Check
        if feat_name is 'Ritual Caster':
            if self.__get_intelligence() < 13 and self.__get_wisdom() < 13:
                return False
        # Spell caster Check
        caster = {
            'Elemental Adept',
            'Spell Sniper',
            'War Caster'
        }
        if feat_name in caster:
            if not self.is_caster():
                return False
        requirement = self.__get_requirements(feat_name)
        # Proficiency Check
        if requirement['proficiency'] != '-':
            if requirement['proficiency'] not in self.__get_proficiencies():
                return False
        # Strength Check
        if requirement['strength'] > self.__get_strength():
            return False
        # Dexterity Check
        if requirement['dexterity'] > self.__get_dexterity():
            return False
        # Constitution Check
        if requirement['constitution'] > self.__get_constitution():
            return False
        # Intelligence Check
        if requirement['intelligence'] > self.__get_intelligence():
            return False
        # Wisdom Check
        if requirement['wisdom'] > self.__get_wisdom():
            return False
        # Charisma Check
        if requirement['charisma'] > self.__get_charisma():
            return False
        return True

    def is_caster(self):
        """Determines if character is a spell caster.

        Returns:
            Returns True if spell caster, False if not.

        """
        if self.__get_class() is 'Bard':
            if not self.is_level(1):
                return False
        if self.__get_class() is 'Cleric':
            if not self.is_level(1):
                return False
        if self.__get_class() is 'Druid':
            if not self.is_level(1):
                return False
        if self.__get_class() is 'Fighter':
            if not self.is_level(3):
                return False
        if self.__get_class() is 'Paladin':
            if not self.is_level(2):
                return False
        if self.__get_class() is 'Ranger':
            if not self.is_level(2):
                return False
        if self.__get_class() is 'Rogue':
            if not self.is_level(3):
                return False
        if self.__get_class() is 'Sorcerer':
            if not self.is_level(1):
                return False
        if self.__get_class() is 'Warlock':
            if not self.is_level(1):
                return False
        if self.__get_class() is 'Wizard':
            if not self.is_level(1):
                return False
        return True

    def is_level(self, min_level=1):
        """Checks if character is of a certain level or higher."""
        if self.__get_level() >= min_level:
            return True
        return False

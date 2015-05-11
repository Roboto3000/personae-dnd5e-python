# Seikou Role Playing Game Kit (Skills)
#
# Author: Marcus T. Taylor <mtaylor3121@gmail.com>
# Website: https://github.com/mtaylor33/seikourpg
# Copyright: 2012, 2015
#

from math import floor
import sqlite3
from seikourpg.settings import *


class Skills:

    def __init__(self, **kwargs):
        if 'race' in kwargs:
            self._race = kwargs['race']
        else:
            self._race = 'Human'
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
            self._charisma = 10
        if 'constitution' in kwargs:
            self._constitution = int(kwargs['constitution'])
        else:
            self._constitution = 10
        if 'dexterity' in kwargs:
            self._dexterity = int(kwargs['dexterity'])
        else:
            self._dexterity = 10
        if 'intelligence' in kwargs:
            self._intelligence = int(kwargs['intelligence'])
        else:
            self._intelligence = 10
        if 'strength' in kwargs:
            self._strength = int(kwargs['strength'])
        else:
            self._strength = 10
        if 'wisdom' in kwargs:
            self._wisdom = int(kwargs['wisdom'])
        else:
            self._wisdom = 10

    def __get_class(self):
        """Returns class value."""
        return self._class

    def __get_level(self):
        """Returns character level value."""
        return self._level

    def get_allotted(self):
        """Returns allowed number of skills for class.

        Returns:
            Returns the number of allotted skills by class.

        """
        num_of_skills = 0
        tier4 = ('Rogue',)
        tier3 = ('Bard', 'Ranger')
        tier2 = (
            'Barbarian',
            'Cleric',
            'Druid',
            'Fighter',
            'Monk',
            'Paladin',
            'Sorcerer',
            'Warlock',
            'Wizard'
        )
        if self.__get_class() in tier4:
            num_of_skills = 4
        if self.__get_class() in tier3:
            num_of_skills = 3
        if self.__get_class() in tier2:
            num_of_skills = 2
        if self.__get_class() not in tier2 or tier3 or tier4:
            num_of_skills = 2
        return num_of_skills

    def get_modifier(self, skill_name):
        """Returns skill modifier value based on skill.

        Args:
            skill_name: Skill to return a modifier for.
        Returns:
            Returns modifier for the specified skill.

        """
        settings = Settings()
        conn = sqlite3.connect(settings.get_database())
        cursor = conn.cursor()
        sql = 'SELECT ability FROM skills WHERE name=:skill'
        cursor.execute(sql, {'skill': skill_name})
        abilities = cursor.fetchall()
        conn.close()
        score = 0
        for ability in abilities:
            if ability is 'Strength':
                score = self._strength
            if ability is 'Dexterity':
                score = self._dexterity
            if ability is 'Intelligence':
                score = self._constitution
            if ability is 'Wisdom':
                score = self._wisdom
            if ability is 'Charisma':
                score = self._charisma
        return int(floor((score - 10)/2))

    def get_skills(self, show_all=False):
        """Returns a list of skills for specified class.

        Args:
            show_all: If True, shows all skills regardless of class.

        Returns:
            Returns a dictionary of allowable skills by class.

        """
        settings = Settings()
        conn = sqlite3.connect(settings.get_database())
        cursor = conn.cursor()
        s = "SELECT name FROM skills WHERE %s='Y'" % self.__get_class().lower()
        if show_all:
            s = 'SELECT name FROM skills'
        try:
            cursor.execute(s)
            skills = cursor.fetchall()
            conn.close()
            skill_list = {}
            index = 1
            for skill_name in skills:
                skill_list[index] = skill_name[0][:]
                index += 1
            return skill_list
        except sqlite3.OperationalError:
            return None

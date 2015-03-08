# Seikou Role Playing Game Kit (Skills)
#
# Author: Marcus T. Taylor <mtaylor3121@gmail.com>
# Website: https://github.com/mtaylor33/seikous-character-generator
# Copyright: 2012, 2015
#

from math import floor
import os
import sqlite3


# SCG
SCG_CONFIG_CORE = os.path.dirname(__file__)
SCG_CONFIG_DATABASE = os.path.join(SCG_CONFIG_CORE, 'database', 'SCG.sqlite')

# Races
SCG_RACE_DRAGONBORN = 'Dragonborn'
SCG_RACE_DWARF = 'Dwarf'
SCG_RACE_ELADRIN = 'Eladrin'
SCG_RACE_ELF = 'Elf'
SCG_RACE_HALFELF = 'Half-elf'
SCG_RACE_HALFLING = 'Halfling'
SCG_RACE_HUMAN = 'Human'
SCG_RACE_TIEFLING = 'Tiefling'


class Skills:

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

    @staticmethod
    def __get_modifier(score):
        """Returns modifier value based on score.

        Args:
            score: Score to return the modifier for.
        Returns:
            Returns modifier for the specified score.

        """
        return int(floor((score - 10)/2))

    def get_allotted(self):
        """Returns allowed number of skills for class.

        Returns:
            Returns the number of allotted skills by class.

        """
        num_of_skills = 0
        tier4 = ('Ranger', 'Rogue', 'Warlock', 'Warlord')
        if self.__get_class() in tier4:
            num_of_skills = 4
        tier3 = ('Cleric', 'Fighter', 'Paladin', 'Wizard')
        if self.__get_class() in tier3:
            num_of_skills = 3
        if self.__get_class() not in tier4 or tier3:
            num_of_skills = 3
        if self._race == SCG_RACE_HUMAN:
            num_of_skills += 1
        return num_of_skills

    @staticmethod
    def get_list():
        """Returns a complete listing of skills.

        Returns:
            Returns a list of valid skills regardless of class.

        """
        conn = sqlite3.connect(SCG_CONFIG_DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT name FROM skills')
        skills = cursor.fetchall()
        conn.close()
        skill_list = []
        for skill_name in skills:
            skill_list.append(skill_name[0][:])
        return skill_list

    def get_rank(self, skill_name):
        """Returns skill rank for specified skill.

        Args:
            skill_name: Skill to return a skill rank for.
        Returns:
            Returns skill rank for the requested skill,
            -1 if skill name is not a valid skill.

        """
        if not self.is_skill(skill_name):
            return -1
        # Get base rank
        rank = int(floor(self._level/2))
        if rank < 1:
            rank = 1
        # Get ability modifier bonus
        conn = sqlite3.connect(SCG_CONFIG_DATABASE)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT ability FROM skills WHERE name=:skill",
            {'skill': skill_name}
        )
        ability = cursor.fetchone()
        ability = ability[0][:]
        modifier = 0
        if ability == 'Charisma':
            modifier = self.__get_modifier(self._charisma)
        if ability == 'Constitution':
            modifier = self.__get_modifier(self._constitution)
        if ability == 'Dexterity':
            modifier = self.__get_modifier(self._dexterity)
        if ability == 'Intelligence':
            modifier = self.__get_modifier(self._intelligence)
        if ability == 'Strength':
            modifier = self.__get_modifier(self._strength)
        if ability == 'Wisdom':
            modifier = self.__get_modifier(self._wisdom)
        # Apply bonus modifiers for race
        if skill_name == 'Dungeoneering' and self.is_race(SCG_RACE_DWARF):
            return rank + modifier + 2
        if skill_name == 'Endurance' and self.is_race(SCG_RACE_DWARF):
            return rank + modifier + 2
        if skill_name == 'Arcana' and self.is_race(SCG_RACE_ELADRIN):
            return rank + modifier + 2
        if skill_name == 'History' and self.is_race(SCG_RACE_ELADRIN):
            return rank + modifier + 2
        if skill_name == 'Nature' and self.is_race(SCG_RACE_ELF):
            return rank + modifier + 2
        if skill_name == 'Perception' and self.is_race(SCG_RACE_ELF):
            return rank + modifier + 2
        if skill_name == 'Diplomacy' and self.is_race(SCG_RACE_HALFELF):
            return rank + modifier + 2
        if skill_name == 'Insight' and self.is_race(SCG_RACE_HALFELF):
            return rank + modifier + 2
        if skill_name == 'Acrobatics' and self.is_race(SCG_RACE_HALFLING):
            return rank + modifier + 2
        if skill_name == 'Thievery' and self.is_race(SCG_RACE_HALFLING):
            return rank + modifier + 2
        return rank + modifier

    def get_skills(self):
        """Returns a list of skills for specified class.

        Returns:
            Returns a dictionary of allowable skills by class.

        """
        conn = sqlite3.connect(SCG_CONFIG_DATABASE)
        cursor = conn.cursor()
        s = "SELECT name FROM skills WHERE %s='Y'" % self.__get_class().lower()
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

    def is_race(self, race_type):
        """Checks if character is a particular race.

        Args:
            race_type: Race type to check if member of.
        Returns:
            Returns True if character is race, False if not.

        """
        if self._race == race_type:
            return True
        return False

    def is_skill(self, skill_name):
        """Checks if skill is valid.

        Args:
            skill_name: Skill to check is valid.
        Returns:
            Returns True if valid, False if not.

        """
        if skill_name in self.get_list():
            return True
        return False

    def set_skill(self, skill_name):
        """Set a skill_name a rank.

        Args:
            skill_name: Skill to set rank for.
        Returns:
            Returns a dictionary of skill name and rank.

        """
        if self.is_skill(skill_name):
            return {skill_name: self.get_rank(skill_name)}
        return {}
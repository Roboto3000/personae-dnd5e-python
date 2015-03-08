# Seikou Role Playing Game Kit (Feats)
#
# Author: Marcus T. Taylor <mtaylor3121@gmail.com>
# Website: https://github.com/mtaylor33/seikous-character-generator
# Copyright: 2012, 2015
#

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


class Feats:

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
        if 'deity' in kwargs.keys():
            self._deity = kwargs['deity']
        else:
            self._deity = 'Faithless'
        if 'skills' in kwargs.keys():
            self._skills = kwargs['skills']
        else:
            self._skills = {}
        if 'feats' in kwargs.keys():
            self._feats = kwargs['feats']
        else:
            self._feats = []
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

    @staticmethod
    def __get_classes(feat_name):
        """Returns a list of required classes for a feat.

        Args:
            feat_name: Feat to retrieve required classes for.
        Returns:
            Returns None or a list of required feats.
        """
        conn = sqlite3.connect(SCG_CONFIG_DATABASE)
        cursor = conn.cursor()
        sql = "SELECT job FROM feats WHERE name=:feat"
        cursor.execute(sql, {'feat': feat_name})
        class_list = cursor.fetchone()
        class_list = class_list[0][:]
        conn.close()
        if class_list != '-':
            return class_list.split('|')
        return None

    def __get_charisma(self):
        """Returns charisma value."""
        return self._charisma

    def __get_class(self):
        """Returns class value."""
        return self._class

    def __get_constitution(self):
        """Returns constitution value."""
        return self._constitution

    def __get_deity(self):
        """Returns deity value."""
        return self._deity

    def __get_dexterity(self):
        """Returns dexterity value."""
        return self._dexterity

    def __get_intelligence(self):
        """Returns intelligence value."""
        return self._intelligence

    def __get_level(self):
        """Returns level value."""
        return self._level

    def __get_race(self):
        """Returns race value."""
        return self._race

    def __get_strength(self):
        """Returns strength value."""
        return self._strength

    def __get_wisdom(self):
        """Returns wisdom value."""
        return self._wisdom

    def get_allotted(self):
        """Return allotted number of allowed feats."""
        num_of_feats = 1
        if self.__get_race() == SCG_RACE_HUMAN:
            num_of_feats += 1
        for level in range(1, self.__get_level()):
            if level is 1 or level is 11 or level is 21:
                num_of_feats += 1
                continue
            if (level % 2) is 0:
                num_of_feats += 1
        return num_of_feats

    def get_feats(self):
        """Generates a dictionary of acceptable selections.

        Returns:
            Returns a dictionary of acceptable feats.

        """
        conn = sqlite3.connect(SCG_CONFIG_DATABASE)
        cursor = conn.cursor()
        feats_list = []
        # Epic level feats
        if self.__get_level() >= 21:
            cursor.execute("SELECT name FROM feats WHERE type='epic'")
            feats = cursor.fetchall()
            for feat_item in feats:
                feat_name = feat_item[0][:]
                feats_list.append(feat_name)
        # Paragon level feats
        if self.__get_level() >= 11:
            cursor.execute("SELECT name FROM feats WHERE type='paragon'")
            feats = cursor.fetchall()
            for feat_item in feats:
                feat_name = feat_item[0][:]
                feats_list.append(feat_name)
        # Heroic level feats
        if self.__get_level() >= 1:
            cursor.execute("SELECT name FROM feats WHERE type='heroic'")
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
        conn = sqlite3.connect(SCG_CONFIG_DATABASE)
        cursor = conn.cursor()
        sql = "SELECT race,deity,job,feat,skill, " \
            "strength,dexterity,constitution, " \
            "intelligence,wisdom,charisma " \
            "FROM feats WHERE name=:feat"
        cursor.execute(sql, {'feat': feat_name})
        requirements = cursor.fetchall()
        conn.close()
        for requirement in requirements:
            # Check race
            if requirement[0] != '-':
                if requirement[0] != self.__get_race():
                    return False
            # Check deity
            if requirement[1] != '-':
                if requirement[1] != self.__get_deity():
                    return False
            # Check class
            if requirement[2] != '-':
                classes = self.__get_classes(feat_name)
                if feat_name.startswith('Weapon Proficiency'):
                    if self.__get_class() in classes:
                        return False
                else:
                    if self.__get_class() not in classes:
                        return False
            # Check feats
            if requirement[3] != '-':
                if requirement[3] not in self._feats:
                    return False
            # Check skills (Skill Focus hack)
            if feat_name.startswith('Skill Focus'):
                skill_name = requirement[4]
                if skill_name not in self._skills:
                    return False
            # Check skills (Skill Training hack)
            elif feat_name.startswith('Skill Training'):
                skill_name = requirement[4][1:]
                if skill_name in self._skills:
                    return False
            # Check skills
            elif requirement[4] != '-':
                if requirement[4] not in self._skills:
                    return False
            # Strength Check
            if requirement[5] > self.__get_strength():
                return False
            # Dexterity Check
            if requirement[6] > self.__get_dexterity():
                return False
            # Constitution Check
            if requirement[7] > self.__get_constitution():
                return False
            # Intelligence Check
            if requirement[8] > self.__get_intelligence():
                return False
            # Wisdom Check
            if requirement[9] > self.__get_wisdom():
                return False
            # Charisma Check
            if requirement[10] > self.__get_charisma():
                return False
        return True

    def set_skills(self, value):
        try:
            if not isinstance(value, dict):
                raise ValueError
        except ValueError:
            pass
        self._skills = value

# Seikou Role Playing Game Kit (Powers)
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


class Powers:

    # Power types
    POWERS_TYPE_AT_WILL = 'At-Will'
    POWERS_TYPE_DAILY = 'Daily'
    POWERS_TYPE_ENCOUNTER = 'Encounter'
    POWERS_TYPE_UTILITY = 'Utility'

    def __init__(self):
        self.powers_race = 'Human'
        self.powers_class = 'Fighter'
        self.powers_level = 1
        self.powers_mine = []
        self.powers_at_will = []
        self.powers_encounter = []
        self.powers_daily = []
        self.powers_utility = []

    def get_allotted(self, power_type):
        """Returns allotted number of powers by power type and level.

        Args:
            power_type: Power type to retrieve the allotted number for.
        Returns:
            Returns the number of allotted powers by power type.

        """
        power_count = 0
        if power_type == self.POWERS_TYPE_AT_WILL:
            if self.get_race() == SCG_RACE_HUMAN:
                power_count = 3
            else:
                power_count = 2
        if power_type == self.POWERS_TYPE_DAILY:
            level = 1
            while level <= self.get_level():
                if level in (1, 5, 9, 20):
                    power_count += 1
                level += 1
        if power_type == self.POWERS_TYPE_ENCOUNTER:
            level = 1
            while level <= self.get_level():
                if level in (1, 3, 7, 11):
                    power_count += 1
                level += 1
        if power_type == self.POWERS_TYPE_UTILITY:
            level = 1
            while level <= self.get_level():
                if level in (2, 6, 10, 12, 16, 22, 26):
                    power_count += 1
                level += 1
        return power_count

    def get_class(self):
        """Returns class value."""
        return self.powers_class

    def get_level(self):
        """Returns level value."""
        return self.powers_level

    def get_list(self, power_type):
        """Returns a dictionary of powers by class, level and type.

        Args:
            power_type: Power type to create list from.
        Returns:
            Returns a dictionary of powers by power type.

        """
        conn = sqlite3.connect(SCG_CONFIG_DATABASE)
        cursor = conn.cursor()
        sql = 'SELECT name FROM powers ' \
              'WHERE class=:class ' \
              'AND level<=:level ' \
              'AND type=:type'
        values = {
            'class': self.get_class(),
            'level': self.get_level(),
            'type': power_type
        }
        cursor.execute(sql, values)
        powers_list = cursor.fetchall()
        conn.close()
        powers_dict = {}
        index = 1
        for power_name in powers_list:
            powers_dict[index] = power_name[0]
            index += 1
        return powers_dict

    def get_powers(self):
        """Returns list of powers."""
        self.powers_mine.sort()
        return self.powers_mine

    def get_race(self):
        """Returns race value."""
        return self.powers_race

    def has_allotted(self, power_type):
        """Check if allotted number of powers by power type reached.

        Args:
            power_type: Power type to check for allotted powers.
        Returns:
            Returns True if allotted number of powers reached, False if not.

        """
        power_count = self.get_allotted(power_type)
        if power_type == self.POWERS_TYPE_AT_WILL:
            if len(self.powers_at_will) is power_count:
                return True
        if power_type == self.POWERS_TYPE_DAILY:
            if len(self.powers_daily) is power_count:
                return True
        if power_type == self.POWERS_TYPE_ENCOUNTER:
            if len(self.powers_encounter) is power_count:
                return True
        if power_type == self.POWERS_TYPE_UTILITY:
            if len(self.powers_utility) is power_count:
                return True
        return False

    def set_class(self, class_name):
        self.powers_class = class_name

    def set_level(self, value):
        self.powers_level = int(value)

    def set_race(self, race_name):
        self.powers_race = race_name

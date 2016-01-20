# Personae RPG Library
#
# Author: Marcus T. Taylor <mtaylor3121@gmail.com>
# Website: https://github.com/mtaylor33/libpersonae
# Copyright: 2012, 2015
#

from math import floor
from random import randint
import os
import sys
import sqlite3

__all__ = [
    'abilities',
    'dice',
    'feats',
    "information",
    "origins",
    "skills"
]
__version__ = '20160120'


def get_version():
    """Returns the version number string."""
    return __version__


#######################################################################
# Personae Role Playing Game Kit (Abilities)
#######################################################################
class Abilities:

    def __init__(self, database='database/personae.sqlite', **kw):
        self._database = database
        try:
            if 'race' in kw:
                origin = Origins(self._database)
                if origin.is_origin(origin.ORIGIN_TYPE_RACE, kw['race']):
                    self._race = kw['race']
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            self._race = 'Human'
        try:
            if 'class_' in kw:
                origin = Origins(self._database)
                if origin.is_origin(origin.ORIGIN_TYPE_CLASS, kw['class_']):
                    self._class = kw['class_']
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            self._class = 'Fighter'
        if 'level' in kw:
            if 1 <= int(kw['level']) <= 20:
                self._level = int(kw['level'])
            else:
                self._level = 1
        if 'strength' in kw:
            self._strength = kw['strength']
        else:
            self._strength = 15
        if 'dexterity' in kw:
            self._dexterity = kw['dexterity']
        else:
            self._dexterity = 14
        if 'constitution' in kw:
            self._constitution = kw['constitution']
        else:
            self._constitution = 13
        if 'intelligence' in kw:
            self._intelligence = kw['intelligence']
        else:
            self._intelligence = 12
        if 'wisdom' in kw:
            self._wisdom = kw['wisdom']
        else:
            self._wisdom = 10
        if 'charisma' in kw:
            self._charisma = kw['charisma']
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
        connect = DRC(self._database).get_database()
        cursor = connect.cursor()
        sql = 'SELECT Strength,Dexterity,Constitution,' \
              'Intelligence,Wisdom,Charisma FROM races ' \
              'WHERE Race=:race'
        cursor.execute(sql, {'race': self.__get_race()})
        bonuses = cursor.fetchall()
        connect.close()
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

    def __get_class(self):
        """Returns the class value."""
        return self._class

    def __get_level(self):
        """Returns the level value."""
        return self._level

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

    def get_hp(self, use_average=False):
        """Sets hit points for character based on class.

        Args:
            use_average:
                True: Use average hit points/level by class.
                False: Randomly generates hit points/level by class.

        Returns:
            Returns the number of calculated hit points.

        """
        try:
            classes = [
                'Barbarian', 'Bard', 'Cleric', 'Druid',
                'Fighter', 'Monk', 'Paladin', 'Ranger',
                'Rogue', 'Sorcerer', 'Warlock', 'Wizard'
            ]
            if self.__get_class() not in classes:
                raise IndexError
        except IndexError:
            self._class = 'Fighter'
        finally:
            tier_12 = ('Barbarian',)
            tier_10 = ('Fighter', 'Paladin', 'Ranger')
            tier_8 = ('Bard', 'Cleric', 'Druid', 'Monk', 'Rogue', 'Warlock')
            tier_6 = ('Sorcerer', 'Wizard')
            hit_points = 0
            if use_average:
                level = self.__get_level() - 1
            else:
                level = self.__get_level()
            for l in range(0, level):
                die = None
                result = 0
                if not use_average:
                    if self.__get_class() in tier_12:
                        die = Dice(12)
                    if self.__get_class() in tier_10:
                        die = Dice(10)
                    if self.__get_class() in tier_8:
                        die = Dice(8)
                    if self.__get_class() in tier_6:
                        die = Dice(6)
                    result = die.roll()
                    if result < 1:
                        result = 1
                if use_average:
                    if self.__get_class() in tier_12:
                        result = 7
                    if self.__get_class() in tier_10:
                        result = 6
                    if self.__get_class() in tier_8:
                        result = 5
                    if self.__get_class() in tier_6:
                        result = 4
                result += self.get_modifier(self.get_constitution())
                hit_points += result
            # Apply base values if averages used
            if use_average:
                if self.__get_class() in tier_12:
                    hit_points += 12 + self.get_modifier(self.get_constitution())
                if self.__get_class() in tier_10:
                    hit_points += 10 + self.get_modifier(self.get_constitution())
                if self.__get_class() in tier_8:
                    hit_points += 8 + self.get_modifier(self.get_constitution())
                if self.__get_class() in tier_6:
                    hit_points += 6 + self.get_modifier(self.get_constitution())
            return hit_points

    def get_increases(self, class_=False, level=False):
        """Returns the number of ability increases for a character.

        Args:
            class_: The class to check increase for.
        Returns:
            The level of the class to check for.

        """
        increases = 0
        if not class_:
            class_ = self.__get_class()
        if not level:
            level = self.__get_level()
        if level >= 4:
            increases += 1
        if class_ is 'Fighter' and level >= 6:
            increases += 1
        if level >= 8:
            increases += 1
        if class_ is 'Rogue' and level >= 10:
            increases += 1
        if level >= 12:
            increases += 1
        if class_ is 'Fighter' and level >= 14:
            increases += 1
        if level >= 16:
            increases += 1
        if level >= 19:
            increases += 1
        return increases

    def get_intelligence(self):
        """Returns intelligence score value."""
        return self._intelligence

    def get_level(self):
        """Returns level value."""
        return self._level

    @staticmethod
    def get_modifier(value):
        """Returns modifier for specified ability type.

        Args:
            value: The value to retrieve a modifier for.
        Returns:
            The modifier for the requested value.

        """
        return floor((value - 10)/2)

    def get_proficiency(self):
        """Returns proficiency bonus value."""
        proficiency = 2
        if self.__get_level() >= 5:
            proficiency += 1
        if self.__get_level() >= 9:
            proficiency += 1
        if self.__get_level() >= 13:
            proficiency += 1
        if self.__get_level() >= 17:
            proficiency += 1
        if self.__get_level() >= 21:
            proficiency += 1
        if self.__get_level() >= 25:
            proficiency += 1
        if self.__get_level() >= 29:
            proficiency += 1
        return proficiency

    def get_strength(self):
        """Returns strength score value."""
        return self._strength

    def get_wisdom(self):
        """Returns wisdom score value."""
        return self._wisdom


#######################################################################
# Personae Role Playing Game Kit (Dice)
#######################################################################
class Dice:

    # Die types
    DICE_TYPE_D4 = 4
    DICE_TYPE_D6 = 6
    DICE_TYPE_D8 = 8
    DICE_TYPE_D10 = 10
    DICE_TYPE_D12 = 12
    DICE_TYPE_D20 = 20
    DICE_TYPE_D100 = 100

    def __init__(self, die=4):
        if die in (4, 6, 8, 10, 12, 20, 100):
            self._die = die
        else:
            self._die = 4

    @staticmethod
    def __die(die):
        """Generates a roll based on specified die.

        Args:
            die: Specified die type to use.

        Returns:
            Returns the result of the die.

        """
        return randint(1, die)

    def roll(self, modifier=0):
        """Rolls the specified die with specified modifier.

        Args:
            modifier: Modifier to add to the roll.

        Returns:
            Returns the modified result of the die roll.

        """
        return self.__die(self._die) + modifier


#######################################################################
# Personae Role Playing Game Kit (Feats)
#######################################################################
class Feats:

    def __init__(self, database='database/personae.sqlite', **kw):
        self._database = database
        try:
            if 'class_' in kw:
                origin = Origins(self._database)
                if origin.is_origin(origin.ORIGIN_TYPE_CLASS, kw['class_']):
                    self._class = kw['class_']
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            self._class = 'Fighter'
        if 'level' in kw:
            if 1 <= int(kw['level']) <= 20:
                self._level = int(kw['level'])
            else:
                self._level = 1
        if 'charisma' in kw:
            self._charisma = int(kw['charisma'])
        else:
            self._charisma = 8
        if 'constitution' in kw:
            self._constitution = int(kw['constitution'])
        else:
            self._constitution = 13
        if 'dexterity' in kw:
            self._dexterity = int(kw['dexterity'])
        else:
            self._dexterity = 14
        if 'intelligence' in kw:
            self._intelligence = int(kw['intelligence'])
        else:
            self._intelligence = 12
        if 'strength' in kw:
            self._strength = int(kw['strength'])
        else:
            self._strength = 15
        if 'wisdom' in kw:
            self._wisdom = int(kw['wisdom'])
        else:
            self._wisdom = 10

    def __get_proficiencies(self):
        """Returns a list of required proficiencies for a feat.

        Returns:
            Returns a list of required armor/weapon proficiencies.
        """
        connect = DRC(self._database).get_database()
        cursor = connect.cursor()
        sql = "SELECT Armors,Weapons FROM classes WHERE Class=:class"
        cursor.execute(sql, {'class': self.__get_class()})
        proficiency_list = cursor.fetchone()
        proficiency_list = (proficiency_list[0][:], proficiency_list[1][:])
        proficiency_list = '|'.join(proficiency_list)
        connect.close()
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

    def __get_requirements(self, feat_name):
        """Get requirements for the requested feat.

        Args:
            feat_name: The feat to retrieve requirements for.
        Returns:
            Returns dictionary of requested requirements for feat.

        """
        connect = DRC(self._database).get_database()
        cursor = connect.cursor()
        sql = "SELECT Proficiency,Strength,Dexterity," \
            "Constitution,Intelligence,Wisdom,Charisma " \
            "FROM feats WHERE Feat=:feat"
        cursor.execute(sql, {'feat': feat_name})
        _requirements = cursor.fetchall()
        _requirements = _requirements[0][:]
        connect.close()
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

    def get_feats(self):
        """Generates a dictionary of acceptable selections.

        Returns:
            Returns a dictionary of acceptable feats.

        """
        connect = DRC(self._database).get_database()
        cursor = connect.cursor()
        feats_list = []
        cursor.execute("SELECT Feat FROM feats")
        feats = cursor.fetchall()
        connect.close()
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
        """Checks if requirements are met for the specified feat.

        Args:
            feat_name: The feat to retrieve requirements for.
        Returns:
            Returns True if requirements met, False if not.

        """
        # Magic Initiative
        if feat_name is 'Magic Initiative':
            classes = ('Bard', 'Cleric', 'Druid', 'Sorcerer', 'Warlock', 'Wizard')
            if self.__get_class() not in classes:
                return False
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


#######################################################################
# Personae Role Playing Game Kit (Information)
#######################################################################
class Information:

    # Data probe types
    PROBE_TYPE_ALIGNMENT = 100
    PROBE_TYPE_CLASS = 201

    def __init__(self, database='database/personae.sqlite'):
        self._database = database

    def __probe(self, probe_type, query):
        """Returns query based upon probe.

        Args:
            probe_type: Type of data probe type to use for query.
            query: Information to query against data probe.
        Returns:
            Returns result if data found, None if not.

        """
        connect = DRC(self._database).get_database()
        cursor = connect.cursor()
        sql = None
        if probe_type is self.PROBE_TYPE_ALIGNMENT:
            sql = 'SELECT Description FROM alignments WHERE Alignment=:query'
        if probe_type is self.PROBE_TYPE_CLASS:
            sql = 'SELECT Description FROM classes WHERE Class=:query'
        cursor.execute(sql, {'query': query})
        description = cursor.fetchone()
        try:
            return description[0][:]
        except TypeError:
            return None

    def get_alignment(self, alignment_name):
        """Retrieves description for alignment.

        Args:
            alignment_name: Alignment name to retrieve info for.
        Returns:
            Returns description if found, None if none found.

        """
        return self.__probe(self.PROBE_TYPE_ALIGNMENT, {'alignment': alignment_name})

    def get_class(self, class_name):
        """Retrieves description for class.

        Args:
            class_name: Class name to retrieve info for.
        Returns:
            Returns description if found, None if none found.

        """
        return self.__probe(self.PROBE_TYPE_CLASS, {'class': class_name})


#######################################################################
# Personae Role Playing Game Kit (Origins)
#######################################################################
class Origins:

    # Origin types
    ORIGIN_TYPE_ALIGNMENT = 'alignments'
    ORIGIN_TYPE_CLASS = 'classes'
    ORIGIN_TYPE_RACE = 'races'

    def __init__(self, database='database/personae.sqlite'):
        self._database = database

    def get_origins(self, origin_type):
        """Returns a list of origins based on category type.

        Args:
            origin_type: Origin type to retrieve origins for.
        Returns:
            Returns a list of origins by origin type.

        """
        connect = DRC(self._database).get_database()
        cursor = connect.cursor()
        cursor.execute('SELECT name FROM %s' % origin_type)
        origins = cursor.fetchall()
        connect.close()
        origin_options = []
        for origin in origins:
            origin_options.append(origin[0][:])
        return origin_options

    def is_origin(self, origin_type, origin_check):
        """Checks if an origin check is within the origin list.

        Args:
            origin_type: Origin type to check origin check against.
            origin_check: Value to check against origin type.
        Returns:
            Returns True if origin_check found, False if not

        """
        origin_list = self.get_origins(origin_type)
        if origin_check in origin_list:
            return True
        return False


#######################################################################
# Personae Role Playing Game Kit (DRC: Data Resource Controller)
#######################################################################
class DRC:

    def __init__(self, database='database/personae.sqlite'):
        try:
            if os.path.exists(database):
                self._database = database
            else:
                raise ImportError
        except (AttributeError, ImportError):
            exit("Cannot find the required database: '%s'!" % database)
        except NameError:
            sys.exit("Cannot find the required database: '%s'!" % database)

    def get_database(self):
        """Returns a database connection."""
        return sqlite3.connect(self._database)


#######################################################################
# Personae Role Playing Game Kit (Skills)
#######################################################################
class Skills:

    def __init__(self, database='database/personae.sqlite', **kw):
        self._database = database
        try:
            if 'race' in kw:
                origin = Origins(self._database)
                if origin.is_origin(origin.ORIGIN_TYPE_RACE, kw['race']):
                    self._race = kw['race']
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            self._race = 'Human'
        try:
            if 'class_' in kw:
                origin = Origins(self._database)
                if origin.is_origin(origin.ORIGIN_TYPE_CLASS, kw['class_']):
                    self._class = kw['class_']
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            self._class = 'Fighter'
        if 'charisma' in kw:
            self._charisma = int(kw['charisma'])
        else:
            self._charisma = 10
        if 'constitution' in kw:
            self._constitution = int(kw['constitution'])
        else:
            self._constitution = 10
        if 'dexterity' in kw:
            self._dexterity = int(kw['dexterity'])
        else:
            self._dexterity = 10
        if 'intelligence' in kw:
            self._intelligence = int(kw['intelligence'])
        else:
            self._intelligence = 10
        if 'strength' in kw:
            self._strength = int(kw['strength'])
        else:
            self._strength = 10
        if 'wisdom' in kw:
            self._wisdom = int(kw['wisdom'])
        else:
            self._wisdom = 10

    def __get_class(self):
        """Returns class value."""
        return self._class

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
        try:
            if self.__get_class() not in tier2 or tier3 or tier4:
                num_of_skills = 2
            else:
                raise IndexError
        except IndexError:
            if self.__get_class() in tier4:
                num_of_skills = 4
            if self.__get_class() in tier3:
                num_of_skills = 3
            if self.__get_class() in tier2:
                num_of_skills = 2
        return num_of_skills

    def get_modifier(self, skill_name):
        """Returns skill modifier value based on skill.

        Args:
            skill_name: Skill to return a modifier for.
        Returns:
            Returns modifier for the specified skill.

        """
        connect = DRC(self._database).get_database()
        cursor = connect.cursor()
        sql = 'SELECT Ability FROM skills WHERE Skill=:skill'
        cursor.execute(sql, {'skill': skill_name})
        abilities = cursor.fetchall()
        connect.close()
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

    def get_skills(self):
        """Returns a list of skills for specified class.

        Returns:
            Returns a dictionary of allowable skills by class.

        """
        connect = DRC(self._database).get_database()
        cursor = connect.cursor()
        sql = "SELECT Skill FROM skills WHERE %s='Y'" % self.__get_class()
        try:
            cursor.execute(sql)
            skills = cursor.fetchall()
            connect.close()
            skill_list = {}
            index = 1
            for skill_name in skills:
                skill_list[index] = skill_name[0][:]
                index += 1
            return skill_list
        except sqlite3.OperationalError:
            return None

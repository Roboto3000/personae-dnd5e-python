# Seikou Role Playing Game Kit (Information)
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


class Information:

    # Data probe types
    PROBE_TYPE_ALIGNMENT = 100
    PROBE_TYPE_CLASS = 201
    PROBE_TYPE_RACE = 302

    def __init__(self):
        pass

    def __probe(self, probe_type, query):
        """Returns query based upon probe.

        Args:
            probe_type: Type of data probe type to use for query.
            query: Information to query against data probe.
        Returns:
            Returns result if data found, None if not.

        """
        conn = sqlite3.connect(SCG_CONFIG_DATABASE)
        cursor = conn.cursor()
        sql = None
        if probe_type is self.PROBE_TYPE_ALIGNMENT:
            sql = 'SELECT description FROM alignments WHERE name=:alignment'
        if probe_type is self.PROBE_TYPE_CLASS:
            sql = 'SELECT description FROM classes WHERE name=:class'
        if probe_type is self.PROBE_TYPE_RACE:
            sql = 'SELECT description FROM races WHERE name=:race'
        cursor.execute(sql, query)
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

    def get_race(self, race_name):
        """Retrieves description for race.

        Args:
            race_name: Race name to retrieve info for.
        Returns:
            Returns description if found, None if none found.

        """
        return self.__probe(self.PROBE_TYPE_RACE, {'race': race_name})

# Seikou Role Playing Game Kit (Origins)
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


class Origins:

    # Origin types
    ORIGIN_TYPE_ALIGNMENT = 'alignments'
    ORIGIN_TYPE_CLASS = 'classes'
    ORIGIN_TYPE_RACE = 'races'
    ORIGIN_TYPE_SEX = 'sexes'

    @staticmethod
    def get_origins(origin_type):
        """Returns a list of origins based on category type.

        Args:
            origin_type: Origin type to retrieve origins for.
        Returns:
            Returns a list of origins by origin type.

        """
        conn = sqlite3.connect(SCG_CONFIG_DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT name FROM %s' % origin_type)
        origins = cursor.fetchall()
        conn.close()
        origin_options = []
        for origin in origins:
            origin_options.append(origin[0][:])
        return origin_options

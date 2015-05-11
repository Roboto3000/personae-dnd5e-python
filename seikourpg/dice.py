# Seikou Role Playing Game Kit (Dice)
#
# Author: Marcus T. Taylor <mtaylor3121@gmail.com>
# Website: https://github.com/mtaylor33/seikourpg
# Copyright: 2012, 2015
#

from random import randint


class Dice:

    def __init__(self, die):
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
        """Rolls the specified die width specified modifier.

        Args:
            modifier: Modifier to add to the specified roll.

        Returns:
            Returns the modified result of the die roll.

        """
        return self.__die(self._die) + modifier

#Personae RPG Library

**Author:** Marcus T. Taylor <mtaylor3121@gmail.com>


##INDEX

1. INTRODUCTION
2. CHANGELOG


###1. Introduction

**Personae RPG Library** is a python library used in the creation of RPG tools utilizing the Dungeon's & Dragons 5th edition rule set. Primarily, I've been using the module to develop a GUI application for generating NPCs for my DnD games, which you can find this project [here](https://github.com/mtaylor33/Personae). It should be noted that this software is not officially developed or endorsed by Wizard of the Coast LLC.


###2. Changelog

- Version *20180203*

    - Merged 'get_armor_proficiency' and 'get_weapon_proficiency' functions into 'get_class_proficiency' function.
    - SQLite database removed from project. Data now stored in personae_config.py.
    - Personae library rewrote completely from scratch.

- Version *20150728*

    - Added get_increases method to Abilities class.
    - Implemented requirements check for Magic Initiative feat.
    - Cleaned up documentation for PHP library.

- Version *20150626*

    - Added get_level method to Abilities class.
    - Added is_origin method to Origins class.
    - Applied average values in addition to random values (hit points/level).
    - Added get_version method to Settings class.
    - Combined classes into one package file.
    
- Version *20150428*

    - Initial release.

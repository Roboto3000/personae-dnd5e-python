# Personae RPG Library
#
# Author: Marcus T. Taylor <mtaylor3121@gmail.com>
# Copyright: 2015, 2018
#
try:
    from personae_config import *
except ImportError:
    exit("Configuration file 'personae_config.py' missing! Halted.")


PERSONAE_VERSION = 20180203


def __myitems__(data):
    try:
        out = []
        for item in data.iteritems():
            out.append(item[0])
        return tuple(out)
    except AttributeError:
        return None

def get_ability(skill):
    """Returns primary ability name for skill.
    
    Args:
        skill (string): Skill to return primary ability for.

    Returns:
        Returns a string name of the primary skill.
    """
    return personae_skill[skill]['Ability']

def get_alignments():
    """Returns list of character classes.
    
    Returns:
        Returns a tuple of class names.
    """
    return __myitems__(personae_alignment)

def get_bonus(race):
    """Returns ability modifiers by race.
    
    Args:
        race (string): Race to retrieve racial bonus(es) for.
        
    Returns:
        Returns racial bonus(es) as dict or None if race not found.
    """
    try:
        _bonus = personae_race[race]
        bonus = {}
        for ability,value in _bonus.iteritems():
            if _bonus[ability] is not 0:
                bonus[ability] = value
        return bonus
    except KeyError:
        return None

def get_classes():
    """Returns list of character classes.
    
    Returns:
        Returns a tuple of class names.
    """
    return __myitems__(personae_class)

def get_feats(omitted=[]):
    """Returns omitted list of character feats.
    
    Args:
        omitted (list): List of feats to exclude.
        
    Returns:
        Returns a list of feats sans any omitted feats.
    """
    feats = list(__myitems__(personae_feat))
    if len(omitted):
        for feat in omitted:
            feats.remove(feat)
    return tuple(feats)

def get_modifier(skill, scores):
    """Returns skill ability modifier value for skill.
    
    Args:
        skill (string): Name of skill to get ability modifier for.
        scores (dict): Score to return a modifier for.
        
    Returns:
        Returns a integer for skill modifier.
    """
    return scores[get_ability(skill)]['Modifier']

def get_proficiency(_class, proficiency_flag='a'):
    """Returns armor/weapon proficiencies by _class.
    
    Args:
        _class (string): Name of class to look for proficiencies.
        proficiency_flag (string): Proficiency type (armor, weapon) to request.
            Flag 'a': Armor Proficiencies
            Flag 'w': Weapon Proficiencies
        
    Returns:
        Returns a list of armor proficiencies or None if not requested.
    """
    try:
        if proficiency_flag is 'a':
            proficiency = personae_class[_class]['Armors'].split(',')
        elif proficiency_flag is 'w':
            proficiency = personae_class[_class]['Weapons'].split(',')
        else:
            raise KeyError
        if '-' not in proficiency:
            return tuple(proficiency)
        else:
            return ()
    except KeyError:
        return None
    
def get_races():
    """Returns list of character races.
    
    Returns:
        Returns a tuple of race names.
    """
    return __myitems__(personae_race)

def get_requirements(feat):
    """Return requirements for feat.
    
    Args:
        feat (string): Feat to find requirements for.
        
    Returns:
        Returns a dictionary of feat requirements.
    """
    return personae_feat[feat]

def get_skills():
    """Returns list of character skills.
    
    Args:
        _class (string): Class to return skills for.
        
    Returns:
        Returns a list of class names by _class.
    """
    return __myitems__(personae_skill)

def get_version():
    """Returns the current version of Persona.
    
    Returns:
        Returns version number as integer.
    """
    return PERSONAE_VERSION


if __name__ == '__main__':
    # PERSONAE DEBUG CODE
    ap = get_proficiency('Cleric', 'a')
    wp = get_proficiency('Fighter', 'w')
    scores = {
        'Strength': {'Modifier': 0, 'Score': 10}, 
        'Dexterity': {'Modifier': -1, 'Score': 8}, 
        'Constitution': {'Modifier': 2, 'Score': 15}, 
        'Intelligence': {'Modifier': 0, 'Score': 11}, 
        'Wisdom': {'Modifier': 1, 'Score': 12}, 
        'Charisma': {'Modifier': 2, 'Score': 15}
    }
    print get_alignments()
    print ap
    print get_classes()
    print get_feats()
    print get_requirements('Actor')
    print get_version()
    print get_bonus('Elf, Drow')
    print get_races()
    print get_ability('Acrobatics')
    print get_skills()
    print wp

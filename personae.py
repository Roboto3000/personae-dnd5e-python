# Personae RPG Library
#
# Author: Marcus T. Taylor <mtaylor3121@gmail.com>
# Website: https://github.com/mtaylor33/Personae
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
    
def get_alignment_list():
    """Returns list of character classes.
    
    Returns:
        Returns a tuple of class names.
    """
    return __myitems__(personae_alignment)

def get_class_list():
    """Returns list of character classes.
    
    Returns:
        Returns a tuple of class names.
    """
    return __myitems__(personae_class)

def get_class_proficiency(_class, proficiency_flag='a'):
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

def get_feat_list(omitted=[]):
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

def get_feat_requirement(feat):
    """Return requirements for feat.
    
    Args:
        feat (string): Feat to find requirements for.
        
    Returns:
        Returns a dictionary of feat requirements.
    """
    return personae_feat[feat]
        
def get_modifier(score):
    """Returns modifier for score.
    
    Returns:
        Returns modifier value (score - 10)/2.
    """
    return (score - 10)/2

def get_personae_version():
    """Returns the current version of Persona.
    
    Returns:
        Returns version number as integer.
    """
    return PERSONAE_VERSION

def get_race_bonus(race):
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
    
def get_race_list():
    """Returns list of character races.
    
    Returns:
        Returns a tuple of race names.
    """
    return __myitems__(personae_race)

def get_skill_ability(skill):
    """Returns primary ability name for skill.
    
    Args:
        skill (string): Skill to return primary ability for.

    Returns:
        Returns a string name of the primary skill.
    """
    return personae_skill[skill]['Ability']

def get_skill_allotment(_class):
    """Returns number of skills by _class.
    
    Args:
        _class (string): Class to return skill allotment for.
    Returns:
        Returns integer of skills by _class.
    """
    num_of_skills = 2
    if _class is 'Rogue':
        num_of_skills = 4
    if _class is 'Bard' or 'Ranger':
        num_of_skills = 3
    return num_of_skills

def get_skill_list():
    """Returns list of character skills.
    
    Args:
        _class (string): Class to return skills for.
        
    Returns:
        Returns a list of class names by _class.
    """
    return __myitems__(personae_skill)

def get_skill_modifier(skill, scores):
    """Returns skill ability modifier value for skill.
    
    Args:
        skill (string): Name of skill to get ability modifier for.
        scores (dict): Score to return a modifier for.
        
    Returns:
        Returns a integer for skill modifier.
    """
    return scores[get_skill_ability(skill)]['Modifier']

def has_feat_requirement(feat, _class, a_prof, w_prof, scores):
    """Checks if scores, a_prof, w_prof has requirements for feat.
    
    Args:
        feat (string): Feat to check requirements for.
        _class (string): Class to check requirements for.
        a_prof (list): List of armor proficiencies.
        w_prof (list): List of weapon proficiencies.
        scores (dict): Dictionary of ability scores.
        
    Returns:
        True if requirements met; False otherwise.
    """
    if feat in ('Elemental Adept', 'Spell Sniper', 'War Caster'):
        if not is_caster(_class):
            return False
    require = get_feat_requirement(feat)
    if require['Class'] is not '-':
        if _class not in require['Class'].split(','):
            return False
    if require['Proficiency'] is not '-':
        if require['Proficiency'] not in a_prof or w_prof:
            return False
    if scores['Strength']['Score'] < require['Strength']:
        return False
    if scores['Dexterity']['Score'] < require['Dexterity']:
        return False
    if scores['Constitution']['Score'] < require['Constitution']:
        return False
    if scores['Intelligence']['Score'] < require['Intelligence']:
        return False
    if scores['Wisdom']['Score'] < require['Wisdom']:
        return False
    if scores['Charisma']['Score'] < require['Charisma']:
        return False
    return True

def is_caster(_class, level=1):
    """Returns True if _class is spellcaster; False if not.
    
    Args:
        _class (string): Class to check if caster.
        
    Returns:
        True if caster; False otherwise.
    """
    casters = ('Bard','Cleric','Druid','Sorcerer','Warlock','Wizard')
    if _class in casters:
        return True
    if _class in ('Fighter', 'Rogue') and level >= 3:
        return True
    if _class in ('Paladin', 'Ranger') and level >= 2:
        return True
    return False


if __name__ == '__main__':
    # PERSONAE DEBUG CODE
    ap = get_class_proficiency('Cleric', 'a')
    wp = get_class_proficiency('Fighter', 'w')
    scores = {
        'Strength': {'Modifier': 0, 'Score': 10}, 
        'Dexterity': {'Modifier': -1, 'Score': 8}, 
        'Constitution': {'Modifier': 2, 'Score': 15}, 
        'Intelligence': {'Modifier': 0, 'Score': 11}, 
        'Wisdom': {'Modifier': 1, 'Score': 12}, 
        'Charisma': {'Modifier': 2, 'Score': 15}
    }
    print get_alignment_list()
    print ap
    print get_class_list()
    print get_feat_list()
    print get_feat_requirement('Actor')
    print get_modifier(20)
    print get_personae_version()
    print get_race_bonus('Elf, Drow')
    print get_race_list()
    print get_skill_ability('Acrobatics')
    print get_skill_allotment('Fighter')
    print get_skill_list()
    print get_skill_modifier('Acrobatics', scores)
    print wp
    print has_feat_requirement('Spell Sniper', 'Fighter', ap, wp, scores)
    #print is_caster('Fighter', 3)
    print is_caster('Wizard')

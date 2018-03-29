def get_allotment(_class):
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

def get_skill_modifier(skill, scores):
    """Returns skill ability modifier value for skill.
    
    Args:
        skill (string): Name of skill to get ability modifier for.
        scores (dict): Score to return a modifier for.
        
    Returns:
        Returns a integer for skill modifier.
    """
    return scores[get_skill_ability(skill)]['Modifier']

def has_requirements(feat, _class, a_prof, w_prof, scores):
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
    require = get_requirements(feat)
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

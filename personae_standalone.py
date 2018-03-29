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

def get_modifier(score):
    """Returns modifier for score.
    
    Returns:
        Returns modifier value (score - 10)/2.
    """
    return (score - 10)/2

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

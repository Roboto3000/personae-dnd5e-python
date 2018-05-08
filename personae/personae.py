try:
	from personae_config import *
except ImportError:
	exit('Failed to import required library! Halted.')


def __myitems__(data):
	"""
	Returns tuple of data from data source.
	
	Parameters
	----------
	
		data : dict
			Dictionary of DnD data.
	
	Returns
	-------
	
		tuple
			Tuple of DnD game material.
	"""
	try:
		out = []
		for item in data.iteritems():
			out.append(item[0])
		return tuple(out)
	except AttributeError:
		return None

def get_allotment(_class):
	"""
	Returns number of skills by _class.
	
	Parameters
	----------
		_class : string
			Class to return skill allotment for.
		
	Returns
	-------
		int
			Returns integer of skills by _class.
	"""
	num_of_skills = 2
	if _class is 'Rogue':
		num_of_skills = 4
	if _class is 'Bard' or 'Ranger':
		num_of_skills = 3
	return num_of_skills

def get_modifier(score):
	"""
	Generates ability modifier by score.
	
	Parameters
	----------
		score : int
			Score to generate modifier for.
			
	Returns
	-------
		int
			Returns modifier value (score - 10)/2.
	"""
	return (score - 10)/2

def is_caster(_class, level=1):
	"""
	Returns whether _class is a spellcaster.
	
	Parameters
	----------
		_class : string
			Class to check if caster.
		level : int
			Level of _class; defaults to 1.
		
	Returns
	-------
		bool
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

    
class Personae:
	def __init__(cls, **kwargs):
		cls.ability_scores = 'ability' in kwargs and kwargs['ability'] or None
		cls.armor_proficiency = 'armor' in kwargs and kwargs['armor'] or None
		cls.weapon_proficiency = 'weapon' in kwargs and kwargs['weapon'] or None
	
	def get_ability(cls, skill):
		"""
		Returns primary ability name for skill.
		
		Parameters
		----------
			skill : string
				Skill to return primary ability for.
		
		Returns
		-------
			string
				Returns a string name of the primary skill.
		"""
		return personae_skill[skill]['Ability']
	
	def get_alignments(cls):
		"""
		Returns list of character classes.
		
		Returns
		-------
			tuple
				Returns a tuple of class names.
		"""
		return __myitems__(personae_alignment)

	def get_bonus(cls, race):
		"""
		Returns ability modifiers by race.

		Parameters
		----------
			race : string
				Race to retrieve racial bonus(es) for.
			
		Returns
		-------
			dict|None
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
				
	def get_classes(cls):
		"""
		Returns list of character classes.
		
		Returns
		-------
			tuple
				Returns a collection of class names.
		"""
		return __myitems__(personae_class)
	
	def get_feats(cls, omitted=[]):
		"""
		Returns omitted list of character feats.

		Parameters
		----------
			omitted : list
				List value of feats to exclude.

		Returns
		-------
			list
				Returns a list of feats sans any omitted feats.
		"""
		feats = list(__myitems__(personae_feat))
		if len(omitted):
			for feat in omitted:
				feats.remove(feat)
		return tuple(feats)
	
	def get_modifier(cls, skill, scores):
		"""
		Returns skill ability modifier value for skill.
		
		Parameters
		----------
			skill : string
				Name of skill to get ability modifier for.
			scores : dict
				Score to return a modifier for.
			
		Returns
		-------
			int
				Returns a modifier for the skill.
		"""
		return scores[get_ability(skill)]['Modifier']
	
	def get_proficiency(cls, _class, proficiency_flag='a'):
		"""
		Returns armor/weapon proficiencies by _class.

		Parameters
		----------
			_class : string
				Name of class to look for proficiencies.
			proficiency_flag : string
				Proficiency type (armor, weapon) to request.
					Flag 'a': Armor Proficiencies
					Flag 'w': Weapon Proficiencies

		Returns
		-------
			tuple|None
				Returns proficiencies, if found; None otherwise.
		"""
		if proficiency_flag is 'a':
			proficiency = personae_class[_class]['Armors'].split(',')
		elif proficiency_flag is 'w':
			proficiency = personae_class[_class]['Weapons'].split(',')
		else:
			return None
		if '-' not in proficiency:
			return tuple(proficiency)
		else:
			return ()

	def get_races(cls):
		"""
		Returns list of character races.

		Returns
		-------
			tuple
				Returns a tuple of race names.
		"""
		return __myitems__(personae_race)

	def get_requirements(cls, feat):
		"""Return requirements for feat.

		Parameters
		----------
			feat : string
				Feat to find requirements for.

		Returns
		-------
			dict
				Returns a dictionary of feat requirements.
		"""
		return personae_feat[feat]
	
	def get_skills(cls):
		"""
		Returns list of character skills.

		Parameters
		----------
			_class : string
				Class to return skills for.

		Returns
		-------
			list
				Returns a list of class names by _class.
		"""
		return __myitems__(personae_skill)

	def has_requirements(cls, feat, _class):
		"""
		Checks if scores, armor, weapon meet feat requirements.

		Parameters
		----------
			feat : string
				Feat to check requirements for.
			_class : string
				Class to check requirements for.

		Returns
		-------
			bool
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
			if require['Proficiency'] not in cls.armor_proficiency or cls.weapon.proficiency:
				return False
		if cls.ability_scores['Strength']['Score'] < require['Strength']:
			return False
		if cls.ability_scores['Dexterity']['Score'] < require['Dexterity']:
			return False
		if cls.ability_scores['Constitution']['Score'] < require['Constitution']:
			return False
		if cls.ability_scores['Intelligence']['Score'] < require['Intelligence']:
			return False
		if cls.ability_scores['Wisdom']['Score'] < require['Wisdom']:
			return False
		if cls.ability_scores['Charisma']['Score'] < require['Charisma']:
			return False
		return True


if __name__ == '__main__':
	pass

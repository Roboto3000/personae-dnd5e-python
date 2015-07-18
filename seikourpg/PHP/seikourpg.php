<?php
namespace SeikouRPG;
/**
 *
 * Seikou Role Playing Game Kit
 * Author: Marcus T. Taylor <mtaylor3121@gmail.com>
 * Website: GitHub <https://github.com/mtaylor33/seikous-rpg-kit>
 * Copyright: 2012, 2015
 *
 */

define('VERSION', '20150728');


/**
 * Seikou Role Playing Game Kit (Abilities)
 */
class Abilities
{
    protected $_race;
    protected $_class;
    protected $_strength;
    protected $_dexterity;
    protected $_constitution;
    protected $_intelligence;
    protected $_wisdom;
    protected $_charisma;

    public function __construct(array $kw=array())
    {
        try {
            if (array_key_exists('race', $kw)) {
                $origins = new Origins();
                if ($origins->is_origin($origins::ORIGIN_TYPE_RACE, $kw['race'])) {
                    $this->_race = $kw['race'];
                } else
                    throw new \Exception();
            } else
                throw new \Exception();
        } catch (\Exception $e) {
            $this->_race = 'Human';
        }
        try {
            if (array_key_exists('class_', $kw)) {
                $origins = new Origins();
                if ($origins->is_origin($origins::ORIGIN_TYPE_CLASS, $kw['class_'])) {
                    $this->_class = $kw['class_'];
                } else
                    throw new \Exception();
            } else
                throw new \Exception();
        } catch (\Exception $e) {
            $this->_class = 'Fighter';
        }
        if (array_key_exists('level', $kw)) {
            if ($kw['level'] >= 1 and $kw['level'] <= 20) {
                $this->_level = intval($kw['level']);
            } else
                $this->_level = 1;
        }
        if (array_key_exists('strength', $kw))
            $this->_strength = $kw['strength'];
        else
            $this->_strength = 15;
        if (array_key_exists('dexterity', $kw))
            $this->_dexterity = $kw['dexterity'];
        else
            $this->_dexterity = 14;
        if (array_key_exists('constitution', $kw))
            $this->_constitution = $kw['constitution'];
        else
            $this->_constitution = 13;
        if (array_key_exists('intelligence', $kw))
            $this->_intelligence = $kw['intelligence'];
        else
            $this->_intelligence = 12;
        if (array_key_exists('wisdom', $kw))
            $this->_wisdom = $kw['wisdom'];
        else
            $this->_wisdom = 10;
        if (array_key_exists('charisma', $kw))
            $this->_charisma = $kw['charisma'];
        else
            $this->_charisma = 8;
        # Apply racial bonuses, if applicable
        $bonus = $this->__get_bonus();
        if (array_key_exists('strength', $bonus))
            $this->__set_strength($bonus['strength']);
        if (array_key_exists('dexterity', $bonus))
            $this->__set_dexterity($bonus['dexterity']);
        if (array_key_exists('constitution', $bonus))
            $this->__set_constitution($bonus['constitution']);
        if (array_key_exists('intelligence', $bonus))
            $this->__set_intelligence($bonus['intelligence']);
        if (array_key_exists('wisdom', $bonus))
            $this->__set_wisdom($bonus['wisdom']);
        if (array_key_exists('charisma', $bonus))
            $this->__set_charisma($bonus['charisma']);
    }

    /**
     * __get_bonus
     *
     * Retrieves racial ability score bonuses.
     *
     * @return array
     *
     */
    private function __get_bonus()
    {
        $settings = new Settings();
        $connect = $settings->get_database();
        $sql = 'SELECT strength,dexterity,constitution,' .
            'intelligence,wisdom,charisma FROM races ' .
            'WHERE name=:race';
        $stm = $connect->prepare($sql);
        $stm->bindValue(':race', $this->__get_race(), \PDO::PARAM_STR);
        $stm->execute();
        $bonus_result = $stm->fetchAll();
        $bonus_list = array();
        foreach ($bonus_result as $bonus) {
            $strength = $bonus[0];
            if ($strength != 0)
                $bonus_list['strength'] = $strength;
            $dexterity = $bonus[1];
            if ($dexterity != 0)
                $bonus_list['dexterity'] = $dexterity;
            $constitution = $bonus[2];
            if ($constitution != 0)
                $bonus_list['constitution'] = $constitution;
            $intelligence = $bonus[3];
            if ($intelligence != 0)
                $bonus_list['intelligence'] = $intelligence;
            $wisdom = $bonus[4];
            if ($wisdom != 0)
                $bonus_list['wisdom'] = $wisdom;
            $charisma = $bonus[5];
            if ($charisma != 0)
                $bonus_list['charisma'] = $charisma;
        }
        return $bonus_list;
    }

    /**
     * __get_class
     *
     * Returns the class value.
     *
     * @return string
     *
     */
    private function __get_class()
    {
        return $this->_class;
    }

    /**
     * __get_level
     *
     * Returns the level value.
     *
     * @return integer
     *
     */
    private function __get_level()
    {
        return $this->_level;
    }

    /**
     * __get_race
     *
     * Returns the racial value.
     *
     * @return string
     *
     */
    private function __get_race()
    {
        return $this->_race;
    }

    /**
     * __set_charisma
     *
     * Sets charisma score value.
     *
     * @param integer $value Bonus value to add to new charisma value.
     *
     */
    private function __set_charisma($value)
    {
        $this->_charisma += intval($value);
    }

    /**
     * __set_constitution
     *
     * Sets constitution score value.
     *
     * @param integer $value Bonus value to add to new constitution value.
     *
     */
    private function __set_constitution($value)
    {
        $this->_constitution += intval($value);
    }

    /**
     * __set_dexterity
     *
     * Sets dexterity score value.
     *
     * @param integer $value Bonus value to add to new charisma value.
     *
     */
    private function __set_dexterity($value)
    {
        $this->_dexterity += intval($value);
    }

    /**
     * __set_intelligence
     *
     * Sets intelligence score value.
     *
     * @param integer $value Bonus value to add to new intelligence value.
     *
     */
    private function __set_intelligence($value)
    {
        $this->_intelligence += intval($value);
    }

    /**
     * __set_strength
     *
     * Sets strength score value.
     *
     * @param integer $value Bonus value to add to new strength value.
     *
     */
    private function __set_strength($value)
    {
        $this->_strength += intval($value);
    }

    /**
     * __set_wisdom
     *
     * Sets wisdom score value.
     *
     * @param integer $value Bonus value to add to new wisdom value.
     *
     */
    private function __set_wisdom($value)
    {
        $this->_wisdom += intval($value);
    }

    /**
     * get_charisma
     *
     * Returns charisma score value.
     *
     * @return integer
     *
     */
    public function get_charisma()
    {
        return $this->_charisma;
    }

    /**
     * get_constitution
     *
     * Returns constitution score value.
     *
     * @return integer
     *
     */
    public function get_constitution()
    {
        return $this->_constitution;
    }

    /**
     * get_dexterity
     *
     * Returns dexterity score value.
     *
     * @return integer
     *
     */
    public function get_dexterity()
    {
        return $this->_dexterity;
    }

    /**
     * __get_hp
     *
     * Sets hit points for character based on class.
     *
     * @param bool $use_average
     *  True: Use average hit points/level by class.
     *  False: Randomly generates hit points/level by class.
     * @return integer Returns the number of calculated hit points.
     *
     */
    public function get_hp($use_average = false)
    {
        try {
            $origins = new Origins();
            if (!$origins->is_origin($origins::ORIGIN_TYPE_CLASS, $this->__get_class()))
                throw new \Exception();
        } catch (\Exception $e) {
            $this->_class = 'Fighter';
        } finally {
            $tier_12 = array('Barbarian');
            $tier_10 = array('Fighter', 'Paladin', 'Ranger');
            $tier_8 = array('Bard', 'Cleric', 'Druid', 'Monk', 'Rogue', 'Warlock');
            $tier_6 = array('Sorcerer', 'Wizard');
            $hit_points = 0;
            if ($use_average)
                $level = $this->__get_level() - 1;
            else
                $level = $this->__get_level();
            for ($l = 0; $l < $level; $l++) {
                $die = false;
                $result = 0;
                if (!$use_average) {
                    if (in_array($this->__get_class(), $tier_12))
                        $die = new Dice(12);
                    if (in_array($this->__get_class(), $tier_10))
                        $die = new Dice(10);
                    if (in_array($this->__get_class(), $tier_8))
                        $die = new Dice(8);
                    if (in_array($this->__get_class(), $tier_6))
                        $die = new Dice(6);
                    $result = $die->roll();
                    if ($result < 1)
                        $result = 1;
                }
                if ($use_average) {
                    if (in_array($this->__get_class(), $tier_12))
                        $result = 7;
                    if (in_array($this->__get_class(), $tier_10))
                        $result = 6;
                    if (in_array($this->__get_class(), $tier_8))
                        $result = 5;
                    if (in_array($this->__get_class(), $tier_6))
                        $result = 4;
                }
                $result += $this->get_modifier($this->get_constitution());
                $hit_points += $result;
                # Apply base values if averages used
                if ($use_average) {
                    if (in_array($this->__get_class(), $tier_12))
                        $hit_points += 12 + $this->get_modifier($this->get_constitution());
                    if (in_array($this->__get_class(), $tier_10))
                        $hit_points += 10 + $this->get_modifier($this->get_constitution());
                    if (in_array($this->__get_class(), $tier_8))
                        $hit_points += 8 + $this->get_modifier($this->get_constitution());
                    if (in_array($this->__get_class(), $tier_6))
                        $hit_points += 6 + $this->get_modifier($this->get_constitution());
                }
            }
        }
        return $hit_points;
    }

    /**
     * get_increases
     *
     * Returns the number of ability increases for a character.
     *
     * @param bool|string $class_ The class to check increase for.
     * @param bool|int $level The level of the class to check for.
     * @return int
     *
     */
    public function get_increases($class_=false, $level=false)
    {
        $increases = 0;
        if ( !$class_ )
            $class_ = $this->__get_class();
        if ( !$level )
            $level = $this->__get_level();
        if ( $level >= 4 )
            $increases += 1;
        if ( $class_ == 'Fighter' and $level >= 6 )
            $increases += 1;
        if ( $level >= 8 )
            $increases += 1;
        if ( $class_ == 'Rogue' and $level >= 10 )
            $increases += 1;
        if ( $level >= 12 )
            $increases += 1;
        if ( $class_ == 'Fighter' and $level >= 14 )
            $increases += 1;
        if ( $level >= 16 )
            $increases += 1;
        if ( $level >= 19 )
            $increases += 1;
        return $increases;
    }

    /**
     * get_intelligence
     *
     * Returns intelligence score value.
     *
     * @return integer
     *
     */
    public function get_intelligence()
    {
        return $this->_intelligence;
    }

    /**
     * get_level
     *
     * Returns level value.
     *
     * @return integer
     *
     */
    public function get_level()
    {
        return $this->_level;
    }

    /**
     * get_modifier
     *
     * Returns modifier value for specified value.
     *
     * @param integer $value The value to retrieve a modifier for.
     * @return integer The modifier for the requested value.
     *
     */
    public function get_modifier($value)
    {
        return intval(floor(($value - 10) / 2));
    }

    /**
     * get_proficiency
     *
     * Returns proficiency bonus value.
     *
     * @return integer
     *
     */
    public function get_proficiency()
    {
        $proficiency = 2;
        if ($this->__get_level() >= 5)
            $proficiency += 1;
        if ($this->__get_level() >= 9)
            $proficiency += 1;
        if ($this->__get_level() >= 13)
            $proficiency += 1;
        if ($this->__get_level() >= 17)
            $proficiency += 1;
        if ($this->__get_level() >= 21)
            $proficiency += 1;
        if ($this->__get_level() >= 25)
            $proficiency += 1;
        if ($this->__get_level() >= 29)
            $proficiency += 1;
        return $proficiency;
    }

    /**
     * get_strength
     *
     * Returns strength score value.
     *
     * @return integer
     *
     */
    public function get_strength()
    {
        return $this->_strength;
    }

    /**
     * get_wisdom
     *
     * Returns wisdom score value.
     *
     * @return integer
     *
     */
    public function get_wisdom()
    {
        return $this->_wisdom;
    }
}


/**
 * Seikou Role Playing Game Kit (Dice)
 */
class Dice
{
    const DICE_TYPE_D4 = 4;
    const DICE_TYPE_D6 = 6;
    const DICE_TYPE_D8 = 8;
    const DICE_TYPE_D10 = 10;
    const DICE_TYPE_D12 = 12;
    const DICE_TYPE_D20 = 20;
    const DICE_TYPE_D100 = 100;

    protected $_die;

    public function __construct($die=4)
    {
        if ( in_array($die, array(4, 6, 8, 10, 12, 20, 100)) )
            $this->_die = $die;
        else
            $this->_die = 4;
    }

    /**
     * __die
     *
     * Generates a roll based on specified die.
     *
     * @param integer $die Specified die type to use.
     * @return int Returns the result of the die.
     *
     */
    private function __die($die)
    {
        return rand(1, $die);
    }

    /**
     * roll
     *
     * Rolls the specified die with the specified modifier.
     *
     * @param int $modifier Modifier to add to the specified roll.
     * @return int Returns the modified result of the die roll.
     *
     */
    public function roll($modifier=0)
    {
        return $this->__die($this->_die) + $modifier;
    }
}


/**
 * Seikou Role Playing Game Kit (Feats)
 */
class Feats
{
    protected $_class;
    protected $_level;
    protected $_charisma;
    protected $_constitution;
    protected $_dexterity;
    protected $_intelligence;
    protected $_strength;
    protected $_wisdom;

    public function __construct(array $kw=array())
    {
        try {
            if (array_key_exists('class_', $kw)) {
                $origins = new Origins();
                if ($origins->is_origin($origins::ORIGIN_TYPE_CLASS, $kw['class_']))
                    $this->_class = $kw['class_'];
                else
                    throw new \Exception();
            } else
                throw new \Exception();
        } catch ( \Exception $e) {
            $this->_class = 'Fighter';
        }
        if (array_key_exists('level', $kw) ) {
            if (intval($kw['level']) >= 1 and intval($kw['level'] <= 20))
                $this->_level = intval($kw['level']);
            else
                $this->_level = 1;
        }
        if (array_key_exists('charisma', $kw))
            $this->_charisma = intval($kw['charisma']);
        else
            $this->_charisma = 8;
        if (array_key_exists('constitution', $kw))
            $this->_constitution = intval($kw['constitution']);
        else
            $this->_constitution = 13;
        if (array_key_exists('dexterity', $kw))
            $this->_dexterity = intval($kw['dexterity']);
        else
            $this->_dexterity = 14;
        if (array_key_exists('intelligence', $kw))
            $this->_intelligence = intval($kw['intelligence']);
        else
            $this->_intelligence = 12;
        if (array_key_exists('strength', $kw))
            $this->_strength = intval($kw['strength']);
        else
            $this->_strength = 15;
        if (array_key_exists('wisdom', $kw))
            $this->_wisdom = intval($kw['wisdom']);
        else
            $this->_wisdom = 10;
    }

    /**
     * __get_proficiencies
     *
     * Returns an array of proficiencies by class.
     *
     * @return array
     *
     */
    private function __get_proficiencies()
    {
        $settings = new Settings();
        $connect = $settings->get_database();
        $sql = 'SELECT armors,weapons FROM classes WHERE name=:class';
        $stm = $connect->prepare($sql);
        $stm->bindValue(':class', $this->__get_class(), \PDO::PARAM_STR);
        $stm->execute();
        $proficiency_temp = $stm->fetchColumn() . '|' . $stm->fetchColumn(1);
        $connect = null;
        $proficiency_temp = explode('|', $proficiency_temp);
        foreach ( $proficiency_temp as $proficiency ) {
            if ( $proficiency == '-' ) {
                $indice = array_search($proficiency, $proficiency_temp);
                unset($proficiency_temp[$indice]);
            }
        }
        return $proficiency_temp;
    }

    /**
     * __get_charisma
     *
     * Returns charisma value.
     *
     * @return int
     *
     */
    private function __get_charisma()
    {
        return $this->_charisma;
    }

    /**
     * __get_class
     *
     * Returns class value.
     *
     * @return string
     *
     */
    private function __get_class()
    {
        return $this->_class;
    }

    /**
     * __get_constitution
     *
     * Returns constitution value.
     *
     * @return int
     *
     */
    private function __get_constitution()
    {
        return $this->_constitution;
    }

    /**
     * __get_dexterity
     *
     * Returns dexterity value.
     *
     * @return int
     *
     */
    private function __get_dexterity()
    {
        return $this->_dexterity;
    }

    /**
     * __get_intelligence
     *
     * Returns intelligence value.
     *
     * @return int
     *
     */
    private function __get_intelligence()
    {
        return $this->_intelligence;
    }

    /**
     * __get_level
     *
     * Returns level value.
     *
     * @return int
     *
     */
    private function __get_level()
    {
        return $this->_level;
    }

    /**
     * __get_requirements
     *
     * Get requirements for the requested feat.
     *
     * @param string $feat_name The feat to retrieve requirements for.
     * @return array Returns dictionary of requested requirements for feat.
     *
     */
    private function __get_requirements($feat_name)
    {
        $settings = new Settings();
        $connect = $settings->get_database();
        $sql = "SELECT proficiency,strength,dexterity," .
            "constitution,intelligence,wisdom,charisma " .
            "FROM feats WHERE name=:feat_name";
        $stm = $connect->prepare($sql);
        $stm->bindValue(':feat_name', $feat_name, \PDO::PARAM_STR);
        $stm->execute();
        $requirements = array(
            'proficiency' => $stm->fetchColumn(),
            'strength' => $stm->fetchColumn(1),
            'dexterity' => $stm->fetchColumn(2),
            'constitution' => $stm->fetchColumn(3),
            'intelligence' => $stm->fetchColumn(4),
            'wisdom' => $stm->fetchColumn(5),
            'charisma' => $stm->fetchColumn(6)
        );
        $connect = null;
        return $requirements;
    }

    /**
     * __get_strength
     *
     * Returns strength value.
     *
     * @return int
     *
     */
    private function __get_strength()
    {
        return $this->_strength;
    }

    /**
     * __get_wisdom
     *
     * Returns wisdom value.
     *
     * @return int
     *
     */
    private function __get_wisdom()
    {
        return $this->_wisdom;
    }

    /**
     * get_feats
     *
     * Generates an array of acceptable selections.
     *
     * @return array Returns an array of acceptable feats.
     *
     */
    public function get_feats()
    {
        $settings = new Settings();
        $connect = $settings->get_database();
        $feats = $connect->query('SELECT name FROM feats');
        $connect = null;
        $feats_temp = array();
        foreach ( $feats as $feat ) {
            $feats_temp[] = $feat;
        }
        sort($feats_temp);
        $feats_list = array();
        $index = 1;
        foreach ( $feats_temp as $feat ) {
            $feats_list[$index] = $feat['name'];
            $index += 1;
        }
        return $feats_list;
    }

    /**
     * has_requirements
     *
     * Checks if requirements are met for the specified feat.
     *
     * @param string $feat_name The feat to retrieve requirements for.
     * @return bool Returns True if requirements met, False if not.
     *
     */
    public function has_requirements($feat_name)
    {
        # Magic Initiative
        if ($feat_name == 'Magic Initiative') {
            $classes = array('Bard', 'Cleric', 'Druid', 'Sorcerer', 'Warlock', 'Wizard');
            if (!in_array($this->__get_class(), $classes))
                return false;
        }
        # Ritual Caster Check
        if ($feat_name == 'Ritual Caster') {
            if ($this->__get_intelligence() < 13 and $this->__get_wisdom() < 13)
                return false;
        }
        # Spell caster Check
        $caster = array(
            'Elemental Adept',
            'Spell Sniper',
            'War Caster'
        );
        if (in_array($feat_name, $caster)) {
            if (!$this->is_caster())
                return false;
        }
        $requirement = $this->__get_requirements($feat_name);
        # Proficiency Check
        if ($requirement['proficiency'] != '-') {
            if (!in_array($requirement['proficiency'], $this->__get_proficiencies()))
                return false;
        }
        # Strength Check
        if ($requirement['strength'] > $this->__get_strength())
            return false;
        # Dexterity Check
        if ($requirement['dexterity'] > $this->__get_dexterity())
            return false;
        # Constitution Check
        if ($requirement['constitution'] > $this->__get_constitution())
            return false;
        # Intelligence Check
        if ($requirement['intelligence'] > $this->__get_intelligence())
            return false;
        # Wisdom Check
        if ($requirement['wisdom'] > $this->__get_wisdom())
            return false;
        # Charisma Check
        if ($requirement['charisma'] > $this->__get_charisma())
            return false;
        return true;
    }

    /**
     * is_caster
     *
     * Determines if character is a spell caster.
     *
     * @return bool True if spell caster, False if not.
     *
     */
    public function is_caster()
    {
        if ($this->__get_class() == 'Bard') {
            if (!$this->is_level(1))
                return false;
        }
        if ($this->__get_class() == 'Cleric') {
            if (!$this->is_level(1))
                return false;
        }
        if ($this->__get_class() == 'Druid') {
            if (!$this->is_level(1))
                return false;
        }
        if ($this->__get_class() == 'Fighter') {
            if (!$this->is_level(3))
                return false;
        }
        if ($this->__get_class() == 'Paladin') {
            if (!$this->is_level(2))
                return false;
        }
        if ($this->__get_class() == 'Ranger') {
            if (!$this->is_level(2))
                return false;
        }
        if ($this->__get_class() == 'Rogue') {
            if (!$this->is_level(3))
                return false;
        }
        if ($this->__get_class() == 'Sorcerer') {
            if (!$this->is_level(1))
                return false;
        }
        if ($this->__get_class() == 'Warlock') {
            if (!$this->is_level(1))
                return false;
        }
        if ($this->__get_class() == 'Wizard') {
            if (!$this->is_level(1))
                return false;
        }
        return true;
    }

    /**
     * is_level
     *
     * Checks if character is of a certain level or higher.
     *
     * @param int $min_level
     * @return bool
     */
    public function is_level($min_level=1)
    {
        if ($this->__get_level() >= $min_level)
            return true;
        return false;
    }
}


/**
 * Seikou Role Playing Game Kit (Information)
 */
class Information
{
    # Data probe types
    const PROBE_TYPE_ALIGNMENT = 100;
    const PROBE_TYPE_CLASS = 201;

    /**
     * __probe
     *
     * Returns query based upon probe.
     *
     * @param int $probe_type Type of data type to use for query.
     * @param string $query Information to query against data probe.
     * @return string
     *
     */
    private function __probe($probe_type, $query)
    {
        $settings = new Settings();
        $connect = $settings->get_database();
        $sql = null;
        if ($probe_type == $this::PROBE_TYPE_ALIGNMENT)
            $sql = 'SELECT description FROM alignments WHERE name=:alignment';
        if ($probe_type == $this::PROBE_TYPE_CLASS)
            $sql = 'SELECT description FROM classes WHERE name=:class';
        $stm = $connect->prepare($sql);
        if ($probe_type == $this::PROBE_TYPE_ALIGNMENT)
            $stm->bindValue(':alignment', $query, \PDO::PARAM_STR);
        if ($probe_type == $this::PROBE_TYPE_CLASS)
            $stm->bindValue(':class', $query, \PDO::PARAM_STR);
        $stm->execute();
        return $stm->fetchColumn();
    }

    /**
     * get_alignment
     *
     * Retrieves description for alignment.
     *
     * @param string $alignment_name Alignment name to retrieve info for.
     * @return string Returns description if found, null if none found.
     *
     */
    public function get_alignment($alignment_name)
    {
        return $this->__probe($this::PROBE_TYPE_ALIGNMENT, $alignment_name);
    }

    /**
     * get_class
     *
     * Retrieves description for class.
     *
     * @param string $class_name Class name to retrieve info for.
     * @return string Returns description if found, Null if none found
     *
     */
    public function get_class($class_name)
    {
        return $this->__probe($this::PROBE_TYPE_CLASS, $class_name);
    }
}


/**
 * Seikou Role Playing Game Kit (Origins)
 */
class Origins
{
    # Origin types
    const ORIGIN_TYPE_ALIGNMENT = 'alignments';
    const ORIGIN_TYPE_CLASS = 'classes';
    const ORIGIN_TYPE_RACE = 'races';

    /**
     * get_origins
     *
     * Returns an array of origins based on category type.
     *
     * @param string $origin_type Origin type to retrieve origins for.
     * @return array Returns an array of origings by origin type.
     *
     */
    public function get_origins($origin_type)
    {
        $settings = new Settings();
        $connect = $settings->get_database();
        $sql = sprintf('SELECT name FROM %s', $origin_type);
        $origin_result = $connect->query($sql);
        $origin_list = array();
        $index = 1;
        foreach ( $origin_result as $row ) {
            $origin_list[$index] = $row['name'];
            $index += 1;
        }
        $settings = null;
        return $origin_list;
    }

    /**
     * is_origin
     *
     * Checks if an origin check is within the origin list.
     *
     * @param string $origin_type Origin type to check origin check against.
     * @param string $origin_check Value to check against origin type.
     * @return bool True if origin_check found, False if not
     *
     */
    public function is_origin($origin_type, $origin_check)
    {
        $origin_list = $this->get_origins($origin_type);
        if ( in_array($origin_check, $origin_list) )
            return true;
        return false;
    }
}


/**
 * Seikou Role Playing Game Kit (Settings)
 */
class Settings
{
    protected $_database;

    public function __construct($database='database/seikourpg.sqlite')
    {
        try {
            if (file_exists($database)) {
                $this->_database = $database;
            } else
                throw new \Exception(
                    "Cannot find the required database: '"
                    . $this->_database
                    . "'!'"
                );
        } catch( \Exception $e ) {
            exit($e->getMessage());
        }
    }

    /**
     * get_database
     *
     * Returns the database path.
     *
     * @return null|\PDO
     *
     */
    public function get_database()
    {
        $database = null;
        try {
            if ( !class_exists('PDO') ) {
                throw new \Exception('PDO Extension not found!');
            }
            $dsn = sprintf('sqlite:%s', $this->_database);
            $database = new \PDO($dsn);
        } catch ( \PDOException $e ) {
            return $database;
        } catch ( \Exception $e ) {
            return $database;
        }
        return $database;
    }

    /**
     * get_version
     *
     * Returns the version number string.
     *
     * @return int
     */
    public function get_version()
    {
        return VERSION;
    }
}


/**
 * Seikou Role Playing Game Kit (Skills)
 */
class Skills
{
    protected $_race;
    protected $_class;
    protected $_strength;
    protected $_dexterity;
    protected $_constitution;
    protected $_intelligence;
    protected $_wisdom;
    protected $_charisma;

    public function __construct(array $kw = array())
    {
        try {
            if (array_key_exists('race', $kw)) {
                $origins = new Origins();
                if ($origins->is_origin($origins::ORIGIN_TYPE_RACE, $kw['race'])) {
                    $this->_race = $kw['race'];
                } else
                    throw new \Exception();
            } else
                throw new \Exception();
        } catch (\Exception $e) {
            $this->_race = 'Human';
        }
        try {
            if (array_key_exists('class_', $kw)) {
                $origins = new Origins();
                if ($origins->is_origin($origins::ORIGIN_TYPE_CLASS, $kw['class_']))
                    $this->_class = $kw['class_'];
                else
                    throw new \Exception();
            } else
                throw new \Exception();
        } catch (\Exception $e) {
            $this->_class = 'Fighter';
        }
        if (array_key_exists('strength', $kw))
            $this->_strength = $kw['strength'];
        else
            $this->_strength = 15;
        if (array_key_exists('dexterity', $kw))
            $this->_dexterity = $kw['dexterity'];
        else
            $this->_dexterity = 14;
        if (array_key_exists('constitution', $kw))
            $this->_constitution = $kw['constitution'];
        else
            $this->_constitution = 13;
        if (array_key_exists('intelligence', $kw))
            $this->_intelligence = $kw['intelligence'];
        else
            $this->_intelligence = 12;
        if (array_key_exists('wisdom', $kw))
            $this->_wisdom = $kw['wisdom'];
        else
            $this->_wisdom = 10;
        if (array_key_exists('charisma', $kw))
            $this->_charisma = $kw['charisma'];
        else
            $this->_charisma = 8;
    }

    /**
     * __get_class
     *
     * Returns class value.
     *
     * @return string
     *
     */
    private function __get_class()
    {
        return $this->_class;
    }

    /**
     * get_allotted
     *
     * Returns allowed number of skills for class.
     *
     * @return int Returns the number of allotted skills by class.
     *
     */
    public function get_allotted()
    {
        $num_of_skills = 0;
        $tier4 = array('Rogue');
        $tier3 = array('Bard', 'Ranger');
        $tier2 = array(
            'Barbarian',
            'Cleric',
            'Druid',
            'Fighter',
            'Monk',
            'Paladin',
            'Sorcerer',
            'Warlock',
            'Wizard'
        );
        if (in_array($this->__get_class(), $tier4))
            $num_of_skills = 4;
        if (in_array($this->__get_class(), $tier3))
            $num_of_skills = 3;
        if (in_array($this->__get_class(), $tier2))
            $num_of_skills = 2;
        $new_tier = array_merge($tier2, $tier3, $tier4);
        if (in_array($this->__get_class(), $new_tier))
            $num_of_skills = 2;
        return $num_of_skills;
    }

    /**
     * get_modifier
     *
     * Returns skill modifier value based on skill.
     *
     * @param string $skill_name Skill to return a modifier for.
     * @return int Returns modifier for the specified skill.
     *
     */
    public function get_modifier($skill_name)
    {
        $settings = new Settings();
        $connect = $settings->get_database();
        $sql = 'SELECT ability FROM skills WHERE name=:skill_name';
        $stm = $connect->prepare($sql);
        $stm->bindValue(':skill_name', $skill_name, \PDO::PARAM_STR);
        $stm->execute();
        $ability = $stm->fetchColumn();
        $connect = null;
        $score = 0;
        if ($ability == 'Strength')
            $score = $this->_strength;
        if ($ability == 'Dexterity')
            $score = $this->_dexterity;
        if ($ability == 'Intelligence')
            $score = $this->_constitution;
        if ($ability == 'Wisdom')
            $score = $this->_wisdom;
        if ($ability == 'Charisma')
            $score = $this->_charisma;
        return intval(floor(($score - 10) / 2));
    }

    /**
     * get_skills
     *
     * Returns an array of skills for a specified class.
     *
     * @param bool|false $show_all If True, shows all skills regardless of class.
     * @return array Returns a dictionary of allowable skills by class.
     *
     */
    public function get_skills($show_all=false)
    {
        $settings = new Settings();
        $connect = $settings->get_database();
        if (!$show_all)
            $sql = sprintf("SELECT name FROM skills WHERE %s='Y'", $this->__get_class());
        else
            $sql = 'SELECT name FROM skills';
        $skills = $connect->query($sql);
        $connect = null;
        $skill_list = array();
        $index = 1;
        foreach ($skills as $skill) {
            $skill_list[$index] = $skill['name'];
            $index += 1;
        }
        return $skill_list;
    }
}
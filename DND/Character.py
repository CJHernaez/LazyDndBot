class Character:
    def __init__(self, dict):
        self.character_name = dict['charactername']
        self.creator_user_id = dict['creator_user_id']
        self.campaign = dict['campaign']
        self.strength = dict['strength']
        self.dexterity = dict['dexterity']
        self.constitution = dict['constitution']
        self.intelligence = dict['intelligence']
        self.wisdom = dict['wisdom']
        self.charisma = dict['charisma']
        self.proficiency = dict['proficiency']
        self.walkingspeed = dict['walkingspeed']
        self.ac = dict['ac']
        self.initiative = dict['initiative']
        self.acrobatics = dict['acrobatics']
        self.animalhandling = dict['animalhandling']
        self.arcana = dict['arcana']
        self.athletics = dict['athletics']
        self.deception = dict['deception']
        self.history = dict['history']
        self.insight = dict['insight']
        self.intimidation = dict['intimidation']
        self.investigation = dict['investigation']
        self.medicine = dict['medicine']
        self.nature = dict['nature']
        self.perception = dict['perception']
        self.performance = dict['performance']
        self.persuasion = dict['persuasion']
        self.religion = dict['religion']
        self.sleightofhand = dict['sleightofhand']
        self.stealth = dict['stealth']
        self.survival = dict['survival']
        self.active = dict['active']

    def toTuple(self):
        return tuple([self.character_name, self.creator_user_id, self.campaign, self.strength, self.dexterity,
                     self.constitution, self.intelligence, self.wisdom, self.charisma, self.proficiency, self.walkingspeed,
                     self.ac, self.initiative, self.acrobatics, self.animalhandling, self.arcana, self.athletics,
                     self.deception, self.history, self.insight, self.intimidation, self.investigation, self.medicine, self.nature,
                     self.perception, self.performance, self.persuasion, self.religion, self.sleightofhand, self.stealth, self.survival, self.active])
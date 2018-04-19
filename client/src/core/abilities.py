
class Ability(object):
	"""docstring for Ability"""
	def __init__(self, arg):
		super(Ability, self).__init__()
		self.arg = arg
	
	def change_rule(self, rule):
		pass

class ChangeCaculateRule(Ability):
	"""docstring for ChangeCaculateRule"""
	def __init__(self, arg):
		super(ChangeCaculateRule, self).__init__()
		self.arg = arg
		
	def change_rule(self, rule):
		'''todo
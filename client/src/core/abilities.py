#import rules
from core.contents import FruitType

class Ability(object):
	"""docstring for Ability"""
	def __init__(self):
		super(Ability, self).__init__()

	def do(rule):
		pass

'''[summary]
改变加减规则的技能
[description]
'''
class ChangeCaculate(Ability):
	"""docstring for ChangeCaculate"""
	def __init__(self, caculate_rule):
		super(ChangeCaculate, self).__init__()
		self.caculate_rule = caculate_rule
		
	def do(rule):
		"""todo"""
		pass

'''[summary]
洗牌
[description]
'''
class ShuffleCards(Ability):
	"""docstring for ShuffleCards"""
	def __init__(self):
		super(ShuffleCards, self).__init__()

	def do(rule):
		#todo
		pass
		
'''[summary]
取消某种蔬菜
[description]
'''
class DisableFruit(Ability):
	"""docstring for ClassName"""
	def __init__(self):
		super(DisableFruit, self).__init__()

	def do(rule, fruit_type):
		#todo
		pass
		
'''[summary]
征集蔬菜
[description]
'''
class CollectFruit(Ability):
	"""docstring for CollectFruit"""
	def __init__(self):
		super(CollectFruit, self).__init__()

	def do(rule, fruit_type):
		#todo
		pass
		
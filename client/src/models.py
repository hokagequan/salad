from enum import Enum
from .core import abilities
from .core import contents

'''[summary]
卡片类型枚举
[description]
'''
@unique
class CardType(Enum):
	NONE = 0
	FRUIT = 1
	POT = 2
	CRUET = 3
	COOK = 4

@unique
class FuitType(Enum):
	"""docstring for FuitType"""
	CHEESE = 1
	ONION = 2
	TOMATO = 3
	CUCUMBER = 4
	OLIVE = 5
	PEPPER = 6


class Card(object):
	"""docstring for card"""
	ctype = CardType.NONE

	def __init__(self, arg):
		super(card, self).__init__()
		self.arg = arg
		
class FuncCard(Card):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		

class FruitCard(Card):
	"""docstring for Fruit"""
	ctype = CardType.Fruit

	def __init__(self, fruits):
		super(Fruit, self).__init__()
		self.fruits = fruits
		

class PotCard(FuncCard):
	"""docstring for POT"""
	ctype = CardType.POT
	'''改为增加规则'''
	increase_ability = ChangeCaculate(CaculateRule.INCREASE)
	'''改为减少规则'''
	decrease_ability = ChangeCaculate(CaculateRule.DECREASE)

	def __init__(self, arg):
		super(POT, self).__init__()
		self.arg = arg
		

class CruetCard(FuncCard):
	"""docstring for Cruet"""
	ctype = CardType.CRUET

	def __init__(self, arg):
		super(Cruet, self).__init__()
		self.arg = arg
		

class CookCard(FuncCard):
	"""docstring for Cook"""
	ctype = CardType.COOK

	def __init__(self, arg):
		super(Cook, self).__init__()
		self.arg = arg
		

class Fruit(object):
	"""docstring for Fruit"""
	def __init__(self, ftype, count):
		super(Fruit, self).__init__()
		self.ftype = ftype
		self.count = count
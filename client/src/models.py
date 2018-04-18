from enum import Enum

'''[summary]
卡片类型枚举
[description]
'''
class CardType(Enum):
	NONE = 0
	FRUIT = 1
	POT = 2
	CRUET = 3
	COOK = 4


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
		

class Fruit(Card):
	"""docstring for Fruit"""
	ctype = CardType.Fruit

	def __init__(self, arg):
		super(Fruit, self).__init__()
		self.arg = arg
		

class POT(FuncCard):
	"""docstring for POT"""
	ctype = CardType.POT

	def __init__(self, arg):
		super(POT, self).__init__()
		self.arg = arg
		

class Cruet(FuncCard):
	"""docstring for Cruet"""
	ctype = CardType.CRUET

	def __init__(self, arg):
		super(Cruet, self).__init__()
		self.arg = arg
		

class Cook(FuncCard):
	"""docstring for Cook"""
	ctype = CardType.COOK
	
	def __init__(self, arg):
		super(Cook, self).__init__()
		self.arg = arg
		
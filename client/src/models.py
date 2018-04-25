
from enum import Enum
from core.abilities import ChangeCaculate
from core.abilities import ShuffleCards
from core.abilities import DisableFruit
from core.abilities import CollectFruit
from core.contents import CaculateRule

'''[summary]
Card type
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

	def __init__(self):
		super(Card, self).__init__()
		
class FuncCard(Card):
	"""docstring for ClassName"""
	def __init__(self):
		super(FuncCard, self).__init__()
		

class FruitCard(Card):
	"""docstring for Fruit"""
	ctype = CardType.FRUIT

	def __init__(self, fruits):
		super(FruitCard, self).__init__()
		self.fruits = fruits
		

class PotCard(FuncCard):
	"""docstring for POT"""
	ctype = CardType.POT
	'''Increase'''
	increase_ability = ChangeCaculate(CaculateRule.INCREASE)
	'''Decrease'''
	decrease_ability = ChangeCaculate(CaculateRule.DECREASE)

	def __init__(self):
		super(PotCard, self).__init__()
		

class CruetCard(FuncCard):
	"""docstring for Cruet"""
	ctype = CardType.CRUET
	#Shuffle
	shuffle_cards = ShuffleCards()

	def __init__(self):
		super(CruetCard, self).__init__()
		

class CookCard(FuncCard):
	"""docstring for Cook"""
	ctype = CardType.COOK
	#Exclude one fruit
	disable_fruit = DisableFruit()
	#Collect on fruit
	collect_fruit = CollectFruit()

	def __init__(self):
		super(CookCard, self).__init__()
		

class Fruit(object):
	"""docstring for Fruit"""
	def __init__(self, ftype, count):
		super(Fruit, self).__init__()
		self.ftype = ftype
		self.count = count

class Person(object):
	"""docstring for Person"""
	def __init__(self):
		super(Person, self).__init__()
		
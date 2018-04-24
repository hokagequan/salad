import models

from core import rules_contents
from core.rules import Rule
from utils import global_util

class World(object):
	"""docstring for World"""
	rules = Rule()
	all_cards = rules_contents.all_cards

	def __init__(self):
		super(World, self).__init__()
		self.prepare()

	def prepare(self):
		# 洗牌
		self.shuffle_cards()

	def shuffle_cards(self):
		global_util.random_list(self.all_cards)
		
		if self.all_cards[-1] is not models.FruitCard:
			self.shuffle_cards()


print(World())
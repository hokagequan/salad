import models
import random

from core import rules_contents
from core.rules import Rule
from utils import global_util

class World(object):
	"""docstring for World"""
	rules = Rule()
	all_cards = rules_contents.all_cards
	persons = []

	def __init__(self):
		super(World, self).__init__()
		self.prepare()

	def prepare(self):
		# Shuffle
		self.shuffle_cards()
		# test
		persons = [models.Person] * 3


	'''[summary]
	Shuffle
	[description]
	'''
	def shuffle_cards(self):
		random.shuffle(self.all_cards)

		if type(self.all_cards[-1]) is not models.FruitCard:
			self.shuffle_cards()

	'''[summary]
	Start
	[description]
	'''
	def start():
		# todo
		pass


print(World())
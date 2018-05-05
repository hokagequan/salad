import models
import random

from core import rules_contents
from core.rules import Rule
from utils import global_util

class World(object):
	"""docstring for World"""
	rules = Rule()
	all_cards = rules_contents.all_cards
	sended_fruit_cards = []
	persons = []
	# Current person index
	cur_p_index = -1

	def __init__(self):
		super(World, self).__init__()
		self.prepare()
		self.start()

	def prepare(self):
		# Shuffle
		self.shuffle_cards()
		# test
		persons = [models.Person] * 3
		cur_p_index = random.randint(0, len(persons))

	def get_next_person(self):
		self.cur_p_index += 1
		self.cur_p_index = cur_p_index if cur_p_index < len(persons) else 0
		return persons[self.cur_p_index]
		 
	# 发牌
	def send_cards(self):
		# 没人发六张牌
		for i in range(0, 6):
			for x in range(0, len(persons)):
				person = get_next_person()
				card = all_cards.pop()
				person.cards.append(card)


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
	def start(self):
		# todo
		# 先出一张水果牌
		card = all_cards.pop()
		sended_fruit_cards.append(card)
		self.send_cards()
		pass


print(World())
import models
import random

from core import rules_contents
from core.rules import Rule
from utils import global_util

class World(object):
	"""docstring for World"""
	def __init__(self):
		super(World, self).__init__()
		self.rules = Rule()
		self.all_cards = rules_contents.all_cards
		self.sended_fruit_cards = []
		self.persons = []
		# Current person index
		self.cur_p_index = -1

		self.prepare()
		self.start()

	def prepare(self):
		# Shuffle
		self.shuffle_cards()
		# test
		self.persons = [models.Person(), models.Person(), models.Person()]
		self.cur_p_index = random.randint(0, len(self.persons))

	def get_next_person(self):
		self.cur_p_index += 1
		self.cur_p_index = self.cur_p_index if self.cur_p_index < len(self.persons) else 0
		return self.persons[self.cur_p_index]

	# 拿牌
	def get_card(self, person):
		card = self.all_cards.pop()
		person.cards.append(card)
		 
	# 发牌
	def send_cards(self):
		# 没人发六张牌
		for i in range(0, 6):
			for x in range(0, len(self.persons)):
				person = self.get_next_person()
				self.get_card(person)


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
		card = self.all_cards.pop()
		self.sended_fruit_cards.append(card)

		self.send_cards()
		print(self.persons)

print(World())
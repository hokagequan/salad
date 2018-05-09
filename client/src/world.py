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

		try:
			self.start_game().send(None)
		except StopIteration as e:
			print(e.value)
		

	def prepare(self):
		# Shuffle
		self.shuffle_cards()
		# test
		self.persons = [models.Person(self.recieve_card), models.Person(self.recieve_card), models.Person(self.recieve_card)]
		self.cur_p_index = random.randint(0, len(self.persons))

		# 先出一张水果牌
		card = self.all_cards.pop()
		self.sended_fruit_cards.append(card)

		self.send_cards()

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
		# 每人发六张牌
		for i in range(0, 6):
			for x in range(0, len(self.persons)):
				person = self.get_next_person()
				self.get_card(person)

	async def start_game(self):
		'''[summary]
		开始游戏
		[description]
		'''
		await self.start_counting_down().send(None)
		print("send card to person")

	async def start_counting_down(self):
		'''[summary]
		开始出牌倒计时
		[description]
		'''
		print("I am async method")

	def shuffle_cards(self):
		'''[summary]
		Shuffle
		[description]
		'''
		random.shuffle(self.all_cards)

		if type(self.all_cards[-1]) is not models.FruitCard:
			self.shuffle_cards()

	def recieve_card(self, card):
		'''[summary]
		接收玩家发送的牌
		[description]
		
		Arguments:
			card {[Card]} -- [所有类型的牌]
		'''
		# todo
		pass


	def recieve_fruit_card(self, fruit_card):
		'''[summary]
		接受水果卡片，判断是否可以出
		[description]
		
		Arguments:
			fruit_card {[FruitCard]} -- [水果牌]
		'''
		if fruit_card.ctype is not rules_contents.car:
			pass

print(World())

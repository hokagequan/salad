import models
import random
import asyncio

from core import rules_contents
from core.rules import Rule
from utils import global_util
from threading import Thread

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
		self.start_game()
		

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

	def start_game(self):
		'''[summary]
		开始游戏
		[description]
		'''
		self.start_counting_down_thread()
		print("send card to person")

	def start_loop(self, loop):
		asyncio.set_event_loop(loop)
		loop.run_forever()

	def start_counting_down_thread(self):
		'''[summary]
		开启倒计时线程
		[description]
		'''
		# new_loop = asyncio.new_event_loop()
		# t = Thread(target=self.start_loop, args=(new_loop,))
		# t.start()

		# new_loop.call_soon_threadsafe(self.start_counting_down)
		new_loop = asyncio.new_event_loop()
		new_loop.call_soon(self.start_counting_down)
		new_loop.run_forever()
		new_loop.close()

	async def start_counting_down(self):
		'''[summary]
		开始出牌倒计时
		[description]
		'''
		count = 60
		while True:
			print("Counting down: {}".format(count))
			await asyncio.sleep(1)
			count -= 1
			if count <= 0:
				# 发牌
				person = self.persons[self.cur_p_index]
				self.get_card(person)
				self.get_next_person()
				count = 60

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

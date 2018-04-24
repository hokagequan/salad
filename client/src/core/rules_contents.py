import models
from core.contents import FruitType

'''[summary]
所有牌组
[description]
'''
all_cards = [ 
# 沙拉盆
models.PotCard(), models.PotCard(), models.PotCard(), models.PotCard(),
# 调味瓶
models.CruetCard(), models.CruetCard(), models.CruetCard(), models.CruetCard(),
# 厨师
models.CookCard(), models.CookCard(), models.CookCard(), models.CookCard(),
# 水果
models.FruitCard([models.Fruit(FruitType.PEPPER, 1), models.Fruit(FruitType.CHEESE, 1), models.Fruit(FruitType.OLIVE, 1), models.Fruit(FruitType.ONION, 3)]),
models.FruitCard([models.Fruit(FruitType.PEPPER, 1), models.Fruit(FruitType.CHEESE, 2), models.Fruit(FruitType.OLIVE, 1), models.Fruit(FruitType.ONION, 2), models.Fruit(FruitType.TOMATO, 1)]),
models.FruitCard([models.Fruit(FruitType.CUCUMBER, 3), models.Fruit(FruitType.ONION, 4)]),
models.FruitCard([models.Fruit(FruitType.PEPPER, 2), models.Fruit(FruitType.CHEESE, 2), models.Fruit(FruitType.ONION, 3)]),
models.FruitCard([models.Fruit(FruitType.PEPPER, 4), models.Fruit(FruitType.TOMATO, 1), models.Fruit(FruitType.CUCUMBER, 1), models.Fruit(FruitType.OLIVE, 1)]),
models.FruitCard([models.Fruit(FruitType.TOMATO, 2), models.Fruit(FruitType.CUCUMBER, 2), models.Fruit(FruitType.OLIVE, 3)]),
models.FruitCard([models.Fruit(FruitType.CHEESE, 2), models.Fruit(FruitType.TOMATO, 4), models.Fruit(FruitType.PEPPER, 1)]),
models.FruitCard([models.Fruit(FruitType.ONION, 4), models.Fruit(FruitType.OLIVE, 2), models.Fruit(FruitType.TOMATO, 1)]),
models.FruitCard([models.Fruit(FruitType.CHEESE, 3), models.Fruit(FruitType.OLIVE, 3)]),
models.FruitCard([models.Fruit(FruitType.TOMATO, 5), models.Fruit(FruitType.CUCUMBER, 2), models.Fruit(FruitType.CHEESE, 1)]),
models.FruitCard([models.Fruit(FruitType.PEPPER, 3), models.Fruit(FruitType.OLIVE, 4)]),
models.FruitCard([models.Fruit(FruitType.PEPPER, 3), models.Fruit(FruitType.TOMATO, 2), models.Fruit(FruitType.OLIVE, 2)]),
models.FruitCard([models.Fruit(FruitType.PEPPER, 1), models.Fruit(FruitType.CUCUMBER, 5), models.Fruit(FruitType.ONION, 2)]),
models.FruitCard([models.Fruit(FruitType.TOMATO, 2), models.Fruit(FruitType.OLIVE, 5), models.Fruit(FruitType.ONION, 1)]),
models.FruitCard([models.Fruit(FruitType.PEPPER, 1), models.Fruit(FruitType.CHEESE, 4), models.Fruit(FruitType.OLIVE, 1), models.Fruit(FruitType.TOMATO, 1)]),
models.FruitCard([models.Fruit(FruitType.TOMATO, 2), models.Fruit(FruitType.ONION, 4)]),
models.FruitCard([models.Fruit(FruitType.CHEESE, 4), models.Fruit(FruitType.ONION, 4)]),
models.FruitCard([models.Fruit(FruitType.TOMATO, 4), models.Fruit(FruitType.CHEESE, 3)]),
models.FruitCard([models.Fruit(FruitType.PEPPER, 3), models.Fruit(FruitType.ONION, 3)]),
models.FruitCard([models.Fruit(FruitType.PEPPER, 5), models.Fruit(FruitType.CUCUMBER, 1), models.Fruit(FruitType.OLIVE, 2)]),
models.FruitCard([models.Fruit(FruitType.CUCUMBER, 2), models.Fruit(FruitType.CHEESE, 5)]),
models.FruitCard([models.Fruit(FruitType.CUCUMBER, 3), models.Fruit(FruitType.OLIVE, 2), models.Fruit(FruitType.ONION, 3)]),
models.FruitCard([models.Fruit(FruitType.TOMATO, 5), models.Fruit(FruitType.PEPPER, 2)]),
models.FruitCard([models.Fruit(FruitType.TOMATO, 4), models.Fruit(FruitType.CHEESE, 1), models.Fruit(FruitType.ONION, 1), models.Fruit(FruitType.CUCUMBER, 1)]),
models.FruitCard([models.Fruit(FruitType.TOMATO, 3), models.Fruit(FruitType.CUCUMBER, 4)]),
models.FruitCard([models.Fruit(FruitType.CUCUMBER, 4), models.Fruit(FruitType.CHEESE, 1), models.Fruit(FruitType.ONION, 1), models.Fruit(FruitType.PEPPER, 1)]),
models.FruitCard([models.Fruit(FruitType.CUCUMBER, 3), models.Fruit(FruitType.CHEESE, 3)]),
models.FruitCard([models.Fruit(FruitType.OLIVE, 5), models.Fruit(FruitType.CHEESE, 2)]),
models.FruitCard([models.Fruit(FruitType.TOMATO, 4), models.Fruit(FruitType.ONION, 4)]),
models.FruitCard([models.Fruit(FruitType.TOMATO, 3), models.Fruit(FruitType.CUCUMBER, 2), models.Fruit(FruitType.ONION, 1), models.Fruit(FruitType.PEPPER, 1)]),
models.FruitCard([models.Fruit(FruitType.TOMATO, 1), models.Fruit(FruitType.OLIVE, 4), models.Fruit(FruitType.ONION, 1), models.Fruit(FruitType.CUCUMBER, 1)]),
models.FruitCard([models.Fruit(FruitType.CUCUMBER, 3), models.Fruit(FruitType.OLIVE, 5)]),
models.FruitCard([models.Fruit(FruitType.TOMATO, 3), models.Fruit(FruitType.CUCUMBER, 3), models.Fruit(FruitType.PEPPER, 2)]),
models.FruitCard([models.Fruit(FruitType.CHEESE, 1), models.Fruit(FruitType.OLIVE, 3), models.Fruit(FruitType.ONION, 2)]),
models.FruitCard([models.Fruit(FruitType.PEPPER, 2), models.Fruit(FruitType.OLIVE, 2), models.Fruit(FruitType.CHEESE, 3)]),
models.FruitCard([models.Fruit(FruitType.PEPPER, 2), models.Fruit(FruitType.OLIVE, 1), models.Fruit(FruitType.CUCUMBER, 4)]),
models.FruitCard([models.Fruit(FruitType.PEPPER, 4), models.Fruit(FruitType.CUCUMBER, 2), models.Fruit(FruitType.ONION, 1)]),
models.FruitCard([models.Fruit(FruitType.TOMATO, 4), models.Fruit(FruitType.OLIVE, 3)]),
models.FruitCard([models.Fruit(FruitType.TOMATO, 3), models.Fruit(FruitType.PEPPER, 3)]),
models.FruitCard([models.Fruit(FruitType.CHEESE, 2), models.Fruit(FruitType.OLIVE, 1), models.Fruit(FruitType.ONION, 5)]),
models.FruitCard([models.Fruit(FruitType.PEPPER, 4), models.Fruit(FruitType.OLIVE, 4)]),
models.FruitCard([models.Fruit(FruitType.TOMATO, 3), models.Fruit(FruitType.OLIVE, 3), models.Fruit(FruitType.CHEESE, 2)]),
models.FruitCard([models.Fruit(FruitType.PEPPER, 3), models.Fruit(FruitType.OLIVE, 3), models.Fruit(FruitType.ONION, 2)]),
models.FruitCard([models.Fruit(FruitType.CHEESE, 2), models.Fruit(FruitType.CUCUMBER, 3), models.Fruit(FruitType.ONION, 2)]),
models.FruitCard([models.Fruit(FruitType.PEPPER, 5), models.Fruit(FruitType.ONION, 2)]),
models.FruitCard([models.Fruit(FruitType.TOMATO, 1), models.Fruit(FruitType.PEPPER, 2), models.Fruit(FruitType.CHEESE, 5)]),
models.FruitCard([models.Fruit(FruitType.TOMATO, 2), models.Fruit(FruitType.CUCUMBER, 1), models.Fruit(FruitType.CHEESE, 4)]),
models.FruitCard([models.Fruit(FruitType.CUCUMBER, 5), models.Fruit(FruitType.CHEESE, 3)])
]
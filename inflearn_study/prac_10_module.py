# import theater_module #모듈 사용
# theater_module.price(3) #3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) #4명이 조조 영화 보러 갔을 때
# theater_module.price_soldier(5) #5명 군인이 영화 보러 갔을 때

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# #from random import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(5)
# price_morning(4)
# #price_soldier(5) #에러. 사용 못함

from theater_module import price_soldier as price
price(5) #군인 할인 가격으로 나옴

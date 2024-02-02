from icecream import ic
from loguru import logger

number = 2



arr = [number*89 for i in range(number)]

logger.warning("Array has been multiplied")
ic(arr)
ic(number)
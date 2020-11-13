class Fund:
	def __init__(self):
		self.__funds = [10]

	def setFund(self, id, amount):
		self.__funds[id] = amount

fundTypes = {0: "Money Market", 1: "Prime Money Market", 2: "Long-Term Bond",
			 3: "Short-Term Bond", 4: "500 Index Fund", 5: "Capital Value Fund",
			 6: "Growth Equity Fund", 7: "Growth Index Fund", 8: "Value Fund",
			 9: "Value Stock Index"}
class client:
	#constructor
	def __init__(self, lName, fName, id):
		self.__fName = fName
		self.__lName = lName
		self.__id = id
		#lists of lists to store history of each fund
		self.__history = [[],[],[],[],[],[],[],[],[],[]]

		self.__funds = []
		for x in range(0,10):
			self.__funds.append(0)

	#getters
	def getFirstName(self):
		return self.__fName

	def getLastName(self):
		return self.__lName

	def getId(self):
		return self.__id

	def getHistory(self):
		return self.__history

	def getFunds(self):
		return self.__funds
	#setters
	def setFirstName(self, fName):
		self.__fName = fName
	
	#helper methods
	def addToHistory(self, action):
		self.__history.append(action)
	
	def depositFunds(self, fundID, amount):
		#add money to specific fund
		self.__funds[fundID] += amount
		#add action to history of fund
		message = "${amount} deposited".format(amount=amount)
		self.__history[fundID].append(message)

	def withdrawlFunds(self, fundID, amount):
		startingFunds = self.__funds[fundID]
		#if starting account has enough money
		if startingFunds >= amount:
			self.__funds[fundID] -= amount
			message = "${amount} withdrawn".format(amount=amount)
			self.__history[fundID].append(message)
			return True
		#else need to check linked funds
		elif fundID >= 0 and fundID <= 3:
			#fund 0 is linked with fund 1
			if fundID == 0:
				additionalFunds = self.__funds[1]
				totalFunds = startingFunds + additionalFunds
				#see if total money is at least what is wanted to be withdrawn
				if totalFunds >= amount:
					#clear funds from starting fund
					self.__funds[fundID] = 0
					#get reduced amount
					amount -= startingFunds
					#update funds in linked acount
					self.__funds[1] -= amount
					#add to history of fund
					message = "$" + str(startingFunds) + " withdrawn from " + fundTypes[fundID] + " and $" + str(amount) + " withdrawn from " + fundTypes[1] + " to cover balance"
					self.__history[fundID].append(message)					
					return True
				else:
					#not enough money between funds, send error to bank and make note in history
					message = "ERROR: Treid to withdraw $" + str(amount) + " from " + fundTypes[fundID] + " but there was not enough money between that fund and " + fundTypes[1] + " fund to cover total amount requested"
					self.__history[fundID].append(message)
					return False
			#fund 1 is linked with fund 0
			elif fundID == 1:
				additionalFunds = self.__funds[0]
				totalFunds = startingFunds + additionalFunds
				#see if total money is at least what is wanted to be withdrawn
				if totalFunds >= amount:
					#clear funds from starting fund
					self.__funds[fundID] = 0
					amount -= startingFunds
					self.__funds[0] -= amount
					message = "$" + str(startingFunds) + " withdrawn from " + fundTypes[fundID] + " and $" + str(amount) + " withdrawn from " + fundTypes[0] + " to cover balance"
					self.__history[fundID].append(message)
					return True
				else:
					message = "ERROR: Treid to withdraw $" + str(amount) + " from " + fundTypes[fundID] + " but there was not enough money between that fund and " + fundTypes[0] + " fund to cover total amount requested"
					self.__history[fundID].append(message)
					return False
			#fund 2 is linked with fund 3
			elif fundID == 2:	
				additionalFunds = self.__funds[3]
				totalFunds = startingFunds + additionalFunds
				#see if total money is at least what is wanted to be withdrawn
				if totalFunds >= amount:
					#clear funds from starting fund
					self.__funds[fundID] = 0
					amount -= startingFunds
					self.__funds[3] -= amount
					#message = "${startingFund} withdrawn from fundID {fundID}, and ${amount} withdrawn from linked account to cover balance".format(startingFund=startingFunds, fundID=fundID, amount=amount)
					message = "$" + str(startingFunds) + " withdrawn from " + fundTypes[fundID] + " and $" + str(amount) + " withdrawn from " + fundTypes[3] + " to cover balance"
					self.__history[fundID].append(message)
					return True
				else:
					message = "ERROR: Treid to withdraw $" + str(amount) + " from " + fundTypes[fundID] + " but there was not enough money between that fund and " + fundTypes[3] + " fund to cover total amount requested"
					self.__history[fundID].append(message)
					return False	
			#else fund 3 is linked with fund 2
			else:
				additionalFunds = self.__funds[2]
				totalFunds = startingFunds + additionalFunds
				#see if total money is at least what is wanted to be withdrawn
				if totalFunds >= amount:
					#clear funds from starting fund
					self.__funds[fundID] = 0
					amount -= startingFunds
					self.__funds[2] -= amount
					message = "$" + str(startingFunds) + " withdrawn from " + fundTypes[fundID] + " and $" + str(amount) + " withdrawn from " + fundTypes[2] + " to cover balance"
					self.__history[fundID].append(message)
					return True
				else:
					message = "ERROR: Treid to withdraw $" + str(amount) + " from " + fundTypes[fundID] + " but there was not enough money between that fund and " + fundTypes[2] + " fund to cover total amount requested"
					self.__history[fundID].append(message)
					return False
		#not enough money in starting fund, and not trying to pull from a linked fund, record in history and throw error
		else:
			message = "ERROR: Tried to withdraw ${amount} but there was not enough money in the fund".format(amount=amount)
			self.__history[fundID].append(message)
			return False
	
	#print client summary
	def printClient(self):
		print(self.__fName + " " + self.__lName + " Account ID: " + self.__id)
		for x in range(0, 10):
			message = "    " + fundTypes[x] + ": $"
			message += str(self.__funds[x])
			print(message)
	#print a detailed history of the clients account
	def printClientHistory(self):
		for x in range(0, len(self.__history)):
			print(fundTypes[x] + ": $" + str(self.__funds[x]))
			for i in range(0, len(self.__history[x])):
					print("    " + self.__history[x][i])
	
	#just print a history of a singular fund
	def printFund(self, fundID):
		message = "Transaction history for " + self.__fName + " " + self.__lName
		message += " " + fundTypes[fundID] + ": $" + str(self.__funds[fundID])
		print(message)
		for x in range(0, len(self.__history[fundID])):
			print("    " + self.__history[fundID][x])
			
import queue
import tree
import client

class Bank:
	def __init__(self):
		self.__transactions = queue.Queue()
		self.__clients = tree.BinarySearchTree()
		self.__clientIDs = []
	
	#getters
	def getQueue(self):
		return self.__transactions

	#helper methods
	def readTransactions(self, file):
		#open file and read through it line by line
		file = open(str(file), "r")
		for line in file:
			#split each line based on spaces
			splitLine = line.split()
			self.__transactions.put(splitLine)
		#close file
		file.close()

	def executeTransactions(self):
		#go through each transaction one at a time until queue is empty
		while not self.__transactions.empty():
			x = self.__transactions.get()
			#open account
			if x[0] == "O":	
				#if client doesn't exist: make a new one
				if self.__clients.get(x[3]) == None:
					newClient = client.client(x[1], x[2], x[3])
					self.__clients.put(x[3], newClient)
					self.__clientIDs.append(x[3])
				#if client does exist: post error to console
				else:
					print("ERROR: Account " + x[3] + " is already open.  Transaction refused")
			#deposit into account
			elif x[0] == "D":
				#get account id
				key = x[1] 
				#get node matching id
				updateNode = self.__clients.get(key[0:4]) 
				#check client actually exists
				if updateNode != None:
					#check if fund id is larger than allowed 
					if len(key[4:]) <= 1:
						#update specific fund within node
						if eval(x[2]) >= 0:
							updateNode.depositFunds(eval(key[4:]), eval(x[2]))
						else:
							print("ERROR: Tried to deposit a negative number.  Transaction refused")
						#return node to tree
						self.__clients.put(key[0:4], updateNode)
					else: 
						print("That fund does not exist within this account")
				else:
					print("ERROR: Account " + key[0:4] + " not found.  Transaction refused.")
			#withdraw from account
			elif x[0] == "W":
				#get account id
				key = x[1]
				#get node matching id
				updateNode = self.__clients.get(key[0:4])
				#check if client actually exists
				if updateNode != None:
					#if fund ids are valid
					if len(key[4:]) <= 1:
						#attempt to update node
						if eval(x[2]) >= 0:
							success = updateNode.withdrawlFunds(eval(key[4:]), eval(x[2]))
							#if able to withdraw return node to tree
							if success:
								self.__clients.put(key[0:4], updateNode)
							#else do nothing and throw error
							else:
								print("ERROR: Not enough funds to withdraw $" + x[2] + " from " + updateNode.getFirstName() + " " + updateNode.getLastName() + " " + client.fundTypes[eval(key[4:])])
						else:
							print("ERROR: Tried to withdraw a negative number.  Transaction refused")
					#fund id is invalid
					else:
						print("ERROR: fund id not found.  Transaction refused")
				#client id doesn't exist
				else:
					print("ERROR: Account " + key[0:4] + " not found.  Transaction refused.")
			#trasnfer between either two funds within one account or between seperate accounts
			elif x[0] == "T":
				#get account ids
				keyFrom = x[1]
				keyTo = x[3]
				#get clients with ids
				updateFromNode = self.__clients.get(keyFrom[0:4])
				updateToNode = self.__clients.get(keyTo[0:4])
				#check if client exists
				if updateFromNode != None and updateToNode != None:
					#get fund ids
					fromID = eval(keyFrom[4:])
					toID = eval(keyTo[4:])
					if eval(x[2]) < 0:
						print("ERROR: Tried to transfer a negative number.  Transaction refused")
					else:
						#if fund ids are within range
						if fromID in range(0,10) and toID in range(0,10):
							#attempt withdrawl from first account
							successWithdraw = updateFromNode.withdrawlFunds(fromID, eval(x[2]))
							#if client has funds available
							if success:
								#check if transferring between same account
								if keyFrom[0:4] == keyTo[0:4]:
									#deposite back into from account
									updateFromNode.depositFunds(toID, eval(x[2]))
								#else transferring to another account
								else:
									#deposite into to account
									updateToNode.deposit(toID, eval(x[2]))
								#put both updated nodes back into the tree
								self.__clients.put(keyFrom[0:4], updateFromNode)
								self.__clients.put(keyTo[0:4], updateToNode)
							#if client does not have the funds
							else:
								#print error message to the console
								print("ERROR: Account " + keyFrom[0:4] + "doesn't not have the funds required to transfer requested amount. Transaction refused")
				#client doesn't exist
				else:
					print("ERROR: One or both accounts not found.  Transfer refused.")
			#print history of either entire client or specific fund
			elif x[0] == "H":
				#get client
				key = x[1]
				updateNode = self.__clients.get(key[0:4])
				if updateNode != None:
					fundID = key[4:]
					#if just client
					if len(fundID) == 0:
						#run through all funds that have a history longer than 0
						print("Transaction history for " + updateNode.getFirstName() + " " + updateNode.getLastName() + " by fund.")
						updateNode.printClientHistory()
					#else if just a fund of client
					else:
						#check if fund id is valid
						if eval(fundID) in range(0, 10):
							updateNode.printFund(eval(fundID))
						else:
							print("ERROR: Invalid fund id requested.  Transaction denied")
			else:
				break
	#print all client account summaries in bank
	def printClients(self):
		for key in self.__clientIDs:
			client = self.__clients.get(key)
			client.printClient()
			print()
		
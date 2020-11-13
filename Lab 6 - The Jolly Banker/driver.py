import bank
import tree

#create a bank
b = bank.Bank()
#read in transactions
b.readTransactions("BankTransIn.txt")
#run all the transactions
b.executeTransactions()
print()
print("Processng Done. Final Balances")
#print clients
b.printClients()
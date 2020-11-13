# Jolly Banker
 CSS 340 Assignment 6: The Jolly Banker
	
	Purpose
		This lab will serve a few purposes. First, it will provide hands-on experience using both queues
		and binary search trees. It will also provide an opportunity for further program/class design as
		the project does not specifically delineate class structure or design.
		
		Note also that there may be some ambiguity in the spec below so please make sure to ask any
		clarifying questions early.
		
	Problem Overview:
		You will build a banking application which processes transactions. This banking
		application consists of three phases.
		
		1) The program will read in a string of transactions from a file into an in-memory queue.
		These transactions can open accounts, withdraw funds, deposit funds, transfer funds, or ask for
		the transactional history to be printed.
		
		2) The program will next read from the queue and process the transactions in order.
		
		3) When the queue has been depleted the program will print out all open accounts and
		balances in those accounts.
	
	Details:
		Input:
			To test your program a file called BankTransIn.txt will be utilized. You program should
			assume a file with this exact name. We will use different variants of this file for testing.
			Transactions of the format described below (see section on transactions) will be contained in
			this file. There will be one transaction per line.
			
			Assume that the input is well-formed—that is, there are no syntax errors. That said,
			there may be errors in the transactions themselves. For instance, a transaction may try to
			withdraw more money than there is a fund or try to withdraw for a non-existent fund. See the
			section below entitled errors for details.
		
		Client Accounts and Funds:
			Each client account contains assets held in up to ten funds. A client account is
			represented by a first and last name (two strings) and a unique 4 digit identifier. A fifth digit
			can be added to the digit id to represent the individual fund within the account as enumerated
			below:
				0: Money Market 5: Capital Value Fund
				1: Prime Money Market 6: Growth Equity Fund
				2: Long-Term Bond 7: Growth Index Fund
				3: Short-Term Bond 8: Value Fund
				4: 500 Index Fund 9: Value Stock Index
			For instance, 23452 represents the Long-Term Bond fund for client account 2345. A
			client account is opened as a transaction (see below).
		
		Transactions:
			There are five types of transactions and each are identified by a character beginning the line.
				O: Open a client account with the appropriate funds
				D: Deposit assets into a fund
				W: Withdraw assets from a fund
				T: Transfer assets between funds (can be funds owned by a single client or
				transfers between clients)
				H: Display the history of all transactions for a client account or for a single fund.
				Include errors in the output where appropriate.
				After this character key, the account-fund number is given followed by relevant information for
				the transaction.
			Examples:
				D 12341 100 Deposit $100 into the prime money market account of client ID 1234
				W 12340 500 Withdraw $500 from the money market of client ID 1234.
				T 12340 1000 12341 Transfer $1000 from client 1234's money market to the prime money market.
				T 12340 1000 56780 Transfer $1000 from 1234's money market to 5678's money market.
				H 1234 Display the history of all transactions of all accounts for client 1234.
				H 12344 Display the history for all transactions on the 500 Index Fund for client 1234
				O Bowden Charles 6537 Open an account for client Charles Bowden. Use account id 6537.
		
		Errors:
			As noted above, assume the format (number and types of input items) are correct. However,
			the program should deal with all other types of errors. For instance, there could be a bad
			account number (for instance, one already used) or an amount which is too much to withdraw.
			Also, assume that each line will begin with an appropriate letter: O, W, D, H, or T.

			Examples of errors which may occur:
				W 65439 10000 (when the Value Stock Index of client 6543 has only $20)
				D 765435 76
			
			A transaction that would cause a balance to become negative should not occur and is an error.
			There is one exception to this rule: if you are withdrawing from a money market fund with
			insufficient dollars, and it can be covered with dollars from the other money market fund
			owned by the client account, the desired amount (only the partial amount needed to cover the
			withdrawal) is moved to that money market account. The two Bond accounts are handled
			similarly. No other types of accounts are handled in this manner.
			
			Appropriate error messages should be printed out to the console. No other messages should
			be printed out during phase 1 or phase 2.
		
		Output:
			In Phase 3, each client account will be printed out with the amount held in each
			account. Please make sure to create an intuitive and readable output for this aspect of the
			program. This should be part of the design.
		
		Data Structures:
			One key aspect of this Lab exercise is the right class design for handling the problem. So
			in general there is no pre-defined classes or signature structure for the classes required. This is
			up to you to define. However, there are two data structures which are required.
			
			First, you need to use a queue to read the transactions into during phase 1. All
			transactions should be read before processing starts. You can use the queue found in the
			queue module if you like.
			
			Second, the client accounts should be stored in a binary search tree (BSTree). You
			should design and code the BST. We have spent time in class on making progress on this.
	Grade:
		81 / 90
			-7: Design - No Transaction class
			-2: BST Remove - No description

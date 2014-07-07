
operand = [] #stack
operator = []
operatorList = ['+', '-', '*', '/']
tempNum = [] #numbers can be more than 1 character long

while True:
	print "-----Enter a an arithmetic expression with full parentheses.-----"
	prompt = '>>>>>> '
	answer = raw_input(prompt).replace(' ', '');

	for c in answer:
		isOperator = False

		#assume answer can't start with operator
		if c in operatorList: 
			isOperator = True
		if isOperator:
			operator.append(c)

		if tempNum and (c == ')' or isOperator):
			fullNumber = "".join(tempNum)
			operand.append(float(fullNumber))
			del tempNum[:]

		#at this point, there exists at least 2 operands and 1 operator
		if c == ')':
			currentOp = operator.pop()
			mostRecentVal = operand.pop() #pop here to preserve order
			if currentOp == '+': result = (operand.pop() + mostRecentVal)
			elif currentOp == '-': result = (operand.pop() - mostRecentVal)
			elif currentOp == '*': result = (operand.pop() * mostRecentVal)
			elif currentOp == '/': result = (operand.pop() / mostRecentVal)
			operand.append(result)

		elif not isOperator and c != '(':
			#variable c is an operand here
			tempNum.append(c)


	print '\n' + str(operand.pop())

	print "\nAnother? n for no"
	another = raw_input(prompt);
	if another == 'n':
		break
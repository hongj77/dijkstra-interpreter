
operand = []
operator = []


while True:

	print "Enter a an arithmetic expression with full parentheses."
	prompt = '>>>>>> '
	answer = raw_input(prompt);

	for c in answer:
		if c == '(': pass
		elif c == '+': operator.append(c)
		elif c == '-': operator.append(c)		
		elif c == '*': operator.append(c)
		elif c == '/': operator.append(c)
		elif c == ')':
			currentOp = operator.pop()
			mostRecentVal = operand.pop() #pop here to preserve order
			if currentOp == '+': result = (operand.pop() + mostRecentVal)
			elif currentOp == '-': result = (operand.pop() - mostRecentVal)
			elif currentOp == '*': result = (operand.pop() * mostRecentVal)
			elif currentOp == '/': result = (operand.pop() / mostRecentVal)
			operand.append(result)
		else:
			#variable c is an operand here
			operand.append(float(c))

	print '\n' + operand.pop()
	print "\nAnother? (y/n)"
	another = raw_input(prompt);
	if another == 'n':
		break
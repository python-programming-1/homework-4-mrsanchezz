def sentence(aList):
	last = len(aList)
	for i,item in enumerate(aList):
		if i == 0:
			sentence = str(item) + ', '
		elif i < last - 1:
			sentence = sentence + str(item) + ', '
		elif i == last - 1:
			sentence = sentence + 'and ' + str(item) + '.'
			return print(sentence)

aList = ['apples','oranges', 'grapes']
sentence(aList)
import copy

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

dotL = []
zeroL = []

for i in range(len(grid)):
	for j in range(len(grid[0])):
		if grid[i][j] == '.':
			dotL.append(grid[i][j])
		else:
			zeroL.append(grid[i][j])

dotL = dotL[0:9]
zeroL = zeroL[0:7]
size = len(dotL)

line0 = copy.deepcopy(dotL)
line1 = copy.deepcopy(dotL)
line2 = copy.deepcopy(dotL)
line3 = copy.deepcopy(dotL)
line4 = copy.deepcopy(dotL)
line5 = copy.deepcopy(dotL)

line0[2:4] = zeroL[0:2]
line0[5:7] = zeroL[0:2]
line1[1:8] = zeroL
line2 = copy.deepcopy(line1)
line3[2:7] = zeroL[0:5]
line4[3:6] = zeroL[0:3]
line5[4] = zeroL[0]

for i,val in enumerate(line0):
	if i < size-1:
		print(val, end='')
	else:
		print(val)

for i,val in enumerate(line1):
	if i < size-1:
		print(val, end='')
	else:
		print(val)

for i,val in enumerate(line2):
	if i < size-1:
		print(val, end='')
	else:
		print(val)

for i,val in enumerate(line3):
	if i < size-1:
		print(val, end='')
	else:
		print(val)

for i,val in enumerate(line4):
	if i < size-1:
		print(val, end='')
	else:
		print(val)

for i,val in enumerate(line5):
	if i < size-1:
		print(val, end='')
	else:
		print(val)
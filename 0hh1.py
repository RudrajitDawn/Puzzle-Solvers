grid=[['.','.','R','.','B','B','.','B','.','.','B','.'],
      ['.','.','R','.','B','B','.','.','.','.','B','R'],
      ['.','.','.','.','.','.','.','.','.','R','.','.'],
      ['.','.','.','.','.','.','.','B','.','.','.','.'],
      ['.','.','.','.','.','R','.','.','.','B','.','B'],
      ['.','.','.','.','R','.','B','.','B','.','.','.'],
      ['B','.','.','R','R','.','.','R','B','.','B','.'],
      ['.','.','.','R','.','.','.','.','.','.','.','.'],
      ['.','.','B','.','.','R','.','.','.','.','R','.'],
      ['B','.','B','.','.','.','.','B','.','.','.','.'],
      ['.','.','.','B','B','.','.','.','.','B','.','B'],
      ['.','.','.','.','R','R','.','B','.','.','.','.']]
row=12
col=12
def fn(grid,i,j,i1,j1,i2,j2,c1,c2):
	if row>i1>-1 and row>i2>-1 and col>j1>-1 and col>j2>-1:
		if grid[i][j]=='.' and grid[i1][j1]==c1 and grid[i2][j2]==c1:
			grid[i][j]=c2
while True:
	for i in range(row):
		for j in range(col):
			fn(grid,i,j,i+1,j,i+2,j,'B','R')
			fn(grid,i,j,i-1,j,i-2,j,'B','R')
			fn(grid,i,j,i,j+1,i,j+2,'B','R')
			fn(grid,i,j,i,j-1,i,j-2,'B','R')
			fn(grid,i,j,i+1,j,i+2,j,'R','B')
			fn(grid,i,j,i-1,j,i-2,j,'R','B')
			fn(grid,i,j,i,j+1,i,j+2,'R','B')
			fn(grid,i,j,i,j-1,i,j-2,'R','B')
			fn(grid,i,j,i+1,j,i-1,j,'B','R')
			fn(grid,i,j,i,j+1,i,j-1,'B','R')
			fn(grid,i,j,i+1,j,i-1,j,'R','B')
			fn(grid,i,j,i,j+1,i,j-1,'R','B')
	for i in range(row):
		tr,tb=0,0
		for j in range(col):
			if grid[i][j]=='R':
				tr+=1
			elif grid[i][j]=='B':
				tb+=1
		if tr==col/2:
			for j in range(col):
				if grid[i][j]=='.':
					grid[i][j]='B'
		elif tb==col/2:
			for j in range(col):
				if grid[i][j]=='.':
					grid[i][j]='R'
	for j in range(col):
		tr,tb=0,0
		for i in range(row):
			if grid[i][j]=='R':
				tr+=1
			elif grid[i][j]=='B':
				tb+=1
		if tr==row/2:
			for i in range(row):
				if grid[i][j]=='.':
					grid[i][j]='B'
		elif tb==row/2:
			for i in range(row):
				if grid[i][j]=='.':
					grid[i][j]='R'
	for i in range(row):
		n=0
		for j in range(col):
			if grid[i][j]=='.':
				n+=1
		if n==2:
			for i1 in range(row):
				ff=0
				if i!=i1:
					for j in range(col):
						if grid[i][j]!='.' and grid[i1][j]!=grid[i][j]:
							ff=1
				if ff==0:
					for j in range(col):
						if grid[i][j]=='.' and grid[i1][j]=='R':
							grid[i][j]='B'
						elif grid[i][j]=='.' and grid[i1][j]=='B':
							grid[i][j]='R'
	for j in range(col):
		n=0
		for i in range(row):
			if grid[i][j]=='.':
				n+=1
		if n==2:
			for j1 in range(col):
				ff=0
				if j!=j1:
					for i in range(row):
						if grid[i][j]!='.' and grid[i][j1]!=grid[i][j]:
							ff=1
				if ff==0:
					for i in range(row):
						if grid[i][j]=='.' and grid[i][j1]=='R':
							grid[i][j]='B'
						elif grid[i][j]=='.' and grid[i][j1]=='B':
							grid[i][j]='R'
	f=0
	for i in range(row):
		for j in range(col):
			if grid[i][j]=='.':
				f=1
	if f==0:
		break
for i in range(row):
	print(grid[i])

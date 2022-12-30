grid = [['/', '.', '.', '/', '.', '.'], 
        ['.', '.', '.', '.', '.', '.'], 
        ['/', '.', '.', '.', '.', '/'], 
        ['.', '/', '.', '.', '.', '.'], 
        ['.', '/', '.', '.', '.', '.'], 
        ['.', '.', '.', '.', '/', '/']]
depth = 11
dim = 6
C1, C2, C3 = {'row':1, 'col':0}, {'row':1, 'col':3}, {'row':5, 'col':0}
c1, c2, c3 = {'row':5, 'col':1}, {'row':5, 'col':2}, {'row':5, 'col':3}
cs = [c1, c2, c3]

visited_positions = []
t1, t2, t3 = {}, {}, {}
t1['row'], t1['col'], t2['row'], t2['col'], t3['row'], t3['col'] = C1['row'], C1['col'], C2['row'], C2['col'], C3['row'], C3['col']
visited_positions.append({'C1':t1, 'C2':t2, 'C3':t3})

def find_path(dim, grid, depth, present_depth, stored_path, C1, C2, C3, c1, c2, c3, cs, visited_positions, instruction):
	if present_depth > depth:
		return
	#if C1['row'] == c1['row'] and C1['col'] == c1['col'] and C2['row'] == c2['row'] and C2['col'] == c2['col'] and C3['row'] == c3['row'] and C3['col'] == c3['col']:
	if C1 in cs and C2 in cs and C3 in cs:
		print(stored_path)
		exit(0)
	if instruction == 'U':
		for __ in range(3):
			for _ in range(dim - 1):
				if C1['row'] != 0 and grid[C1['row']-1][C1['col']] != '/' and (C1['row']-1 != C2['row'] or C1['col'] != C2['col']) and (C1['row']-1 != C3['row'] or C1['col'] != C3['col']):
					C1['row'] -= 1
			for _ in range(dim - 1):
				if C2['row'] != 0 and grid[C2['row']-1][C2['col']] != '/' and (C2['row']-1 != C1['row'] or C2['col'] != C1['col']) and (C2['row']-1 != C3['row'] or C2['col'] != C3['col']):
					C2['row'] -= 1
			for _ in range(dim - 1):
				if C3['row'] != 0 and grid[C3['row']-1][C3['col']] != '/' and (C3['row']-1 != C1['row'] or C3['col'] != C1['col']) and (C3['row']-1 != C2['row'] or C3['col'] != C2['col']):
					C3['row'] -= 1
	if instruction == 'D':
		for __ in range(3):
			for _ in range(dim - 1):
				if C1['row'] != dim - 1 and grid[C1['row']+1][C1['col']] != '/' and (C1['row']+1 != C2['row'] or C1['col'] != C2['col']) and (C1['row']+1 != C3['row'] or C1['col'] != C3['col']):
					C1['row'] += 1
			for _ in range(dim - 1):
				if C2['row'] != dim - 1 and grid[C2['row']+1][C2['col']] != '/' and (C2['row']+1 != C1['row'] or C2['col'] != C1['col']) and (C2['row']+1 != C3['row'] or C2['col'] != C3['col']):
					C2['row'] += 1
			for _ in range(dim - 1):
				if C3['row'] != dim - 1 and grid[C3['row']+1][C3['col']] != '/' and (C3['row']+1 != C1['row'] or C3['col'] != C1['col']) and (C3['row']+1 != C2['row'] or C3['col'] != C2['col']):
					C3['row'] += 1
	if instruction == 'L':
		for __ in range(3):
			for _ in range(dim - 1):
				if C1['col'] != 0 and grid[C1['row']][C1['col']-1] != '/' and (C1['row'] != C2['row'] or C1['col']-1 != C2['col']) and (C1['row'] != C3['row'] or C1['col']-1 != C3['col']):
					C1['col'] -= 1
			for _ in range(dim - 1):
				if C2['col'] != 0 and grid[C2['row']][C2['col']-1] != '/' and (C2['row'] != C1['row'] or C2['col']-1 != C1['col']) and (C2['row'] != C3['row'] or C2['col']-1 != C3['col']):
					C2['col'] -= 1
			for _ in range(dim - 1):
				if C3['col'] != 0 and grid[C3['row']][C3['col']-1] != '/' and (C3['row'] != C1['row'] or C3['col']-1 != C1['col']) and (C3['row'] != C2['row'] or C3['col']-1 != C2['col']):
					C3['col'] -= 1
	if instruction == 'R':
		for __ in range(3):
			for _ in range(dim - 1):
				if C1['col'] != dim - 1 and grid[C1['row']][C1['col']+1] != '/' and (C1['row'] != C2['row'] or C1['col']+1 != C2['col']) and (C1['row'] != C3['row'] or C1['col']+1 != C3['col']):
					C1['col'] += 1
			for _ in range(dim - 1):
				if C2['col'] != dim - 1 and grid[C2['row']][C2['col']+1] != '/' and (C2['row'] != C1['row'] or C2['col']+1 != C1['col']) and (C2['row'] != C3['row'] or C2['col']+1 != C3['col']):
					C2['col'] += 1
			for _ in range(dim - 1):
				if C3['col'] != dim - 1 and grid[C3['row']][C3['col']+1] != '/' and (C3['row'] != C1['row'] or C3['col']+1 != C1['col']) and (C3['row'] != C2['row'] or C3['col']+1 != C2['col']):
					C3['col'] += 1
	for p in visited_positions:
		#if p['C1']['row'] == C1['row'] and p['C1']['col'] == C1['col'] and p['C2']['row'] == C2['row'] and p['C2']['col'] == C2['col'] and p['C3']['row'] == C3['row'] and p['C3']['col'] == C3['col']:
		if p['C1'] in cs and p['C2'] in cs and p['C3'] in cs:
			return
	t1, t2, t3 = {}, {}, {}
	t1['row'], t1['col'], t2['row'], t2['col'], t3['row'], t3['col'] = C1['row'], C1['col'], C2['row'], C2['col'], C3['row'], C3['col']
	stored_path += instruction
	if instruction == 'L' or instruction == 'R':
		find_path(dim, grid, depth, present_depth + 1, stored_path, {'row':C1['row'], 'col':C1['col']}, {'row':C2['row'], 'col':C2['col']}, {'row':C3['row'], 'col':C3['col']}, c1, c2, c3, cs, visited_positions + [{'C1':t1, 'C2':t2, 'C3':t3}], 'U')
		find_path(dim, grid, depth, present_depth + 1, stored_path, {'row':C1['row'], 'col':C1['col']}, {'row':C2['row'], 'col':C2['col']}, {'row':C3['row'], 'col':C3['col']}, c1, c2, c3, cs, visited_positions + [{'C1':t1, 'C2':t2, 'C3':t3}], 'D')
	else:
		find_path(dim, grid, depth, present_depth + 1, stored_path, {'row':C1['row'], 'col':C1['col']}, {'row':C2['row'], 'col':C2['col']}, {'row':C3['row'], 'col':C3['col']}, c1, c2, c3, cs, visited_positions + [{'C1':t1, 'C2':t2, 'C3':t3}], 'L')
		find_path(dim, grid, depth, present_depth + 1, stored_path, {'row':C1['row'], 'col':C1['col']}, {'row':C2['row'], 'col':C2['col']}, {'row':C3['row'], 'col':C3['col']}, c1, c2, c3, cs, visited_positions + [{'C1':t1, 'C2':t2, 'C3':t3}], 'R')

find_path(dim, grid, depth, 0, '', {'row':C1['row'], 'col':C1['col']}, {'row':C2['row'], 'col':C2['col']}, {'row':C3['row'], 'col':C3['col']}, c1, c2, c3, cs, visited_positions, 'U')
find_path(dim, grid, depth, 0, '', {'row':C1['row'], 'col':C1['col']}, {'row':C2['row'], 'col':C2['col']}, {'row':C3['row'], 'col':C3['col']}, c1, c2, c3, cs, visited_positions, 'D')
find_path(dim, grid, depth, 0, '', {'row':C1['row'], 'col':C1['col']}, {'row':C2['row'], 'col':C2['col']}, {'row':C3['row'], 'col':C3['col']}, c1, c2, c3, cs, visited_positions, 'L')
find_path(dim, grid, depth, 0, '', {'row':C1['row'], 'col':C1['col']}, {'row':C2['row'], 'col':C2['col']}, {'row':C3['row'], 'col':C3['col']}, c1, c2, c3, cs, visited_positions, 'R')

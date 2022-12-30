from itertools import permutations
nmbrs=[int(s) for s in raw_input('Enter numbers: ').split()]
rslt=int(input('Enter result: '))
perm=permutations(nmbrs)
o={}
o[0]='+'
o[1]='-'
o[2]='*'
o[3]='/'
for n in list(perm):
	a,b,c,d=str(n[0])+'.0',str(n[1])+'.0',str(n[2])+'.0',str(n[3])+'.0'
	for i in range(4):
		for j in range(4):
   			for k in range(4):
   				try:
					if eval(a+o[i]+b+o[j]+c+o[k]+d)==rslt:
						print(a+o[i]+b+o[j]+c+o[k]+d)
						exit()
					if eval('('+a+o[i]+b+')'+o[j]+c+o[k]+d)==rslt:
						print('('+a+o[i]+b+')'+o[j]+c+o[k]+d)
						exit()
					if eval(a+o[i]+'('+b+o[j]+c+')'+o[k]+d)==rslt:
						print(a+o[i]+'('+b+o[j]+c+')'+o[k]+d)
						exit()
					if eval(a+o[i]+b+o[j]+'('+c+o[k]+d+')')==rslt:
						print(a+o[i]+b+o[j]+'('+c+o[k]+d+')')
						exit()
					if eval('('+a+o[i]+b+')'+o[j]+'('+c+o[k]+d+')')==rslt:
						print('('+a+o[i]+b+')'+o[j]+'('+c+o[k]+d+')')
						exit()
					if eval('('+a+o[i]+b+o[j]+c+')'+o[k]+d)==rslt:
						print('('+a+o[i]+b+o[j]+c+')'+o[k]+d)
						exit()
					if eval(a+o[i]+'('+b+o[j]+c+o[k]+d+')')==rslt:
						print(a+o[i]+'('+b+o[j]+c+o[k]+d+')')
						exit()
				except:
					pass
	ab,bc,cd=str(n[0])+str(n[1])+'.0',str(n[1])+str(n[2])+'.0',str(n[2])+str(n[3])+'.0'
	for i in range(4):
		for j in range(4):
			try:
				if eval(ab+o[i]+c+o[j]+d)==rslt:
					print(ab+o[i]+c+o[j]+d)
					exit()
				if eval('('+ab+o[i]+c+')'+o[j]+d)==rslt:
					print('('+ab+o[i]+c+')'+o[j]+d)
					exit()
				if eval(ab+o[i]+'('+c+o[j]+d+')')==rslt:
					print(ab+o[i]+'('+c+o[j]+d+')')
					exit()
				if eval(a+o[i]+bc+o[j]+d)==rslt:
					print(a+o[i]+bc+o[j]+d)
					exit()
				if eval('('+a+o[i]+bc+')'+o[j]+d)==rslt:
					print('('+a+o[i]+bc+')'+o[j]+d)
					exit()
				if eval(a+o[i]+'('+bc+o[j]+d+')')==rslt:
					print(a+o[i]+'('+bc+o[j]+d+')')
					exit()
				if eval(a+o[i]+b+o[j]+cd)==rslt:
					print(a+o[i]+b+o[j]+cd)
					exit()
				if eval('('+a+o[i]+b+')'+o[j]+cd)==rslt:
					print('('+a+o[i]+b+')'+o[j]+cd)
					exit()
				if eval(a+o[i]+'('+b+o[j]+cd+')')==rslt:
					print(a+o[i]+'('+b+o[j]+cd+')')
					exit()
			except:
				pass
	abc,bcd=str(n[0])+str(n[1])+str(n[2])+'.0',str(n[1])+str(n[2])+str(n[3])+'.0'
	for i in range(4):
		try:
			if eval(abc+o[i]+d)==rslt:
				print(abc+o[i]+d)
				exit()
			if eval(a+o[i]+bcd)==rslt:
				print(a+o[i]+dcd)
				exit()
		except:
			pass
	abcd=str(n[0])+str(n[1])+str(n[2])+str(n[3])+'.0'
	if eval(abcd)==rslt:
		print(abcd)
		exit()
				

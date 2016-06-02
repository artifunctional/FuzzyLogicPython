angle = 0.5
distance = 0.999
speed = 0.999

angle_mf = {'LOW': (0,0,0.5),'MEDIUM':(0,0.5,1),'HIGH':(0.5,1,1)}
distance_mf = {'LOW': (0,0,0.5),'MEDIUM':(0,0.5,1),'HIGH':(0.5,1,1)}
current_speed_mf = {'LOW': (0,0,0.5),'MEDIUM':(0,0.5,1),'HIGH':(0.5,1,1)}

membership_functions = [(angle_mf,angle),(distance_mf,distance),(current_speed_mf,speed)]
rulebase = [
	[0,'HIGH',0],
	[0,'MEDIUM',50],
	[0,'LOW',100]
]

def getMembership(linguistic_variable,member,x):
	a,b,c = linguistic_variable[member]
	if x<=a or x>=c:
		return 0.0
	elif a<=x<=b:
		return (x-a)/(b-a)
	else: #b<=x<=c
		return (c-x)/(c-b)

def infere(mfs,rules):
	sumx,sumfx = 0,0
	for i in rules:
		if len(i)>3:
			if i[2] == 'AND':
				value = min(
					getMembership(mfs[i[0]][0],i[1],mfs[i[0]][1]),
					getMembership(mfs[i[3]][0],i[4],mfs[i[3]][1])
					)
			elif i[2] == 'OR':
				value = max(
					getMembership(mfs[i[0]][0],i[1],mfs[i[0]][1]),
					getMembership(mfs[i[3]][0],i[4],mfs[i[3]][1])
					)
		else:
			value = getMembership(mfs[i[0]][0],i[1],mfs[i[0]][1])

		sumx += value
		sumfx += value * i[len(i)-1]
	return sumfx / sumx

print infere(membership_functions,rulebase)


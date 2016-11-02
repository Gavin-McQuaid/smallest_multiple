i = 2520
divisble_by_all = False
while  not divisble_by_all:
	j = 11
	lel = 0
	while j <= 20:
		if i % j == 0:
			 lel += 1
			 j += 1

		else:
			break

	if lel == 10:
		divisble_by_all = True
		print i 
	i += 10
	

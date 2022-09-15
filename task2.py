import random

randomlist = []
randomlist2 = []

while True:
	randomlist.append(random.randint(1,50))
	randomlist2.append(random.randint(1,50))
	if (len(randomlist) and len(randomlist2)) == 10:
		break
randomlist3 = randomlist + randomlist2

x = set(randomlist3)
print(x)
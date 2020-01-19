from itertools import combinations	

count = 0
for i in combinations(range(1,7), 0):
	count += 1
print("0 form 6 : {}".format(count))

count = 0
for i in combinations(range(1,7), 1):
	count += 1
print("1 form 6 : {}".format(count))

count = 0
for i in combinations(range(1,7), 2):
	count += 1
print("2 form 6 : {}".format(count))

count = 0
for i in combinations(range(1,7), 3):
	count += 1
print("3 form 6 : {}".format(count))

count = 0
for i in combinations(range(1,7), 4):
	count += 1
print("4 form 6 : {}".format(count))

count = 0
for i in combinations(range(1,7), 5):
	count += 1
print("5 form 6 : {}".format(count))

count = 0
for i in combinations(range(1,7), 6):
	count += 1
print("6 form 6 : {}".format(count))

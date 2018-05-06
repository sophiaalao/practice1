
num = 10

flag = True

while True:

	for i in range(1, 20):
		if(num % i != 0):
			flag = False

	if flag:
		break
	else:
		num += 1
		flag = True


print(num)

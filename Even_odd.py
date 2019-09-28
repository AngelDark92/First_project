i=0
while i!=2:
	i=0
	num=int(input("Input a number to check if even or odd: "))
	check=int(input("Input another number: "))
	if num%4==0:
		print(f"the number {num} is a multiple of 4")
	else:
		print(f"the number {num} is no multiple of 4")
	if num%2==0:
		print(f"the number {num} is even")
	else:
		print(f"the number {num} is odd")
	if num%check==0:
		print(f"{num} and {check} divide evenly into each other")
		while i==0:
			loppo=input("continue yes or no? ")
			if loppo=="yes":
				i=1
				continue
			elif loppo=="no":
				i=2
				break
			else:
				print("your reply is not valid, re enter")
				continue	
	else:
		print(f"{num} and {check} do not divide evenly into each other")
		while i==0:
			loppo=input("continue yes or no? ")
			if loppo=="yes":
				i=1
				continue
			elif loppo=="no":
				i=2
				break
			else:
				print("your reply is not valid, re enter")
				continue

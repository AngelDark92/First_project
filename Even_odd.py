while 1>0:
	num=int(input("Input a number to check if even or odd: "))
	check=int(input("Input another number: "))
	if num%4==0:
		print("the number", num," is a multiple of 4")
	else:
		print("the number", num," is no multiple of 4")
	if num%2==0:
		print("the number", num," is even")
	else:
		print("the number", num," is odd and no multiple of 4")
		loppo=input("continue yes or no? ")
		if loppo=="no":
			break
	if num%check==0:
		print(num, " and ",check, " divide evenly into each other")
		loppo=input("continue yes or no? ")
		if loppo=="no":
			break
	else:
		print(num, " and ",check," do not divide evenly into each other")
		loppo=input("continue yes or no? ")
		if loppo=="no":
			break
	
n = int(input("enter a value:"))
for fizz in range(n):
	if fizz % 15 == 0:
		print("Fizz")										
		continue
	elif fizz % 3 == 0:	
		print("buzz")										
		continue
	elif fizz % 5 == 0:		
		print("fizz,Buzz")									
		continue
	print(fizz)

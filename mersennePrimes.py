#mersennePrimes
#n=int(input("Enter the starting number"))
for i in range(2,110):
	a=(2**i)-1
	prime=True
	b=int(2**((i+1)/2))
	for j in range(3,b,2):
		if (a%j==0):
			prime=False
			print('',i," is not a prime. Divisible by ",j)
			break;
	if prime==True:
		print("2^",i,"-1 is a prime")

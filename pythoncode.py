Primes = input(“maximum prime value”)
Prime = int(primes)
Primelist = []
For x in range (2, 1000):
	Prime = true
	For y in range (2, x):
		If (x % y == 0):
			Prime = false
	If prime:
		Primelist.append(x)
Print (primelist)
X = sum(primelist)
Print (x)

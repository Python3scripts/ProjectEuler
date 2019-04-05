#! /usr/bin/python3

def is_prime(n):
	for i in range(2, n):
		if(n%i==0):
			return False
	return True

n = 600851475143
i = 1
while n>1:
	i+=1
	while(is_prime(i) and n%i==0):
		n/=i
print(i)
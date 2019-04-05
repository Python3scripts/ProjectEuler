#! /usr/bin/python3

i, j, k, s = 1, 2, 0, 2
while(k<4_000_000):
	k=i+j
	if(k%2==0):
		s+=k
	i, j = j, k
print(s)
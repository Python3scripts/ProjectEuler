#! /usr/bin/python3

i = 1
j = 2
k = 0
s = 2 # s starts with 2 because our loop starts from 3, and k=2 is should also be added.
while(k<4_000_000):
	k = i+j
	if(k%2==0):
		s+=k
	i = j
	j = k
print(s)
#!/usr/bin/python          
# -*- coding: utf-8 -*- 
import string
import time
import math

def isPrime(n):
	count = 2
	while count <= math.floor(math.sqrt(n)):    
		if n % count is 0:
			return False
			break
		count = count + 1
	return True

if __name__=='__main__':
	i = 2
	starttime = time.clock()
	while i > 1:     
		if(isPrime(i)):
			print i 
			endtime = time.clock() 
			print 'Totally spend' + str((endtime - starttime)) + 'seconds'   
			i = i + 1  
		else:               
			i = i + 1	  

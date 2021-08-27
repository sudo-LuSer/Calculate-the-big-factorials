NMAX=10**5
factorial=[1]
def plein_the_factorial():
	for i in range(1,NMAX+1):
		factorial.append(factorial[i-1]*i)
def title():
	print ("-"*(1.5)*10**2)
	print("\t\t\t\t\t\t\t"+"welcome to my factorial program using dynamic programming you can calculate n! for all 0<=n<10^5 Enjoy")
	print ("-"*(1.5)*10**2)
plein_the_factorial()
title()
def run():
	try:
		print("ENTER A POSITIVE INTGER N:")
		N=int(input())
		print("THE N! = ")
		print(factorial[N])
	except ValueError:
		print("ENTER A NUMBER PLEASE !")
	run()
run()
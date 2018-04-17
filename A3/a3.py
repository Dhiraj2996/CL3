
#save lenght of both binary numbers(x and y)
#A=M,append 9 zeros
#S=-M,append 9zeros
#P=x zeroes,Q,append 0


def add(x,y):
	z=[0]*17
	i=16
	c=0
	while i>=0:
		temp=x[i]+y[i]+c
		z[i]=temp%2
		c=temp/2
		i=i-1
	return z



def dec_to_bin(num):
	ans=[0]*8
	i=7
	while num and i>=0:
		ans[i]=num%2
		#print ans[i]," ",num," ",i
		num=num/2
		i=i-1
	return ans

def rightshift(x):
	i=16
	while i>0:
		x[i]=x[i-1]
		i-=1
	return x

def sub(x,y):
	z=[0]*16
	i=15
	c=0
	while i>=1:
		temp=x[i]-y[i]-c
		z[i]=temp%2
		c=abs(temp/2)
		i=i-1
	return z

def bin_to_dec(x):
	if x[0]==1:
		one = [0]*15 + [1]
		x=sub(x,one)
		for i in range(len(x)):
			x[i]=1-x[i] #invert

	print "X-inv",x,len(x)
	
	i=15
	p=0
	ans=0
	while i>=1:
		if x[i]==1:
			ans=ans+2**p
		p=p+1
		i=i-1
	if x[0]:
		return -ans
	return ans


def prod (num1,num2):
	#conv both numbers to binary (M and Q)
	M=dec_to_bin(num1)
	Q=dec_to_bin(num2)
	Minus_M=dec_to_bin(-num1)

	P=[0]*8
	P.extend(Q)
	P.append(0)
	print "Original P value:",P

	M+=[0]*9
	Minus_M+=[0]*9
	print len(M)," ",len(Minus_M)

	#check last two LSB of P
	#01 --> P+M,10 --> P-M 
	for i in range(8) :
		if P[-2]==0 and P[-1]==1:
			P=add(P,M)
			print "P+M::",P
		elif P[-2]==1 and P[-1]==0:
			P=add(P,Minus_M)
			print "P-M::",P
		p=rightshift(P)
	print p	
	return bin_to_dec(P)




#get two integers from user
#num1=int(raw_input("Enter the num1::"))
#num2=int(raw_input("Enter the num2::"))
#print "Two numbers are ::",num1 ," ", num2
#print "Product is::",prod(num1,num2)

#print "Check binary function::\n",dec_to_bin(-12)
#res=prod(num1,num2)
#print "Product is::",res

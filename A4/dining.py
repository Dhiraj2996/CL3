import threading
import random
import time
from pymongo import MongoClient


class Philosopher(threading.Thread):
	running=True
	connection=MongoClient("127.0.0.1",27017)
	printcounter=0
	def __init__(self,index,name,forkonleft,forkonright):
		threading.Thread.__init__(self)
		self.index=index
		self.name=name
		self.forkonleft=forkonleft
		self.forkonright=forkonright
	def run(self):
		while self.running:
			#Philosopher is thinking
			time.sleep(random.uniform(3,13))
			print self.name," is Hungry."
			self.dine()
	def dine(self):
		fork1=self.forkonleft
		fork2=self.forkonright
		while self.running:
			fork1.acquire(True)
			lockt=fork2.acquire(False)
			if lockt: break
			fork1.release()
			print self.name," swaps forks left and right."
			fork1,fork2=fork2,fork1
		else:
			return
		self.dining()
		fork1.release()
		fork2.release()
	def dining(self):
		print self.name," starts eating!"
		self.readfromMongo()
		time.sleep(random.uniform(1,10))
		print self.name," finishes eating and leaves to think."
	def readfromMongo(self):
		db=Philosopher.connection.test.dining
		limit=self.printcounter
		cursor=db.find({"ph_no":self.index})[limit:limit+1]
		print cursor[0]
		self.printcounter+=1
		if self.printcounter==2:
			self.running=False


def Dining_Philosophers():
	forks=[threading.Lock() for i in range(5)]
	names=['A','B','C','D','E']
	philosophers=[Philosopher(i,names[i],forks[i%5],forks[(i+1)%5]) for i in range(5)]
	for p in philosophers:
		p.start()
	time.sleep(50)
	Philosopher.running=False
	print "Now we are Finishing"

Dining_Philosophers()

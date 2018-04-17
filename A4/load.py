from pymongo import MongoClient
from datetime import datetime

connection=MongoClient("127.0.0.1",27017)
db=connection.test.dining

fd=open("data.txt","r").read().strip().split("\n")

for line in fd:
	record=line.strip().split(",")
	
	record=[int(i) for i in record]
	#print record
	post={"ph_no":record[0],"temp":record[1],"time":str(datetime.now())}
	print post
	db.insert_one(post)

# Python code to Insert RFID data into MongoDB 
from pymongo import MongoClient 

try: 
	conn = MongoClient() 
	print("Connected successfully!!!") 
except: 
	print("Could not connect to MongoDB") 

# database 
db = conn.StudentLog 

# Created or Switched to collection names: RFID_Data
collection = db.RFID_Data 

RFID_Data = { 
		"id":"150040588"
		} 

# Insert Data   
rec_id1 = collection.insert_one(RFID_Data) 

print(rec_id1," ") 

# Printing the data inserted 
cursor = collection.find() 
for record in cursor: 
	print(record) 
#mongoexport --db StudentLog --collection RFID_key --out RFID_data_log.json

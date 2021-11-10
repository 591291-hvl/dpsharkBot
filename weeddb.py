from replit import db
import random

def add_respons(response):
	number = db["nrWeedRespons"]
	keys = db.keys()
	if number in keys:
		print("Name already exists")
	else:
		print("add " + str(number))
		db[number] = response[5:]
		number += 1
		db["nrWeedRespons"] = number

def remove_respons(remove):
	numberRemove = remove[8:]
	number = db["nrWeedRespons"]
	keys = db.keys()
	if number in keys:
		print("Cant remove")
	else:
		number -= 1
		db[numberRemove] = db[str(number)]
		del db[str(number)]
		db["nrWeedRespons"] = number
	

def print_respons():
	nrWeed = db["nrWeedRespons"]
	if nrWeed == 0:
		print("No respones")
	else:
		rndVal = random.randint(0, nrWeed-1)
		respons = db[str(rndVal)]
		return respons
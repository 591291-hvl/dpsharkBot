from replit import db
import random


def add_respons(response):
	number = db["nrWeedRespons"]
	keys = db.keys()
	if number in keys:
		return "Bad shit happend, contact bot maker"
	else:
		print("add " + str(number))
		db[number] = response
		number += 1
		db["nrWeedRespons"] = number
		return "\"" + response + "\" is added as " + str(number-1)

def remove_respons(remove):
	numberRemove = remove
	number = db["nrWeedRespons"]
	if int(number) <= int(numberRemove):
		return "Invalid index"
	else:
		number -= 1
		db[numberRemove] = db[str(number)]
		removedStr = db[str(number)]
		del db[str(number)]
		db["nrWeedRespons"] = number
		return "Removed \"" + removedStr + "\""


def print_respons():
	nrWeed = db["nrWeedRespons"]
	if nrWeed == 0:
		print("No respones")
	else:
		rndVal = random.randint(0, nrWeed-1)
		respons = db[str(rndVal)]
		return respons
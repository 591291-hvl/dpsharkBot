import random
import json
import numpy as np


# def add_respons(response):
# 	number = db["nrWeedRespons"]
# 	keys = db.keys()
# 	if number in keys:
# 		return "Bad shit happend, contact bot maker"
# 	else:
# 		print("add " + str(number))
# 		db[number] = response
# 		number += 1
# 		db["nrWeedRespons"] = number
# 		return "\"" + response + "\" is added as " + str(number-1)

# def remove_respons(remove):
# 	numberRemove = remove
# 	number = db["nrWeedRespons"]
# 	if int(number) <= int(numberRemove):
# 		return "Invalid index"
# 	else:
# 		number -= 1
# 		db[numberRemove] = db[str(number)]
# 		removedStr = db[str(number)]
# 		del db[str(number)]
# 		db["nrWeedRespons"] = number
# 		return "Removed \"" + removedStr + "\""


def print_respons():
	with open("db.json", "r") as json_file:
		data = np.array(json.load(json_file)['weed'])

	rndVal = random.randint(0, (data.size-1))
	respons = data[rndVal]
	return respons
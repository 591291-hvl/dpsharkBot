from replit import db
import random

def add_respons(number, response):
  keys = db.keys()
  if number in keys:
    print("Name already exists")
  else:
    print("add " + str(number))
    db[number] = response
    number += 1
    db["nrWeedRespons"] = number

def print_respons():
  nrWeed = db["nrWeedRespons"]
  if nrWeed == 0:
    print("No respones")
  else:
    rndVal = random.randint(0, nrWeed-1)
    respons = db[str(rndVal)]
    return respons
from replit import db
import discord
import os

import weeddb

#Should always be commented out
#db["nrWeedRespons"] = 0
nrWeed = db["nrWeedRespons"]
print(str(nrWeed) + " nr of responses")

print("test " + str(db["0"]))

keys = db.keys()
for x in keys:
    print(x + " " + str(db[x]))

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!add"):
        weeddb.add_respons(nrWeed, message.content[5:])
        value = db["nrWeedRespons"]
        print(value)

    elif "!all" in message.content:
        keys = db.keys()
        strOut = ""
        for x in keys:
            if (x.isdigit()):
                print(x)
                strOut += (x + " " + str(db[x]) + "\n")
        await message.channel.send(strOut)

    elif "weed" in message.content:
        await message.channel.send(weeddb.print_respons())

    else:
        print("Nothing")


#Functions, to be added to another class

client.run(os.environ['TOKEN'])

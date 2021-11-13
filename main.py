from replit import db
import discord
import os
import art

import weeddb
#import countInfo

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

#Text responses
@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith("!add"):
		weeddb.add_respons(message.content)
		
	elif "!all" in message.content:
		#add to method
		keys = db.keys()
		strOut = ""
		for x in keys:
			if (x.isdigit()):
				print(x)
				strOut += (x + " " + str(db[x]) + "\n")
		await message.channel.send(strOut)
	

	elif message.content.startswith("!remove"):
		weeddb.remove_respons(message.content)
	

	elif "weed" in message.content:
		await message.channel.send(weeddb.print_respons())

	elif "!count" in message.content:
		counter = 0

		text_channel_list = []
		for guild in client.guilds:
			for channel in guild.text_channels:
				text_channel_list.append(channel)

		userID = message.author.id
		for txtChannel in text_channel_list:
			async for msg in txtChannel.history(limit=10000):
				if msg.author.id == userID:
					counter += 1
		
		await message.reply(counter, mention_author=True)
	
	elif "!art" in message.content:
		await message.channel.send("```\n" + art.text2art(message.content[5:]) + "\n```")

	else:
		print("Nothing")


#Functions, to be added to another class

client.run(os.environ['TOKEN'])

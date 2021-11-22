from replit import db
import discord
intents = discord.Intents(messages=True, guilds=True, members=True)
import os
import art

import weeddb
import countInfo

#Should always be commented out
#db["nrWeedRespons"] = 0
#nrWeed = db["nrWeedRespons"]
#print(str(nrWeed) + " nr of responses")

#print("test " + str(db["0"]))

#keys = db.keys()
#for x in keys:
#    print(x + " " + str(db[x]))

client = discord.Client(intents=intents)




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
	
	elif "!counttxt" in message.content:
		await message.channel.send("```\n" + await countInfo.get_txt(client, message) + "\n```")

	elif "!countimg" in message.content:
		await message.channel.send(file=await countInfo.get_img(client, message))

	elif "!count" in message.content:
		await message.reply(await countInfo.get_count(message.content[7:],client, message), mention_author=True)
	
	elif "!art" in message.content:
		await message.channel.send("```\n" + art.text2art(message.content[5:]) + "\n```")

	elif "!github" in message.content:
		await message.channel.send("https://github.com/591291-hvl/dpsharkBot")

	elif message.content.lower().startswith("jeg er"):
		await message.channel.send("Hei " + message.content[7:] + ", jeg er dpsharkBot")

	elif "this is fine" in message.content.lower():
		await message.channel.send(file=discord.File('other/thisisfine.jpg'))

	elif "!ping" in message.content.lower():
		await message.channel.send(file=discord.File('other/blobping.gif'))

	elif (client.user.mentioned_in(message) or "<@" in message.content):
		await message.add_reaction("<:blobping:910561946443604018>")
		#await message.add_reaction("<:angryping:910511211928518746>")

	#"main" function of bot
	elif "weed" in message.content.lower():
		await message.channel.send(weeddb.print_respons())

	else:
		print("Nothing")


#Functions, to be added to another class

client.run(os.environ['TOKEN'])

from replit import db
import discord
intents = discord.Intents(messages=True, guilds=True, members=True)
import os
import art
from random import randint


from keepAlive import keepAlive
import weeddb
import countInfo
import webhook

#import manualAdd



#Should always be commented out
#manualAdd.remove_all()
#manualAdd.add_all()
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
	
	if message.content.startswith("!add") and message.author.id == 223112835671130112:
		async with message.channel.typing():
			await message.channel.send(weeddb.add_respons(message.content[5:]))
		

	elif message.content.startswith("!remove") and message.author.id == 223112835671130112:
		async with message.channel.typing():
			await message.channel.send(weeddb.remove_respons(message.content[8:]))
		
	elif "!all" in message.content:
		async with message.channel.typing():
			#add to method
			numberOfKeys = db["nrWeedRespons"]
			strOut = ""
			for x in range(numberOfKeys):
				print(str(x))
				strOut += (str(x) + " " + str(db[str(x)]) + "\n")
			await message.channel.send("```\n" + strOut + "\n```")
	
	elif message.content.startswith("!help"):
		async with message.channel.typing():
			await message.channel.send(file=discord.File("readme.md"))

	#webhooks
	elif message.content.startswith("!send"):
		async with message.channel.typing():
			await webhook.sendMsg(message, client)
	
	
	elif "!counttxt" in message.content:
		async with message.channel.typing():
			await message.channel.send("```\n" + await countInfo.get_txt(client, message) + "\n```")

	elif "!countimg" in message.content:
		async with message.channel.typing():
			await message.channel.send(file=await countInfo.get_img(client, message))

	elif "!count" in message.content:
		async with message.channel.typing():
			await message.reply(await countInfo.get_count(message.content[7:],client, message), mention_author=True)
	
	elif "!art" in message.content:
		async with message.channel.typing():
			await message.channel.send("```\n" + art.text2art(message.content[5:]) + "\n```")

	elif "!github" in message.content:
		async with message.channel.typing():
			await message.channel.send("https://github.com/591291-hvl/dpsharkBot")

	elif message.content.lower().startswith("jeg er"):
		async with message.channel.typing():
			await message.channel.send("Hei " + message.content[7:] + ", jeg er dpsharkBot")

	elif "!sleep" in message.content.lower():
		async with message.channel.typing():
			value = randint(0, 1)
			if value == 0:
				await message.channel.send(file=discord.File('other/sleep.jpg'))
			else:
				await message.channel.send(file=discord.File('other/sleep1.jpg'))
		

	elif "this is fine" in message.content.lower():
		async with message.channel.typing():
			await message.channel.send(file=discord.File('other/thisisfine.jpg'))

	elif "!ping" in message.content.lower():
		async with message.channel.typing():
			await message.channel.send(file=discord.File('other/blobping.gif'))

	elif (client.user.mentioned_in(message) or "<@" in message.content):
		async with message.channel.typing():
			await message.add_reaction("<:blobping:917804967350399059>")
			#await message.add_reaction("<:angryping:910511211928518746>")

	elif "pog" in message.content.lower():
		async with message.channel.typing():
			await message.add_reaction("<:pog:917817711982182570")

	elif "cock" in message.content.lower():
		async with message.channel.typing():
			await message.reply(file=discord.File('other/YEP.png'))
	
	elif message.content.startswith("!thonk"):
		async with message.channel.typing():
			await message.reply(file=discord.File('other/ThonkSpin.gif'))

	elif message.content.startswith("!d"):
		async with message.channel.typing():
			number = message.content[2:]
			value = randint(1,int(number))
			await message.reply("Rolled d" + str(number) + ": " + str(value))

	#"main" function of bot
	elif "weed" in message.content.lower():
		async with message.channel.typing():
			await message.channel.send(weeddb.print_respons())

	else:
		print("Nothing")


#Functions, to be added to another class


keepAlive()
client.run(os.environ['TOKEN'])

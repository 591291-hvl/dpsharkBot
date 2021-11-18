import matplotlib.pyplot as plt
import discord

async def get_count(user, client, message):
	counter = 0

	text_channel_list = []
	server = message.guild.id
	for guild in client.guilds:
		if guild.id == server:
			for channel in guild.text_channels:
				if str(channel.type) == 'text':
					text_channel_list.append(channel)
	
	userID = 0
	if not user:
		userID = message.author.id
	else:
		user = user.replace("<","")
		user = user.replace(">","")
		user = user.replace("@","")
		user = user.replace("!","")
		user = user.replace(" ","")
		userID = user
	
	for txtChannel in text_channel_list:
		async for msg in txtChannel.history(limit=10000):
			if msg.author.id == int(userID):
				counter += 1
	return counter

async def get_max(client, message):

	#get all text channels in server
	text_channel_list = []
	server = message.guild.id
	for guild in client.guilds:
		if guild.id == server:
			for channel in guild.text_channels:
				if str(channel.type) == 'text':
					text_channel_list.append(channel)
	
	#get all members in server
	member_list = []
	for guild in client.guilds:
		if guild.id == server:
			for member in guild.members:
				member_list.append(member)
	#list for counting
	member_counter = []
	for x in member_list:
		member_counter.append(0)
	#count through messages
	for txtChannel in text_channel_list:
		async for msg in txtChannel.history(limit=10000):
			for i in range(len(member_list)):
				if msg.author.id == member_list[i].id:
					member_counter[i] += 1
	
	#sort
	#member_counter, member_list = (list(t) for t in zip(*sorted(zip(member_counter, member_list),reverse=True)))

	for i in member_list:
		print(i)

	zipped_pairs = zip(member_counter, member_list)
 
	member_list = [x for _, x in sorted(zipped_pairs, reverse=True)]
	member_counter = sorted(member_counter, reverse=True)
	for i in member_list:
		print(i)

	#text version, todo: splitt into 2 methods
	outStr = ""
	for i in range(len(member_counter)):
		outStr += str(member_list[i]) + ": " + str(member_counter[i]) + "\n"
	#return outStr	

	#image version
	plt.pie(member_counter, labels=member_list, autopct='%1.1f%%', startangle=140)
	
	filename =  "image.png"
	plt.savefig(filename)
	image = discord.File(filename)

	return image
	
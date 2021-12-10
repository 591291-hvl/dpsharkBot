import matplotlib.pyplot as plt
import pandas as pd
import discord

#todo
#I really really need to reduce number of lines by reusing methods


#returns table of users and number of messages sendt
async def get_table(client, message):
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
	
	for i in range(len(member_list)):
		member_list[i] = str(member_list[i])
	
	#sort
	index = list(range(len(member_counter)))

	index.sort(key = member_counter.__getitem__,reverse=True)

	member_counter[:] = [member_counter[i] for i in index]
	member_list[:] = [member_list[i] for i in index]

	
	return member_list, member_counter



#returns string of users: number of messages
async def get_txt(client, message):
	member_list, member_counter = await get_table(client, message)

	#text version, todo: splitt into 2 methods
	outStr = ""
	for i in range(len(member_counter)):
		outStr += str(member_list[i]) + ": " + str(member_counter[i]) + "\n"
	return outStr	

#returns piechart of users: %of messages
async def get_img(client, message):

	member_list, member_counter = await get_table(client, message)

	df = pd.DataFrame(data = {'Users':member_list , '% Messages' :member_counter})

	#new version
	
	#% cut off point for pie chart
	cutOffPoint = 3
	#max nr of messages
	maxMessages = df['% Messages'].sum()
	for i in range(len(member_counter)):
		if (member_counter[i]/maxMessages) < (cutOffPoint/100):
			cutOffPoint = i
			break
	
	#top users
	df2 = df[:cutOffPoint].copy()

	#others
	new_row = pd.DataFrame(data = {'Users' : ['others'],'% Messages' : [df['% Messages'][cutOffPoint:].sum()]})

	#combining top users with others
	df2 = pd.concat([df2, new_row])
	plt.pie(df2['% Messages'],labels=df2['Users'],autopct='%1.1f%%')


	###########


	filename =  "other/image.png"
	plt.savefig(filename)
	image = discord.File(filename)
	plt.clf()

	return image

#Returns number of messages sendt, @user optional
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
	return "Number of messages: " + str(counter)

#Returns number of words sendt, @user optional
async def get_wordCount(user, client, message):
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
				wordsInMessage = " ".join(msg.content.split()).split(" ")
				counter += len(wordsInMessage)
	return "Number of words: " + str(counter)
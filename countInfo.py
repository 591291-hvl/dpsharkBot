

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

	text_channel_list = []
	server = message.guild.id
	for guild in client.guilds:
		if guild.id == server:
			for channel in guild.text_channels:
				if str(channel.type) == 'text':
					text_channel_list.append(channel)
	
	
	member_list = []

	for guild in client.guilds:
		if guild.id == server:
			for member in guild.members:
				member_list.append(member)

	member_counter = []
	for x in member_list:
		member_counter.append(0)

	for txtChannel in text_channel_list:
		async for msg in txtChannel.history(limit=10000):
			for i in range(len(member_list)):
				if msg.author.id == member_list[i].id:
					member_counter[i] += 1
	
	outStr = ""
	for i in range(len(member_counter)):
		outStr += str(member_list[i]) + ": " + str(member_counter[i]) + "\n"


	return outStr	
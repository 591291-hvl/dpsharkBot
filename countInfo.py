

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



	
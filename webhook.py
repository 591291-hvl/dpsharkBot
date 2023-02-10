
#!send @user words to be sendt as user
async def sendMsg(message, client):
	txt = message.content.split()
	user = " ".join(txt[1:2])
	print(user)
	user = user.replace("<","")
	user = user.replace(">","")
	user = user.replace("@","")
	user = user.replace("!","")
	newMember = client.get_user(int(user))
	print(newMember)
	listToStr = " ".join(txt[2:])
	
	webhook = await message.channel.create_webhook(name=newMember.name)
	#await webhook.send(listToStr, username=newMember.name,avatar_url=newMember.avatar_url)
	await webhook.send(listToStr, username=newMember.name,avatar_url=newMember.avatar)
	webhooks = await message.channel.webhooks()
	for webhook in webhooks:
		await webhook.delete()
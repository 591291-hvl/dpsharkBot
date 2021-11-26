

async def sendMsg(message):

	member = message.author
	webhook = await message.channel.create_webhook(name=member.name)
	await webhook.send(
			str(message), username=member.name, avatar_url=member.avatar_url)
	webhooks = await message.channel.webhooks()
	for webhook in webhooks:
		await webhook.delete()
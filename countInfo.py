

def get_count(client, message):
	userID = message.author.id
	channel = client.get_channel(channel_id)
	messages = channel.history(limit=200)
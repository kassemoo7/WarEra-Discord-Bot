import discord


async def send_message(client, channel_id, message):
    channel = client.get_channel(channel_id)

    if channel is None:
        print("Channel not found")
        return

    await channel.send(message)
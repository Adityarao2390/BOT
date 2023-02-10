import discord
#import os

#client = discord.Client()
client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('Hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('Who invented you'):
    await message.channel.send('Adi Bhaya')

  if message.content.startswith('Vegetable'):
    await message.channel.send('Apple:High, Onion:High, Patao:High')
  


client.run(
  #os.getenv('TOKEN'))
  'MTA3MzU5MjgwMDU0NjkzMDgyMA.GbPx1T.b-2LEYaAch6oqkLxfYEI1MfkDdHaXVZdSUy5ug')
  #'MTA3MzI2NzYyMDk5ODA0MTY0MQ.GqjzAU.9ogjXkHBH_kJV2HhmjarZgT9m-3X5lsCJ9eXA8')

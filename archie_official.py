import discord
import os
import asyncio
import time
import site
# esconder el config.py
import sys
sys.path.insert(0, '/home/dietpi/discord')

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!ping'):
        msg = 'Pong haha'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!music'):
        msg = 'My recommendation for {0.author.mention}: https://www.youtube.com/watch?v=hLTgQ5SC-PU'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!lal'):
        msg = 'Are you jaking?'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!lel'):
        msg = 'Are you jeking?'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!lil'):
        msg = 'Are you jiking?'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!lol'):
        msg = 'Are you joking?'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!lul'):
        msg = 'Are you juking?'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!joke'):
        msg = 'Why can\'t cats work with a computer? Because they get too distracted chasing the mouse around, haha!'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!update'):
        msg = 'Wait a few seconds...'.format(message)
        await client.send_message(message.channel, msg)
        msg = 'Updating Archie'.format(message)
        await client.send_message(message.channel, msg)
        msg = 'Archie is now offline!'.format(message)
        await client.send_message(message.channel, msg)
        os.system("python3 ~/discord/update.py")
        time.sleep(5)
        exit()

    if message.content.startswith('!areureal'):
        msg = 'I am completely real! I have feelings and emotions like you, of course!'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!howru'):
        msg = 'I\'m fine! Thanks for asking.'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!whereru'):
        msg = 'I\'m wherever you are, ready to help you.'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!letswork'):
        msg = 'Time to work! {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!whoru'):
        msg = 'Did not introduced myself yet? My apologies, I\'m Archie, the official CAD assistant created by us. Nice to meet you {0.author.mention}! You can see the list of commands that you can use by typing !help'.format(message)
        await client.send_message(message.channel, msg)

  #  if message.content.startswith('!add'):
  #      async def add(ctx, a: int, b: int):
  #      await client.send(a+b)


    #Leave !help always the last one. Please update any changes.
    if message.content.startswith('!help'):
        msg = 'Hi there! This are the commands you can use with me so far:\n !help \n !hello \n !ping \n !lal \n !lel \n !lil \n !lol \n !lul \n !joke \n !areureal \n !howru \n !whereru \n !letswork \n !whoru \n !update (to update any changes)'.format(message)
        await client.send_message(message.channel, msg)
        
@client.command(pass_context=True, aliases=['user'])
async def info(ctx, user: discord.Member):
    try:
        await client.say("`The user's name is: {}`".format(user.name))
        await client.say("`The user's ID is: {}`".format(user.id))
        await client.say("`The user's status is: {}`".format(user.status))
        await client.say("`The user's highest role is: {}`".format(user.top_role))
        await client.say("`The user joined at: {}`".format(user.joined_at))        
        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.send_message(discord.Object(id='458378197478932492'), 'Archie is now online!')
    await client.change_presence(game=discord.Game(name="CAD Developers | !help"))


if __name__ == '__main__':
    import config
    client.run(config.token)
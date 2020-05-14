  
# Python Libraries
import re
import asyncio

# Third Party Libraries
import discord
token = "token"
client = discord.Client()
players = []
sum = 0
time = 20

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name='Jamming with 27o'))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!tm'):
        if message.channel.id == 709149749025964043:
            await message.channel.send("Initiating...")
            players.clear()
            for guild in client.guilds:
                for member in guild.members:
                    x = member.id
                    x = str(x)
                    players.append(x)
            global sum
            t = len(players)
            L = 0 
            while L < t:
                id = players[L]
                L += 1
                tempVar = "!pw <@" + id + ">"
                await message.channel.send(tempVar)
            time = len(players)
            time = int(time)
            time = time*4
            await asyncio.sleep(time)
            id = message.author.id
            id = str(id)
            tempVar = "!<@" + id + ">"
            await message.channel.send("The total balance of all players is " + str(sum) + " chips!" + tempVar)
            sum = 0



@client.event
async def on_message_edit(before, after):
    if before.channel.id == 709149749025964043:            
        if len(after.embeds) != 0:
            if len(before.embeds) != 0: 
                expression = re.compile(r"wallet:[\s\*]*(?P<amount>\d+)[\s\*]chip")
                if expression.search(after.embeds[0].description):
                    match = expression.search(after.embeds[0].description)
                    chips = match.group('amount')
                    chips = int(chips)
                    global sum
                    sum = sum + chips


client.run(token)

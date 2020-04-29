  
# Python Libraries
import re
import asyncio

# Third Party Libraries
import discord
token = "Njk3ODcxNzExMjEwNTY5OTA5.Xo92UA.LQc4_EIVpF_ZUpgSjsMFLYvSA2s"
client = discord.Client()
players = ["613156357239078913"]
sum = 0


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name='losing money to Erika'))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!tm'):
        if message.channel.id == 698990499104555079:
            global sum
            t = len(players)
            L = 0 
            while L < t:
                id = players[L]
                L += 1
                tempVar = "!pw <@" + id + ">"
                await message.channel.send(tempVar)
            await asyncio.sleep(300)
            await message.channel.send("The total balance of all players is " + str(sum) + " chips!")
            sum = 0


@client.event
async def on_message_edit(before, after):
    if before.channel.id == 698990499104555079:            
        if len(after.embeds) != 0:
            if len(before.embeds) != 0: 
                expression = re.compile(r"wallet:[\s\*]*(?P<amount>\d+)[\s\*]chip")
                if expression.search(after.embeds[0].description):
                    match = expression.search(after.embeds[0].description)
                    chips = match.group('amount')
                    chips = int(chips)
                    global sum
                    sum = sum + chips
    
@client.event
async def on_raw_reaction_add(payload):
    #channel_id = payload.channel_id
    x = payload.message_id
    x = str(x)
    if x == 'REPLACE WITH MESSAGE ID':
        member = payload.member
        role = discord.utils.get(member.guild.roles, name = 'has ID')

        await member.add_roles(role)
        x = member.id
        x = str(x)
        players.append(x)

        print(x)




client.run(token)
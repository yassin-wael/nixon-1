import discord
import asyncio



client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="25/7"))

@client.event
async def on_message(message):
    if message.content.startswith("!test"):
        await client.send_message(message.channel, "Test erfolgreich")    

@client.event
async def on_member_join(member):
    print("recognised that a member called " + member.name + " joined")
    await client.send_message(member, "welcome to the server! we hope you will enjoy your stay :heart:")
    print("send message to " + member.name)
    
@client.event    
    
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
        
    if message.content.startswith('!join'):
        try:
            channel = message.author.voice.voice_channel
            await client.join_voice_channel(channel)
        except discord.errors.InvalidArgument:
            await client.send_message(message.channel, "Kein Voice channel gefunden.")
        except Exception as error:
            await client.send_message(message.channel, "Ein Error: ```{error}```".format(error=error))        

    if message.content.lower().startswith("!info"):
        info = discord.Embed(
            title="Hey, I'M Yassin w. :)",
            color=0xe74c3c,
            description="Hey this bot made for being online 27/7\n"
                        "the program : python 3.6.5 \n"
                        "dev : yassin w.#5343"
                        "\n"
                        "\n"
                        "Beta 0.1"

        )

        await client.send_message(message.channel, embed=info)     
        

client.run("NDY1MjgyMjk3NDc0NzExNTc0.DiLP7A.dpq8qvPczWGvchEZn_xrdAdOc1A")


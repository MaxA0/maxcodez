from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix="?")

@client.event
async def on_ready():
    print("ready")
    while True:
        print("cleared")
        await asyncio.sleep(10)
        with open("spam_detect.txt", "r+") as file:
            file.truncate(0)

@client.event
async def on_message(message):
    counter = 0
    with open("spam_detect.txt", "r+") as file:
        for lines in file:
            if lines.strip("\n") == str(message.author.id):
                counter+=1

        file.writelines(f"{str(message.author.id)}\n")
        if counter > 5:
            await message.guild.ban(message.author, reason="spam")
            await asyncio.sleep(1)
            await message.guild.unban(message.author)
            print("uh oh")

client.run("NzczOTY0NTI0NjQ5OTcxNzEy.X6Q4og.b13wEqs3JkaIwIefg2N5Zdcyl98")

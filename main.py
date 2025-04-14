import discord
from discord.ext import commands
from config import TOKEN
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            await attachment.save(f'./images/{file_name}')
            result = get_class("./keras_model.h5","./labels.txt",f'./images/{file_name}')
            if result[0]=="akıllı_ev\n":
                await ctx.send("Akıllı evler --> https://home-assistant.io")
            elif result[0]=="normal_ev\n":
                await ctx.send("Normal ev rsımlerı --> https://www.pexels.com/tr-tr/arama/ev%20i%C3%A7i/")
            else :
                await ctx.send("böyle bir ev türü yok")
    else:
        await ctx.send("you forgot the upload the image")
    
bot.run(TOKEN)

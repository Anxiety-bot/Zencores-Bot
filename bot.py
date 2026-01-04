import discord
from discord.ext import commands
import os

# Получаем токен из переменных окружения
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN') or os.getenv('DISCORD_TOKEN') or os.getenv('BOT_TOKEN')

# Создаем экземпляр бота
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

# Обрабатываем команду /hello
@bot.command()
async def hello(ctx):
    await ctx.send(f"Привет, {ctx.author.mention}!")

# Обрабатываем команду /start
@bot.command()
async def start(ctx):
    await ctx.send('Я на связи. Напиши мне что-нибудь )')

# Получение сообщений от юзера
@bot.event
async def on_message(message):
    if message.author.bot:
        await bot.process_commands(message)
        return
    
    if not message.content.startswith("/"):
        await message.channel.send('Вы написали: ' + message.content)
    
    await bot.process_commands(message)

# Запускаем бота
bot.run(BOT_TOKEN)

from discord.ext import commands
import discord

print("token?")
TOKEN = input()
I = 1
di = 1
prefix = "!"

bot = commands.Bot(prefix)
print("Bot is ready!")


@bot.command()
async def die(ctx):
  await ctx.send("So you have chosen death")
  print("Someone used the command [!die]")

bot.run(TOKEN)

from discord.ext import commands
import discord

I = 1
di = 1
prefix = "!"

bot = commands.Bot(prefix)
print("Bot is ready!")


@bot.command()
async def die(ctx):
  await ctx.send("So you have chosen death")
  print("Someone used the command [!die]")

bot.run("ODcwNzI1MjQxOTAxNTY4MDUw.YQQ8Eg.Vmhf6CztEfay9mGrQPKaoChFHrc")
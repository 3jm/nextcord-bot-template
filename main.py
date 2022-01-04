from nextcord.ext import commands
import os, urllib, requests, json, random

bot = commands.Bot(command_prefix='$')
bot.remove_command('help')

@bot.event
async def on_ready():
  print('Onine')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'`cogs.{extension}` was loaded.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'`cogs.{extension}` was unloaded. You can no longer use it until it is reloaded.')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('')

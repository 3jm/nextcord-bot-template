from nextcord.ext import commands
import os, urllib, requests, json, random

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
      await ctx.reply(f'{round(self.bot.latency * 1000)}')

def setup(bot):
    bot.add_cog(Ping(bot))

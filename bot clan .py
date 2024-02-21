import discord
from discord.ext import commands

bot_token = 'MTIwOTgwMDQxNTgwMjI5ODQxOA.Gmh84G.2a5epDZOCbVumKPzSsRbT9xYy3mlUOyhCp7c2w'
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_member_update(before, after):
    if before.roles != after.roles:
        role_name = [role.name for role in after.roles if role not in before.roles][0]
        if role_name == 'teste':
            channel = discord.utils.get(after.guild.channels, id=1209807928706465832)
            if channel:
                await channel.send(f'{after.mention} has been given the {role_name} role.')

bot.run(bot_token)
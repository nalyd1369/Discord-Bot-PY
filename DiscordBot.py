import os
import discord
import discord.utils
from itertools import cycle
from discord.utils import get
from discord.ext import commands
from discord.ext import commands, tasks
from discord.ext.commands import CheckFailure
from discord.ext.commands import has_permissions

client = commands.Bot(command_prefix = '.', case_insensitive=True, help_command=None)
status = cycle(['Racism (Comp)', 'Fuck Racists', 'Destroying the KKK', 'Being southern', 'Going to target'])

#bot ready and status
@client.event
async def on_ready():
    change_status.start()
    print('bot is ready')

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="Not racist")
    await member.add_roles(role)

#help
@client.command()
async def help(ctx):
    await ctx.send("```Report:\n.report @______ Racist, Karen, Capping hard, Impostor, Gay, Illiterate\n.sorry Racist, Karen, Capping hard, Impostor, Gay, Illiterate\n\nSpam:\n.spam Cringe, Cursed, Die, Hentai, Legs, Skeleton\n.joke\n\nModeration:\n.kick @______\n.ban @______\n.clear 5(enter amount of messages to be cleared, default is 5)\n.mute @______\n.unmute @______\n\nCog control:\n.load report, mod, spam, joke\n.reload report, mod, spam, joke\n.unload report, mod, spam, joke```", delete_after=120)

#cogs commands
@client.command()
@commands.has_permissions(manage_roles=True)
async def load(ctx, extension):
    message = ctx.message
    await message.delete(delay=120)
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded {extension}', delete_after=120)
@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"You don't have permission to use this command", delete_after=120)
    if hasattr(ctx.command, 'on_error'):
        await ctx.send("Cog not recognized", delete_after=120)

@client.command()
@commands.has_permissions(manage_roles=True)
async def reload(ctx, extension):
    message = ctx.message
    await message.delete(delay=120)
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Reloaded {extension}', delete_after=120)
@reload.error
async def reload_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"You don't have permission to use this command", delete_after=120)
    if hasattr(ctx.command, 'on_error'):
        await ctx.send("Cog not recognized", delete_after=120)

@client.command()
@commands.has_permissions(manage_roles=True)
async def unload(ctx, extension):
    message = ctx.message
    await message.delete(delay=120)
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded {extension}', delete_after=120)
@unload.error
async def unload_error(ctx, error): 
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"You don't have permission to use this command", delete_after=120)
    if hasattr(ctx.command, 'on_error'):
        await ctx.send("Cog not recognized", delete_after=120)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NzU3MDUyNDE1NTcxNzg3OTE5.X2ayAQ.0_kdm-RksN6HvCxzZKtKcxqRq18')
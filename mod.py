import discord
import asyncio
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import CheckFailure
from discord.ext.commands import has_permissions, CheckFailure

class moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #kick
    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None): 
        message = ctx.message
        await message.delete(delay=120)
        await member.kick(reason=reason)
        await ctx.send(f'{member} has been kicked for: {reason}', delete_after=120)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"You don't have permission to perform this command", delete_after=120)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Missing arguments", delete_after=120)
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"Something went wrong", delete_after=120)

    #ban
    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        message = ctx.message
        await message.delete(delay=120)
        await member.ban(reason=reason)
        await ctx.send(f'{member} has been banned for: {reason}', delete_after=120)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"You don't have permission to perform this command", delete_after=120)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Missing arguments", delete_after=120)
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"Something went wrong", delete_after=120)
    
    #clear
    @commands.command()
    @has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        amount = amount + 1
        await ctx.channel.purge(limit=amount)
    
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"You don't have permission to perform this command", delete_after=120)

    #mute
    @commands.command()
    @has_permissions(kick_members=True)
    async def mute(self, ctx, user: discord.Member, mute_time : int):
        message = ctx.message
        await message.delete(delay=120)
        mute_Role = get(ctx.message.guild.roles, name='Muted')
        speak_Role = get(ctx.message.guild.roles, name='Not racist')
        await user.add_roles(mute_Role)
        await user.remove_roles(speak_Role)
        await ctx.send(f"{user.name} has been muted for {mute_time} minutes", delete_after=120)
        await asyncio.sleep(mute_time * 60)
        await user.remove_roles(mute_Role)
        await user.add_roles(speak_Role)
        await ctx.send(f'{user.name} has been unmuted', delete_after=120)
        print("unmuted")


    
    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"You don't have permission to perform this command", delete_after=120)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Missing arguments", delete_after=120)
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"Something went wrong", delete_after=120)

    #unmute
    @commands.command()
    @has_permissions(kick_members=True)
    async def unmute(self, ctx, user: discord.Member):
        message = ctx.message
        await message.delete(delay=120)
        mute_Role = get(ctx.message.guild.roles, name='Muted')
        speak_Role = get(ctx.message.guild.roles, name='Not racist')
        await user.add_roles(speak_Role)
        await user.remove_roles(mute_Role)
        await ctx.send(f'{user.name} has been unmuted', delete_after=120)

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"You don't have permission to perform this command", delete_after=120)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Missing arguments", delete_after=120)
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"Something went wrong", delete_after=120)


def setup(client):
    client.add_cog(moderation(client))
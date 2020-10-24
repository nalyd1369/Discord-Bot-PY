import discord
import os
import random
from discord.ext import commands
from discord.ext.commands import Bot

class annoy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_role("Not racist")
    @commands.cooldown(5,150, commands.BucketType.channel)
    async def spam(self, ctx, folder="die"):
        message = ctx.message
        bruh=["0","1","2","3","4","5","6","7","8","9"]
        await message.delete(delay=45)
        if (folder=="hentai" or folder=="Hentai"):
            if ctx.channel.is_nsfw():
                image = os.listdir('./Spam_commands/Spam/')
                for x in bruh:
                    imgString = random.choice(image)  # Selects a random element from the list
                    path = "./Spam_commands/Spam/" + imgString
                    await ctx.send(file=discord.File(path), delete_after=45)
            else:
                await ctx.send(f"That library isn't available in this channel", delete_after=120)

        if (folder=="legs" or folder=="Legs"):
            image = os.listdir('./Spam_commands/Legs/')
            for x in bruh:
                imgString = random.choice(image)  # Selects a random element from the list
                path = "./Spam_commands/Legs/" + imgString
                await ctx.send(file=discord.File(path), delete_after=45)

        if (folder=="cringe" or folder=="Cringe"):
            image = os.listdir('./Spam_commands/Cringe/')
            for x in bruh:
                imgString = random.choice(image)  # Selects a random element from the list
                path = "./Spam_commands/Cringe/" + imgString
                await ctx.send(file=discord.File(path), delete_after=45)

        if (folder=="dead" or folder=="Dead" or folder=="Ded" or folder=="ded"):
            image = os.listdir('./Spam_commands/Skeleton/')
            for x in bruh:
                imgString = random.choice(image)  # Selects a random element from the list
                path = "./Spam_commands/Skeleton/" + imgString
                await ctx.send(file=discord.File(path), delete_after=45)
        
        if (folder=="rishi" or folder=="Rishi"):
            image = os.listdir('./Spam_commands/rishi/')
            for x in bruh:
                imgString = random.choice(image)  # Selects a random element from the list
                path = "./Spam_commands/rishi/" + imgString
                await ctx.send(file=discord.File(path), delete_after=45)

        if (folder=="cursed" or folder=="Cursed"):
            if ctx.channel.is_nsfw():
                image = os.listdir('./Spam_commands/Cursed/')
                for x in bruh:
                    imgString = random.choice(image)  # Selects a random element from the list
                    path = "./Spam_commands/Cursed/" + imgString
                    await ctx.send(file=discord.File(path), delete_after=45)
            else:
                await ctx.send(f"That library isn't available in this channel", delete_after=120)

        if (folder=="die" or folder=="die"):
            image = os.listdir('./Spam_commands/die/')
            for x in bruh:
                imgString = random.choice(image)  # Selects a random element from the list
                path = "./Spam_commands/die/" + imgString
                await ctx.send(file=discord.File(path), delete_after=45)
    
    @spam.error
    async def spam_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'Command is on cooldown', delete_after=120)
        if isinstance(error, commands.NSFWChannelRequired):
            await ctx.send(f"That library isn't available in this channel", delete_after=120)

        
def setup(client):
    client.add_cog(annoy(client))
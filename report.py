import discord
import random
from discord.ext import commands
from discord.ext.commands import has_role
from discord.ext.commands import CheckFailure
from discord.utils import get


class report(commands.Cog):
    def __init__(self, client):
        self.client = client

    #give and take roles
    @commands.command()
    @commands.cooldown(10,300, commands.BucketType.channel)
    async def report(self, ctx, user: discord.Member, *, role: discord.Role):
        role_to_remove = get(ctx.message.guild.roles, name='Not racist')
        role_to_check = get(ctx.message.guild.roles, name='Different')
        Gay_check = get(ctx.message.guild.roles, name='Gay')
        Racist_check = get(ctx.message.guild.roles, name='Racist')
        Karen_check = get(ctx.message.guild.roles, name='Karen')
        Impostor_check = get(ctx.message.guild.roles, name='Impostor')
        Capping_hard_check = get(ctx.message.guild.roles, name='Capping hard')
        Illiterate_check = get(ctx.message.guild.roles, name='Illiterate')

        Racist_responses = ["Bro same", "I do not associate with niggers"]
        Gay_responses = ["I fucking called it", "James Charles?", "The colored hair is strong with this one", "What's their favorite color of flannel?", "🏳️‍🌈"]
        Impostor_responses = ["I'll send them out the airlock", "Yeah, I saw him vent", "Knew it", "He faked dragon"]
        Karen_responses = ["What a bitch", "Bruh I'm not the manager", "I'm blinded by their skin", "I was born in Canada, I swear", "Don't call Trump"]
        Illiterate_responses = ["Lmao that guy's fuckin retarded", "Goo ga goo?", "Ching chong wing wong fing fong ding dong", "dsjaf;lkdsajfol;dsajhfo;ia - them"]
        Capping_hard_responses = ["That's a literal sin", "Say on god", "On jah?", "No cap stretching to the moon?", "That's pretty yankee with no brim of them"]
        Immune_responses = ["Nah, they built different", "I can't he's too different", "Coochie man", "His different pass hasn't expired yet"]
        Not_Racist_responses = ["No, they must apologize", "Thanks for telling me that?", "You're helpful", "Fuck off"]

        message = ctx.message
        await message.delete(delay=120)

        if role_to_check in user.roles:
            await ctx.send(f"He's too different, I can't")
        else:
            if role.name == "Different":
                await ctx.send(random.choice(Immune_responses))
            if role.name == "Not racist":
                await ctx.send(random.choice(Not_Racist_responses))

            if role.name == "Gay":
                if Gay_check in user.roles:
                    await ctx.send(f"I'm aware")
                else:
                    await ctx.send(random.choice(Gay_responses))
                    await user.add_roles(role)
                    
            if role.name == "Racist":
                if Racist_check in user.roles:
                    await ctx.send(f"I'm aware")
                else:
                    await ctx.send(random.choice(Racist_responses))
                    await user.add_roles(role)
                    await user.remove_roles(role_to_remove)
            if role.name == "Karen":
                if Karen_check in user.roles:
                    await ctx.send(f"I'm aware")
                else:
                    await ctx.send(random.choice(Karen_responses))
                    await user.add_roles(role)
                    await user.remove_roles(role_to_remove)
            if role.name == "Impostor":
                if Impostor_check in user.roles:
                    await ctx.send(f"I'm aware")
                else:
                    await ctx.send(random.choice(Impostor_responses))
                    await user.add_roles(role)
            if role.name == "Capping hard":
                if Capping_hard_check in user.roles:
                    await ctx.send(f"I'm aware")
                else:
                    await ctx.send(random.choice(Capping_hard_responses))
                    await user.add_roles(role)
                    await user.remove_roles(role_to_remove)
            if role.name == "Illiterate":
                if Illiterate_check in user.roles:
                    await ctx.send(f"I'm aware")
                else:
                    await ctx.send(random.choice(Illiterate_responses))
                    await user.add_roles(role)

    @report.error
    async def joke_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Missing arguments")
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'Command is on cooldown')
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"Something went wrong")

    @commands.command(pass_context=True)
    async def sorry(self, ctx, *, role: discord.Role):
        user = ctx.message.author
        role_to_give = get(ctx.message.guild.roles, name='Not racist')
        Gay_check = get(ctx.message.guild.roles, name='Gay')
        Racist_check = get(ctx.message.guild.roles, name='Racist')
        Karen_check = get(ctx.message.guild.roles, name='Karen')
        Impostor_check = get(ctx.message.guild.roles, name='Impostor')
        Capping_hard_check = get(ctx.message.guild.roles, name='Capping hard')
        Illiterate_check = get(ctx.message.guild.roles, name='Illiterate')
        Immune_check = get(ctx.message.guild.roles, name='Different')

        Racist_sorry = ["I forgive you, but you need to cool it with the hard R's"]
        Gay_sorry = [f"Wait, you're gay?\n*{user.name} has been banned.*"]
        Impostor_sorry = ["NAH, out the the airlock"]
        Karen_sorry = ["Fine but you really need to stop being a bitch"]
        Illiterate_sorry = ["Goo goo ga ga?"]
        Capping_hard_sorry = ["Lying is a sin, I'll report you to jesus next time"]
        Immune_sorry = ["You're fucking retarded but fine"]
        Not_racist_sorry = ["Stop it dipshit"]

        message = ctx.message
        await message.delete(delay=120)

        if role.name == "Not racist":
            await ctx.send(random.choice(Not_racist_sorry), delete_after=120)

        if role.name == "Racist":
            if Racist_check in user.roles:
                await ctx.send(random.choice(Racist_sorry), delete_after=120)
                await user.remove_roles(role)
                if Karen_check not in user.roles and Capping_hard_check not in user.roles:
                    await user.add_roles(role_to_give)
            else:
                await ctx.send("Why are you apologizing for something you didn't do?", delete_after=120)

        if role.name == "Gay":
            if Gay_check in user.roles:
                await ctx.send(random.choice(Gay_sorry), delete_after=120)
                await user.remove_roles(role)
                if Karen_check not in user.roles and Capping_hard_check not in user.roles and Racist_check not in user.roles:
                    await user.add_roles(role_to_give)
            else:
                await ctx.send("Why are you apologizing for something you didn't do?", delete_after=120)

        if role.name == "Impostor":
            if Impostor_check in user.roles:
                await ctx.send(random.choice(Impostor_sorry), delete_after=120)
                await user.remove_roles(role)
                if Karen_check not in user.roles and Capping_hard_check not in user.roles and Racist_check not in user.roles:
                    await user.add_roles(role_to_give)
            else:
                await ctx.send("Why are you apologizing for something you didn't do?", delete_after=120)

        if role.name == "Karen":
            if Karen_check in user.roles:
                await ctx.send(random.choice(Karen_sorry), delete_after=120)
                await user.remove_roles(role)
                if Capping_hard_check not in user.role and Racist_check not in user.roles:
                    await user.add_roles(role_to_give)
            else:
                await ctx.send("Why are you apologizing for something you didn't do?", delete_after=120)
                
        if role.name == "Capping hard":
            if Capping_hard_check in user.roles:
                await ctx.send(random.choice(Capping_hard_sorry), delete_after=120)
                await user.remove_roles(role)
                if Karen_check not in user.roles and Racist_check not in user.roles:
                    await user.add_roles(role_to_give)
            else:
                await ctx.send("Why are you apologizing for something you didn't do?", delete_after=120)

        if role.name == "Different":
            if Immune_check in user.roles:
                await ctx.send(random.choice(Immune_sorry), delete_after=120)
                await user.remove_roles(role)
                if Karen_check not in user.roles and Capping_hard_check not in user.roles and Racist_check not in user.roles:
                    await user.add_roles(role_to_give)
            else:
                    await ctx.send("Why are you apologizing for something you didn't do?", delete_after=120)
            
        if role.name == "Illiterate":
            if Illiterate_check in user.roles:
                await ctx.send(random.choice(Illiterate_sorry), delete_after=120)
                await user.remove_roles(role)
                if Karen_check not in user.roles and Capping_hard_check not in user.roles and Racist_check not in user.roles:
                    await user.add_roles(role_to_give)
            else:
                await ctx.send("Why are you apologizing for something you didn't do?", delete_after=120)
    @sorry.error
    async def sorry_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Missing arguments", delete_after=120)
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"Something went wrong", delete_after=120)

def setup(client):
    client.add_cog(report(client))
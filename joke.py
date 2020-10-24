import discord
from discord.ext import commands
import random

class joke(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(10,90, commands.BucketType.channel)
    @commands.has_role("Not racist")
    async def joke(self, ctx):
        message = ctx.message
        await message.delete(delay=15)
        jokes = ["What did the the jam say to the bread?", 
        'Why do we tell actors to "break a leg"?',
        'How many times can you subtract 10 from 100?',
        "Knock Knock",
        "Why don't scientists trust atoms?",
        'Why did the chicken go to the seance?',
        'How do you drown a hipster?',
        'What’s the best thing about Switzerland?',
        'I invented a new word',
        'Did you hear about the mathematician who’s afraid of negative numbers?',
        'Why do we tell actors to “break a leg?”',
        'Helvetica and Times New Roman walk into a bar',
        'Yesterday I saw a guy spill all his Scrabble letters on the road.',
        'Hear about the new restaurant called Karma?',
        'Did you hear about the actor who fell through the floorboards?',
        'Did you hear about the claustrophobic astronaut?',
        'Where are average things manufactured?',
        'What does a nosy pepper do?',
        'Why are pirates called pirates?',
        'Why can’t you explain puns to kleptomaniacs?',
        'How do you keep a bagel from getting away?',
        'A man tells his doctor, “Doc, help me. I’m addicted to Twitter!”',
        'What kind of exercise do lazy people do?',
        'Why don’t Calculus majors throw house parties?',
        'What do you call a parade of rabbits hopping backwards?',
        'What does Charles Dickens keep in his spice rack?',
        'What’s the different between a cat and a comma?',
        'Why should the number 288 never be mentioned?',
        'What did the Tin Man say when he got run over by a steamroller?',
        'What did the bald man exclaim when he received a comb for a present?',
        'What rhymes with orange',
        'What did the left eye say to the right eye?',
        'What do you call a fake noodle?',
        'How do you make a tissue dance?',
        'What did the 0 say to the 8?',
        'What do you call a pony with a cough?',
        'What did one hat say to the other?',
        'What do you call a magic dog?',
        'What did the shark say when he ate the clownfish?',
        'What’s orange and sounds like a carrot?']

        await ctx.send(random.choice(jokes) + "\n..." + "\nNigga!", delete_after=15)

    @joke.error
    async def joke_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f"I don't serve bad people", delete_after=15)
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'Command is on cooldown', delete_after=15)

def setup(client):
    client.add_cog(joke(client))
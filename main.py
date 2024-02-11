from typing import Optional
import os
import discord
from discord import app_commands
import sys
import random
import time
from news import preamble, cata, catb, catc, closing, corps, gangs, areas, plans, accidents, mysteries
from markets import categories, foods, electronics, combatgear, cyberware, clothing, survival
from criticalinjuries import *

token = os.getenv("token")
new_line = '\n'
MY_GUILD = discord.Object(id=1191987404853215262)  # replace with your guild id
THEIR_GUILD = discord.Object(id=611115334971162624) 


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        # A CommandTree is a special type that holds all the application command
        # state required to make it work. This is a separate class because it
        # allows all the extra state to be opt-in.
        # Whenever you want to work with application commands, your tree is used
        # to store and work with them.
        # Note: When using commands.Bot instead of discord.Client, the bot will
        # maintain its own tree instead.
        self.tree = app_commands.CommandTree(self)

    # In this basic example, we just synchronize the app commands to one guild.
    # Instead of specifying a guild to every command, we copy over our global commands instead.
    # By doing so, we don't have to wait up to an hour until they are shown to the end-user.
    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)
        self.tree.copy_global_to(guild=THEIR_GUILD)
        await self.tree.sync(guild=THEIR_GUILD)


intents = discord.Intents.default()
client = MyClient(intents=intents)


@client.event
async def on_ready():
    print('Black ice online! Instance ID is {0.user}'.format(client))
    print('------')

@client.tree.command()
async def nightmarket(interaction: discord.Interaction):
    ITEMS_WON_EMBED_TITLE = "Good evening shoppers, its time for the night market!"
    MAIN_COLOR = 0xffec00 
    currenttime = int(time.time()) 
    dealtime = currenttime + 172800
    stocktypes = tuple(random.sample(categories, 2))
    marketembed = discord.Embed(color=MAIN_COLOR, title=ITEMS_WON_EMBED_TITLE, description=f'Get your eddies ready because this stock wont last! {new_line} This offer expires at <t:{dealtime}>')
    for n in stocktypes:
        if n == "Food and drugs":
            goods = foods
        elif n == "Personal Electronics":
            goods = electronics
        elif n == "Weapons and Armor":
            goods = combatgear
        elif n == "Cyberware":
            goods = cyberware
        elif n == "Clothing and Fashionware":
            goods = clothing
        elif n == "Survival Gear":
            goods = survival
        else: print ("error: goods cannot be found, sorry.[this is a bug in the code]")
        count = random.choice([1, 2, 3, 4, 5, 6, 7 ,8, 9, 10])
        inv = tuple(random.sample(goods, count))
        shoptitle = f'**__We have {count} Offering(s) of  {n}:__**'
        marketembed.add_field(name=shoptitle, value="", inline=False)
        for x in inv:
            y = f'- {x}'
            marketembed.add_field(name=y , value="", inline=False)
    await interaction.response.send_message(embed=marketembed)

@client.tree.command()
async def news(interaction: discord.Interaction):

    intro = random.choice(preamble)
    topica = random.choice(cata)
    topicb = random.choice(catb)
    topicc = random.choice(catc)
    outro  = random.choice(closing)

    if topica == "An undisclosed corp":
        newsa = random.choice(corps)
    elif topica == "a gang":
        newsa = random.choice(gangs)
    elif topica == "a gang of rich investors":
        newsa = ("a gang of rich investors from " + random.choice(corps))
    elif topica == "some anonymous Fixer":
        newsa = ("some anonymous Fixer based in " + random.choice(areas))
    elif topica == "an alliance of corpos":
        corpgang = random.sample(corps, 2)
        tidiedcorpgang = (corpgang[0] + " and " + corpgang[1])
        newsa = ("an alliance of corpos from " + tidiedcorpgang)
    else:
        newsa = topica

    if topicb == "is threatening":
        newsb = ("is threatening " + random.choice(cata) + " with")
    else:
        newsb = topicb

    if topicc == "a plan.":
        newsc = ("a plan to " + random.choice(plans))
    elif topicc == "a compromise.":
        newsc = ("a compromise by agreeing to " + random.choice(plans))
    elif topicc == "an accident.":
        newsc = ("an accident " + random.choice(accidents))
    elif topicc == "a mysterious man.":
        newsc = ("a mysterious man, all we know about him is he " + random.choice(mysteries))
    elif topicc == "a mysterious woman.":
        newsc = ("a mysterious woman, all we know about her is she " + random.choice(mysteries))
    else:
        newsc = topicc

    print("The intro is", intro)
    print("The first category is", topica)
    print("The Second category is", topicb)
    print("The Third category is", topicc)
    print("The Outro is", outro)

    print("The News is")
    print(intro, newsa, newsb, newsc, outro)
    news_embed_title = f'{intro} {newsa} {newsb} {newsc} {outro}'
    MAIN_COLOR = 0xffec00 
    newsembed = discord.Embed(color=MAIN_COLOR, title=news_embed_title, description=f'')
    await interaction.response.send_message(embed=newsembed)

# To make an argument optional, you can either give it a supported default argument
# or you can mark it as Optional from the typing standard library. This example does both.

@client.tree.command()
@app_commands.describe(location='Where did you get hit choom?!')
@app_commands.choices(location=[
    app_commands.Choice(name="Head", value="Head"),
    app_commands.Choice(name="Body", value="Body"),
    ])
async def crit(interaction: discord.Interaction, location: app_commands.Choice[str]):
    injuryembed_title = "Oh no, they got you good this time choom!"
    injuryembed_colour = 0xffec00 
    injury_lists = {'b2': b2, 'b3': b3, 'b4': b4, 'b5': b5, 'b6': b6, 'b7': b7, 'b8': b8, 'b9': b9, 'b10': b10, 'b11': b11, 'b12': b12, 'h2': h2, 'h3': h3, 'h4': h4, 'h5': h5, 'h6': h6, 'h7': h7, 'h8': h8, 'h9': h9, 'h10': h10, 'h11': h11, 'h12': h12}
    roll = (random.randint(1, 6))+(random.randint(1, 6))
    if location.value == "Head":
        letter = 'h'
    elif location.value == "Body":
        letter = 'b'

    injury = letter + str(roll)
    injury_list = injury_lists.get(injury)
    injuryembed = discord.Embed(color=injuryembed_colour, title=injuryembed_title, description=f'')
    injuryembed.add_field(name="Injury" , value=injury_list[0], inline=True)
    injuryembed.add_field(name="Effect" , value=injury_list[1], inline=False)
    injuryembed.add_field(name="Quick-Fix" , value=injury_list[2], inline=True)
    injuryembed.add_field(name="Treatment" , value=injury_list[3], inline=True)
    await interaction.response.send_message(embed=injuryembed)

#    """Says when a member joined."""
#    # If no member is explicitly provided then we use the command user here
#    member = member or interaction.user
#
#    # The format_dt function formats the date time into a human readable representation in the official client
#    await interaction.response.send_message(f'{member} joined {discord.utils.format_dt(member.joined_at)}')


# A Context Menu command is an app command that can be run on a member or on a message by
# accessing a menu within the client, usually via right clicking.
# It always takes an interaction as its first parameter and a Member or Message as its second parameter.

# This context menu command only works on members

#@client.tree.context_menu(name='Show Join Date')
#async def show_join_date(interaction: discord.Interaction, member: discord.Member):
#    # The format_dt function formats the date time into a human readable representation in the official client
#    await interaction.response.send_message(f'{member} joined at {discord.utils.format_dt(member.joined_at)}')

client.run(token)
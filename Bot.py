#BotDee By DlolFace

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from itertools import cycle
import os
import youtube_dl

client = commands.Bot(command_prefix='~')

players = {}

@client.event
async def on_ready():
    print ("Ready!!")
    print ("I am " + client.user.name + " a bot sent by Cybe...i mean DlolFace")
    print ("My ID Serial Number Is : " + client.user.id)

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Chefs')
    await client.add_roles(member, role)

@client.command(pass_context=True)
async def test(ctx):
    await client.say("Procedure Success")
    print ("Test Subject Complete")

@client.command(pass_context=True)
async def whoareu(ctx):
    await client.say("Hello im {}".format(client.user.name))
    await client.say("I am a bot sent by Cybe-...DlolFace")
    await client.say("my function is not complete yet since the owner is a moron")
    print ("Introduction Complete")

@client.command(pass_context=True)
async def scan(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s Name".format(user.name), description="This Is The Data I've Got", color=0xff00ce)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Role", value=user.top_role, inline=True)
    embed.add_field(name="Joined Since", value=user.joined_at, inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)
    print ("Person Profile Has Been Sent In By this Command")

@client.command(pass_context=True)
async def serverdata(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what i got", color=0xffb1b1)
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Role", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await client.say(embed=embed)
@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()
    
client.run(os.getenv('TOKEN'))

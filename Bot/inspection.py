from asyncio.windows_events import PipeServer
from hashlib import new
from os import name
from re import M
import discord
import asyncio
from discord import message
from discord import channel
from discord import user
from discord import embeds
from discord.ext import commands
from discord.ext.commands import Bot, bot
from discord.ext.commands.core import check
from discord import DMChannel
import datetime
from time import *

token = ''

client = Bot(command_prefix='!')

msg = """
더 나은 기능을 위해 제공하기 위해 점검중입니다.

인증기능이 비활성화 됩니다.
"""

@client.command(name="점검")
@commands.has_permissions(administrator=True)
async def test(message):
    await message.channel.purge(limit=int(1))
    embed = discord.Embed(title=f"**점검 중**",description=msg, color=0x6937a1)
    await message.channel.send(embed = embed)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.playing, name="점검 중"))
    print("점검")


client.run(token)

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

#폐기
#code = {}
#code_list = []

object_msg = """
-🔵 학생
-🟣 교수
"""
notice_list = ["""
22학번

정보 보안과 스터디 서버입니다.

디스코드 접속 시 본명으로 이름을 바꾸어 주시길 바라며, 서로 간의 예의를 지켜주시길 바랍니다.
따로 규칙은 없으며, 교수님과 학생의 선을 지켜주시길 바랍니다.

역할 지급에 사용된 이모티콘 사용을 자제바라며,
문제 발생 시 문의해 주시길 바랍니다.
"""]

project_list = ["""sample"""]

client = Bot(command_prefix='!')


@client.command(name="과제리스트")
@commands.has_permissions(administrator=True)
async def test(message):
    await message.channel.purge(limit=int(1))
    global project_list
    msg_list = """"""
    for i in range(0, len(project_list)):
        msg_list += f"{i+1}. " + project_list[i] + "\n"
    await message.channel.send(f"```{msg_list}```")


@client.command(name="과제삭제")
@commands.has_permissions(administrator=True)
async def test(message, num):
    global project_list

    await message.channel.purge(limit=int(1))
    del project_list[int(num)-1]

    await message.channel.send(f"** {num}번쨰 과제내용을 삭제하였습니다.**")

    await asyncio.sleep(2)
    await message.channel.purge(limit=int(1))

@client.command(name="과제등록")
@commands.has_permissions(administrator=True)
async def test(message, num):

    global notice_list

    await message.channel.purge(limit=int(1))
    
    embed = discord.Embed(title=f"**새로운 과제!**",description=f"{project_list[int(num) - 1]}", color=0xFF0000)
    await message.channel.send(embed = embed)

@client.command(name="과제입력")
@commands.has_permissions(administrator=True)
async def test(message):
    def check(m):
            return m.author == message.author and m.channel == message.channel
    await message.channel.purge(limit=int(1))
    global project_list

    await message.channel.send("과제 내용을 한번에 적어주세요.")
    try:
        msg = await client.wait_for("message", check=check, timeout=600)
        msg = msg.content
        if msg == "취소":
            await message.channel.purge(limit=int(1))
            await message.channel.send(f"취소하였습니다.")
            await asyncio.sleep(1)
            await message.channel.purge(limit=int(1))

            return
        project_list.append(f"""{msg}""")
        await message.channel.purge(limit=int(2))
        await message.channel.send(f"\n`{msg}`\n\n**내용이 추가되었습니다.**")
        await asyncio.sleep(2)
        await message.channel.purge(limit=int(1))
        
    except asyncio.exceptions.TimeoutError:
        await message.channel.purge(limit=int(1))
        await message.channel.send("**10분간 입력이 되지 않아 입력을 취소했어요.**")
        await asyncio.sleep(2)
        await message.channel.purge(limit=int(1))


@client.command(name="공지리스트")
@commands.has_permissions(administrator=True)
async def test(message):
    await message.channel.purge(limit=int(1))
    global notice_list
    msg_list = """"""
    for i in range(0, len(notice_list)):
        msg_list += f"{i+1}. " + notice_list[i] + "\n"
    await message.channel.send(f"```{msg_list}```")


@client.command(name="공지삭제")
@commands.has_permissions(administrator=True)
async def test(message, num):
    global notice_list

    await message.channel.purge(limit=int(1))
    del notice_list[int(num)-1]

    await message.channel.send(f"** {num}번쨰 공지내용을 삭제하였습니다.**")

    await asyncio.sleep(2)
    await message.channel.purge(limit=int(1))

@client.command(name="공지등록")
@commands.has_permissions(administrator=True)
async def test(message, num):

    global notice_list

    await message.channel.purge(limit=int(1))
    
    embed = discord.Embed(title=f"**새로운 공지사항!**",description=f"{notice_list[int(num) - 1]}", color=0x6937a1)
    await message.channel.send(embed = embed)

@client.command(name="공지입력")
@commands.has_permissions(administrator=True)
async def test(message):
    def check(m):
            return m.author == message.author and m.channel == message.channel
    await message.channel.purge(limit=int(1))
    global notice_list

    await message.channel.send("공지 내용을 한번에 적어주세요.")
    try:
        msg = await client.wait_for("message", check=check, timeout=600)
        msg = msg.content

        if msg == "취소":
            await message.channel.purge(limit=int(1))
            await message.channel.send(f"취소하였습니다.")
            await asyncio.sleep(1)
            await message.channel.purge(limit=int(1))

            return
        notice_list.append(f"""{msg}""")
        await message.channel.purge(limit=int(2))
        await message.channel.send(f"\n`{msg}`\n\n**내용이 추가되었습니다.**")
        await asyncio.sleep(2)
        await message.channel.purge(limit=int(1))
        
    except asyncio.exceptions.TimeoutError:
        await message.channel.purge(limit=int(1))
        await message.channel.send("**10분간 입력이 되지 않아 입력을 취소했어요.**")
        await asyncio.sleep(2)
        await message.channel.purge(limit=int(1))


@client.command(name="인증")
@commands.has_permissions(administrator=True)
async def test(message):

    await message.channel.purge(limit=int(1))
    embed = discord.Embed(title=f"**처음오셨나요? 역할을 신청하세요!**",description=object_msg, color=0x6937a1)
    checked = await message.channel.send(embed = embed)
    await checked.add_reaction("🔵")
    await checked.add_reaction("🟣")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.playing, name="인증 시스템"))
    print("온라인")

@client.event
async def on_raw_reaction_add(payload):
    member = payload.member
    guild = member.guild
    emoji = payload.emoji.name

    if member.bot == True:
        return None
    if emoji == "🔵":
        role = discord.utils.get(guild.roles, name="학생")
        await member.add_roles(role)
    #폐기
    '''
    if emoji == "🟣":
        role = discord.utils.get(guild.roles, name="교수")
        global code
        checked = False
        embed = discord.Embed(title=f"**인증**", description="발급받은 인증코드를 입력해주세요.",color=0x6937a1)
        await member.send(embed=embed)

        an_code = await client.wait_for("Message", check = check)

        if an_code.content in code_list:
            name = code[an_code.content]
            embed = discord.Embed(title=f"**정상적으로 인증되었습니다.**", description=f"환영합니다! {name}!",color=0x6937a1)
            await member.send(embed=embed)
            await member.add_roles(role)
        else:
            embed = discord.Embed(title=f"**인증실패*", description="인증번호가 알맞지 않습니다.",color=0x6937a1)
            await member.send(embed=embed)
    '''

client.run(token)

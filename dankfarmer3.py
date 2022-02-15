import os
import discord
import asyncio
import random
import datetime
import colorama
from discord.ext import commands
from colorama import Fore, init
init()
data = {}

prefix = os.environ.get('PREFIX')
token = os.environ.get('TOKEN')

dank = commands.Bot(command_prefix=prefix, self_bot=True, case_insensitive=True, intents=discord.Intents.all())
dank.remove_command('help')

stream_url = "https://www.twitch.tv/monstercat"
tts_language = "en"

start_time = datetime.datetime.utcnow()

@dank.event
async def on_ready():
    print(f'''



{Fore.LIGHTMAGENTA_EX}         ╔═══╗ ╔═══╗ ╔═╗ ╔╗ ╔╗╔═╗  {Fore.CYAN} ╔═══╗ ╔═══╗ ╔═══╗ ╔═╗╔═╗ ╔═══╗ ╔═══╗
{Fore.LIGHTMAGENTA_EX}         ╚╗╔╗║ ║╔═╗║ ║║╚╗║║ ║║║╔╝  {Fore.CYAN} ║╔══╝ ║╔═╗║ ║╔═╗║ ║║╚╝║║ ║╔══╝ ║╔═╗║
{Fore.LIGHTMAGENTA_EX}          ║║║║ ║║ ║║ ║╔╗╚╝║ ║╚╝╝   {Fore.CYAN} ║╚══╗ ║║ ║║ ║╚═╝║ ║╔╗╔╗║ ║╚══╗ ║╚═╝║
{Fore.LIGHTMAGENTA_EX}          ║║║║ ║╚═╝║ ║║╚╗║║ ║╔╗║   {Fore.CYAN} ║╔══╝ ║╚═╝║ ║╔╗╔╝ ║║║║║║ ║╔══╝ ║╔╗╔╝
{Fore.LIGHTMAGENTA_EX}         ╔╝╚╝║ ║╔═╗║ ║║ ║║║ ║║║╚╗  {Fore.CYAN}╔╝╚╗   ║╔═╗║ ║║║╚╗ ║║║║║║ ║╚══╗ ║║║╚╗
{Fore.LIGHTMAGENTA_EX}         ╚═══╝ ╚╝ ╚╝ ╚╝ ╚═╝ ╚╝╚═╝  {Fore.CYAN}╚══╝   ╚╝ ╚╝ ╚╝╚═╝ ╚╝╚╝╚╝ ╚═══╝ ╚╝╚═╝

{Fore.MAGENTA}          ╔═════════════════════════════════════════════════════════╗
{Fore.GREEN}            Developer: {Fore.LIGHTRED_EX}Not a Nub | notanub@seized.email
{Fore.GREEN}            User: {Fore.LIGHTRED_EX}{dank.user.name}#{dank.user.discriminator} ID: {dank.user.id}
{Fore.GREEN}            Guilds: {Fore.LIGHTRED_EX}{len(dank.guilds)}
{Fore.GREEN}            Prefix: {Fore.LIGHTRED_EX}{dank.command_prefix}
{Fore.GREEN}            Version: {Fore.LIGHTRED_EX}1
{Fore.MAGENTA}          ╚═════════════════════════════════════════════════════════╝

  ''' + Fore.RESET)
    dank.play = True
    if dank.play == True:
            abc = os.environ.get('CHANNELID')
            channel = dank.get_channel(abc)
            await channel.send("Autoplay is successfully bound to `" + channel.name + "`", delete_after=3)
    else: 
        await ctx.send("Autoplay is successfully *disabled*", delete_after=3)
    while dank.play is True:
            try:
                await asyncio.sleep(5)
                await channel.send('pls beg')
                await asyncio.sleep(5)
                await channel.send('pls dep all')
                await asyncio.sleep(5)
                await channel.send('pls hunt')
                await asyncio.sleep(5)
                await channel.send('pls fish')
                await asyncio.sleep(25)
                await channel.send('pls dig')
            except:
                print("Couldn't Play. Did the channel get nuked or deleted?")


@dank.command()
async def uptime(ctx):
    await ctx.message.delete()
    now = datetime.datetime.utcnow()
    delta = now - start_time
    hours, remainder =divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    if days:
        time_format = "**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds."
    else:
        time_format = "**{h}** hours, **{m}** minutes, and **{s}** seconds."
    uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
    await ctx.send(uptime_stamp)


@dank.command(aliases=['logout', 'exit'])
async def shutdown(ctx):
    await ctx.message.delete()
    await dank.logout()


@dank.command(aliases=['credit'])
async def credits(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=0xd142b5, timestamp=ctx.message.created_at)
    embed.set_author(name="𝘾𝙍𝙀𝘿𝙄𝙏𝙎")
    embed.add_field(name="**Le Creator/Developer**", value="`Not a Nub#0729`")
    embed.set_image(url='https://media.discordapp.net/attachments/761320654514683914/859264330940022804/image0_7.jpg?width=427&height=428')
    await ctx.send(embed=embed)

dank.run(token, bot=False)

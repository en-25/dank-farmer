import os
import discord
import asyncio
import random
import colorama
from discord.ext import commands
from colorama import Fore
colorama.init()

print(f'{Fore.MAGENTA}~>Enter prefix:{Fore.RESET} ')
prefix = input("")
print(f'{Fore.MAGENTA}~>Enter token:{Fore.RESET} ')
token = input("")

dank = commands.Bot(command_prefix=prefix, self_bot=True, case_insensitive=True, intents=discord.Intents.all())
dank.remove_command('help')


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
{Fore.GREEN}            Developer: {Fore.LIGHTRED_EX}Sociopath | sociopath@thighs.today
{Fore.GREEN}            User: {Fore.LIGHTRED_EX}{dank.user.name}#{dank.user.discriminator} ID: {dank.user.id}
{Fore.GREEN}            Guilds: {Fore.LIGHTRED_EX}{len(dank.guilds)}
{Fore.GREEN}            Prefix: {Fore.LIGHTRED_EX}{dank.command_prefix}
{Fore.GREEN}            Version: {Fore.LIGHTRED_EX}1
{Fore.MAGENTA}          ╚═════════════════════════════════════════════════════════╝

  ''' + Fore.RESET)
    os.system('clear')


@dank.command(invoke_without_command=True)
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=0x9a15c3)
    embed.set_author(name="𝘿𝘼𝙉𝙆 𝙁𝘼𝙍𝙈𝙀𝙍  | 𝙋𝙍𝙀𝙁𝙄𝙓: " + str(dank.command_prefix), icon_url=dank.user.avatar_url)
    embed.set_image(url="https://media1.tenor.com/images/58b49cddfff37475725298562adcf46a/tenor.gif?itemid=13633941")
    embed.add_field(name=" :frog: Beg", value=f"Using cmd `{prefix}beg [on/off]`", inline=False)
    embed.add_field(name=" :frog: Daily", value=f"Using cmd `{prefix}daily [on/off]`", inline=False)
    embed.add_field(name=" :frog: Post Meme", value=f"Using cmd `{prefix}pm [on/off]`", inline=False)
    embed.add_field(name=" :frog: Snake Eyes", value=f"Using cmd `{prefix}se [on/off]`", inline=False)
    embed.add_field(name=" :frog: Fish", value=f"Using cmd `{prefix}fish [on/off]`", inline=False)
    embed.add_field(name=" :frog: Hunt", value=f"Using cmd `{prefix}hunt [on/off]`", inline=False)
    embed.add_field(name=" :frog: Shovel", value=f"Using cmd `{prefix}dig [on/off]`", inline=False)
    embed.add_field(name=" :frog: Credits", value=f"See The Developer, using cmd `{prefix}credits`", inline=False)
    embed.add_field(name=" :frog: Exit", value=f"Exits The Program, using the cmd `{prefix}exit`", inline=True)
    await ctx.send(embed=embed)


dank.beg = False
dank.daily = False
dank.pm = False
dank.se = False
dank.fish = False
dank.hunt = False
dank.dig = False

@dank.command()
async def beg(ctx, param=None):
    await ctx.message.delete()
    if param is None:
        await ctx.send("Please specify yes or no", delete_after=3)
        return
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        if isinstance(ctx.message.channel, (discord.DMChannel, discord.GroupChannel)):
            await ctx.send("You can't bind Autobeg to a DM or GC", delete_after=3)
            return
        else:
            dank.beg = True
            await ctx.send("Autobeg is successfully bound to `" + ctx.channel.name + "`", delete_after=3)
            dank.dankmemer_channel = ctx.channel.id
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        dank.beg = False
        await ctx.send("Autobeg is successfully *disabled*", delete_after=3)
    while dank.beg is True:
            try:
                await ctx.send('pls beg')
                await asyncio.sleep(1)
                await ctx.send('pls dep all')
                await asyncio.sleep(46)
            except:
                print("Couldn't Beg. Did the channel get nuked or deleted?")


@dank.command()
async def daily(ctx, param=None):
    await ctx.message.delete()
    if param is None:
        await ctx.send("Please specify yes or no", delete_after=3)
        return
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        if isinstance(ctx.message.channel, (discord.DMChannel, discord.GroupChannel)):
            await ctx.send("You can't bind Autodaily to a DM or GC", delete_after=3)
            return
        else:
            dank.daily = True
            await ctx.send("Autodaily is successfully bound to `" + ctx.channel.name + "`", delete_after=3)
            dank.dankmemer_channel = ctx.channel.id
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        dank.daily = False
        await ctx.send("Autodaily is successfully *disabled*", delete_after=3)
    while dank.daily is True:
            try:
                await ctx.send('pls daily')
                await asyncio.sleep(1)
                await ctx.send('pls dep all')
                await asyncio.sleep(86400)
            except:
                print("Couldn't Daily. Did the channel get nuked or deleted?")


@dank.command()
async def pm(ctx, param=None):
    frick = ['f', 'r', 'i', 'c', 'k']
    await ctx.message.delete()
    if param is None:
        await ctx.send("Please specify yes or no", delete_after=3)
        return
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        if isinstance(ctx.message.channel, (discord.DMChannel, discord.GroupChannel)):
            await ctx.send("You can't bind Autopm to a DM or GC", delete_after=3)
            return
        else:
            dank.pm = True
            await ctx.send("Autopm is successfully bound to `" + ctx.channel.name + "`", delete_after=3)
            dank.dankmemer_channel = ctx.channel.id
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        dank.pm = False
        await ctx.send("Autopm is successfully *disabled*", delete_after=3)
    while dank.pm is True:
            try:
                await ctx.send('pls pm')
                await asyncio.sleep(1)
                await ctx.send(f'{random.choice(frick)}')
                await asyncio.sleep(1)
                await ctx.send('pls dep all')
                await asyncio.sleep(40)
            except:
                print("Couldn't Post Meme. Did the channel get nuked or deleted?")


@dank.command()
async def fish(ctx, param=None):
    await ctx.message.delete()
    startTime=dt.now()
    if param is None:
        await ctx.send("Please specify yes or no", delete_after=3)
        return
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        if isinstance(ctx.message.channel, (discord.DMChannel, discord.GroupChannel)):
            await ctx.send("You can't bind Autofish to a DM or GC", delete_after=3)
            return
        else:
            dank.fish = True
            await ctx.send("Autofish is successfully bound to `" + ctx.channel.name + "`", delete_after=3)
            dank.dankmemer_channel = ctx.channel.id
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        dank.fish = False
        await ctx.send("Autofish is successfully *disabled*", delete_after=3)
    while dank.fish is True:
            try:
                await ctx.send('pls fish')
                await asyncio.sleep(41)
            except:
                print("Couldn't Hunt. Did the channel get nuked or deleted?")


@dank.command()
async def hunt(ctx, param=None):
    await ctx.message.delete()
    if param is None:
        await ctx.send("Please specify yes or no", delete_after=3)
        return
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        if isinstance(ctx.message.channel, (discord.DMChannel, discord.GroupChannel)):
            await ctx.send("You can't bind Autohunt to a DM or GC", delete_after=3)
            return
        else:
            dank.hunt = True
            await ctx.send("Autohunt is successfully bound to `" + ctx.channel.name + "`", delete_after=3)
            dank.dankmemer_channel = ctx.channel.id
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        dank.hunt = False
        await ctx.send("Autohunt is successfully *disabled*", delete_after=3)
    while dank.hunt is True:
            try:
                await ctx.send('pls hunt')
                await asyncio.sleep(41)
            except:
                print("Couldn't Hunt. Did the channel get nuked or deleted?")


@dank.command(aliases=['snake'])
async def se(ctx, param=None):
    await ctx.message.delete()
    if param is None:
        await ctx.send("Please specify yes or no", delete_after=3)
        return
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        if isinstance(ctx.message.channel, (discord.DMChannel, discord.GroupChannel)):
            await ctx.send("You can't bind Autose to a DM or GC", delete_after=3)
            return
        else:
            dank.se = True
            await ctx.send("Autose is successfully bound to `" + ctx.channel.name + "`", delete_after=3)
            dank.dankmemer_channel = ctx.channel.id
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        dank.se = False
        await ctx.send("Autose is successfully *disabled*", delete_after=3)
    while dank.se is True:
            try:
                await ctx.send('pls with 1000')
                await asyncio.sleep(1)
                await ctx.send('pls se 1000')
                await asyncio.sleep(60)
            except:
                print("Couldn't Snake eyes. Did the channel get nuked or deleted?")


@dank.command()
async def dig(ctx, param=None):
    await ctx.message.delete()
    if param is None:
        await ctx.send("Please specify yes or no", delete_after=3)
        return
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        if isinstance(ctx.message.channel, (discord.DMChannel, discord.GroupChannel)):
            await ctx.send("You can't bind Autodig to a DM or GC", delete_after=3)
            return
        else:
            dank.dig = True
            await ctx.send("Autodig is successfully bound to `" + ctx.channel.name + "`", delete_after=3)
            dank.dankmemer_channel = ctx.channel.id
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        dank.dig = False
        await ctx.send("Autodig is successfully *disabled*", delete_after=3)
    while dank.dig is True:
            try:
                await ctx.send('pls dig')
                await asyncio.sleep(41)
            except:
                print("Couldn't Dig. Did the channel get nuked or deleted?")


@dank.command(aliases=['logout', 'exit'])
async def shutdown(ctx):
    await ctx.message.delete()
    await dank.logout()


@dank.command(aliases=['credit'])
async def credits(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=0xd142b5, timestamp=ctx.message.created_at)
    embed.set_author(name="𝘾𝙍𝙀𝘿𝙄𝙏𝙎")
    embed.add_field(name="**Le Creator/Developer**", value="`Sociopath#5340`")
    embed.set_image(url='https://media.discordapp.net/attachments/761320654514683914/859264330940022804/image0_7.jpg?width=427&height=428')
    await ctx.send(embed=embed)

dank.run(token, bot=False)

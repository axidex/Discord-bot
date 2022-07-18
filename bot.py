import discord
from discord.ext import commands
from discord.utils import get
from config import settings

import re

import random
import asyncio

import aiohttp # google

import json # random images from internet
import requests 

bot = commands.Bot(command_prefix = settings['prefix']) 

song_queue = []
admins = []
skipBans = []
bans = []

@bot.command() 
async def banSkip(ctx, user):
    if ctx.channel.name == settings['bot_channel_name']:
        global admins

        for admin in admins:
            if admin == f"{ctx.message.author.id}":
                break
        else:
            return await ctx.send(f'<:gachiFU:998171613247848448> Fuck you!!!!!!, {ctx.message.author.mention}! You not my master FUCKING SLAVE! <:gachiFU:998171613247848448>') 

        userId = re.findall(r'[0-9]+', f"{user}")

        skipBans.append(userId[0])
        with open('skipBans.dat', 'a') as f:
            f.write(f"{userId[0]}\n")

        await ctx.send(f'Ohh my master {ctx.message.author.mention}, this dirty {user} was added to my slaves note.') 


@bot.command() 
async def ban(ctx, user):
    if ctx.channel.name == settings['bot_channel_name']:
        global admins

        for admin in admins:
            if admin == f"{ctx.message.author.id}":
                break
        else:
            return await ctx.send(f'<:gachiFU:998171613247848448> Fuck you!!!!!!, {ctx.message.author.mention}! You not my master FUCKING SLAVE! <:gachiFU:998171613247848448>') 

        userId = re.findall(r'[0-9]+', f"{user}")

        bans.append(f"{userId[0]}")
        with open('bans.dat', 'a') as f:
            f.write(f"{userId[0]}\n")

        await ctx.send(f'Ohh my master {ctx.message.author.mention}, this dirty {user} was added to my slaves note.') 


@bot.command() 
async def unban(ctx, ban_mode, user):
    """Unban user. Example: slave, unban skipBan @axidex"""
    if ctx.channel.name == settings['bot_channel_name']:
        global admins
        global skipBans
        global bans

        for admin in admins:
            if admin == f"{ctx.message.author.id}":
                break
        else:
            return await ctx.send(f'<:gachiFU:998171613247848448> Fuck you!!!!!!, {ctx.message.author.mention}! You not my master FUCKING SLAVE! <:gachiFU:998171613247848448>') 

        userId = re.findall(r'[0-9]+', f"{user}")

        if ban_mode == "ban":
            ban_list = bans
        elif ban_mode == "skipBan":
            ban_list = skipBans
        else:
            return await ctx.send(f'I dont undestand. It\'s to HAAARD!!!') 

        with open(rf"{ban_mode}s.dat", 'r+') as f:
            lines = f.readlines()

            for i in range(len(lines)):
                if lines[i] == f"{userId[0]}\n":
                    del lines[i]
                    break
            else:
                return await ctx.send(f'I can\'t find this {user} in my slaves note.') 
            
            f.seek(0)
            f.truncate()   
            f.writelines(lines)

        for i in range(len(ban_list)):
            if ban_list[i] == f"{userId[0]}":
                del ban_list[i]
                
        await ctx.send(f'Ohh my lord {ctx.message.author.mention}, this {user} is now free.') 
            

@bot.command() 
async def hello(ctx):
    if ctx.channel.name == settings['bot_channel_name']:
        global bans

        for ban in bans:
            if ban == f"{ctx.message.author.id}":
                return await ctx.send(f'Fuck you, {ctx.message.author.mention}! <:gachiFU:998171613247848448>')
        else:

            author = ctx.message.author 
            await ctx.send(f'Hello, {author.mention}!') 
            
            # add admin to admins.dat
            with open('admin_id.txt', 'a') as f:
                f.write(f"{ctx.author.id}")

@bot.command()
async def fucku(ctx): 
    if ctx.channel.name == settings['bot_channel_name']:
        global bans

        for ban in bans:
            if ban == f"{ctx.message.author.id}":
                return await ctx.send(f'Fuck you, {ctx.message.author.mention}! <:gachiFU:998171613247848448>')
        else:

            author = ctx.message.author

            await ctx.send(f'Fuck u, {author.mention}!') 

@bot.command()
async def joke(ctx):
    if ctx.channel.name == settings['bot_channel_name']:
        global bans

        for ban in bans:
            if ban == f"{ctx.message.author.id}":
                return await ctx.send(f'Fuck you, {ctx.message.author.mention}! <:gachiFU:998171613247848448>')
        else:
            response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
            json_data = json.loads(response.text) # Извлекаем JSON

            embed = discord.Embed(color = 0xff9900, title = 'Random joke') # Создание Embed'a
            embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
            await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    if ctx.channel.name == settings['bot_channel_name']:
        global bans

        for ban in bans:
            if ban == f"{ctx.message.author.id}":
                return await ctx.send(f'Fuck you, {ctx.message.author.mention}! <:gachiFU:998171613247848448>')
        else:
            
            await ctx.send(left + right)

@bot.command()
async def roll(ctx, left: int):
    if ctx.channel.name == settings['bot_channel_name']:
        global bans

        for ban in bans:
            if ban == f"{ctx.message.author.id}":
                return await ctx.send(f'Fuck you, {ctx.message.author.mention}! <:gachiFU:998171613247848448>')
        else:
            await ctx.send(random.randint(0, left)) 

@bot.command()
async def roll100(ctx):
    if ctx.channel.name == settings['bot_channel_name']:
        global bans

        for ban in bans:
            if ban == f"{ctx.message.author.id}":
                return await ctx.send(f'Fuck you, {ctx.message.author.mention}! <:gachiFU:998171613247848448>')
        else:
            await ctx.send(random.randint(0, 100))

@bot.command()
async def roll2(ctx, left: int, right: int):
    if ctx.channel.name == settings['bot_channel_name']:
        global bans

        for ban in bans:
            if ban == f"{ctx.message.author.id}":
                return await ctx.send(f'Fuck you, {ctx.message.author.mention}! <:gachiFU:998171613247848448>')
        else:
            await ctx.send(random.randint(left, right)) 
    
@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    if ctx.channel.name == settings['bot_channel_name']:
        global bans

        for ban in bans:
            if ban == f"{ctx.message.author.id}":
                return await ctx.send(f'Fuck you, {ctx.message.author.mention}! <:gachiFU:998171613247848448>')
        else:
            await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    if ctx.channel.name == settings['bot_channel_name']:
        global bans

        for ban in bans:
            if ban == f"{ctx.message.author.id}":
                return await ctx.send(f'Fuck you, {ctx.message.author.mention}! <:gachiFU:998171613247848448>')
        else:
            for i in range(times):
                await ctx.send(content)




# Youtube #####################################################

from youtube_dl import YoutubeDL
from asyncio import sleep

YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'False'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}


def playNext(ctx):
    del song_queue[0]
    voice_client = get(bot.voice_clients, guild=ctx.guild)

    if len(song_queue) > 0: 
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(song_queue[0], download=False)

        URL = info['formats'][0]['url']

        voice_client.play(discord.FFmpegPCMAudio(executable=settings['ffmpeg_path'], source=URL, **FFMPEG_OPTIONS), after=lambda e: playNext(ctx))
    else:
        if not voice_client.is_playing():
            voice_client.disconnect(ctx)


@bot.command()
async def play(ctx, arg = None):
    """Play song"""

    if ctx.channel.name == settings['bot_channel_name']:
        global bans

        for ban in bans:
            if ban == f"{ctx.message.author.id}":
                return await ctx.send(f'Fuck you, {ctx.message.author.mention}! <:gachiFU:998171613247848448>')
        else:
            global song_queue
            
            if arg is None and not song_queue:
                return await ctx.send(f"Hey {ctx.message.author.mention}, you must include something to play or i will cum inside your ass!")
            else:
                song_queue.append(arg)
                await ctx.send(f"``{arg}`` Thank you sir {ctx.message.author.mention}! I added your song to queue. <:gachiVan:998171539746861108>")

            voice_client = get(bot.voice_clients, guild=ctx.guild)

            if voice_client is None:
                try:
                    voice_channel = ctx.message.author.voice.channel
                    voice_client = await voice_channel.connect()
                except:
                    print('Уже подключен или не удалось подключиться')


                with YoutubeDL(YDL_OPTIONS) as ydl:
                    info = ydl.extract_info(song_queue[0], download=False)

                URL = info['formats'][0]['url']

                if not voice_client.is_playing():
                    voice_client.play(discord.FFmpegPCMAudio(executable=settings['ffmpeg_path'], source = URL, **FFMPEG_OPTIONS), after=lambda e: playNext(ctx))


@bot.command()
async def pause(ctx):
    """Pause song"""
    if ctx.channel.name == settings['bot_channel_name']:
        global bans

        for ban in bans:
            if ban == f"{ctx.message.author.id}":
                return await ctx.send(f'Fuck you, {ctx.message.author.mention}! <:gachiFU:998171613247848448>')
        else:
            global skipBans

            for ban in skipBans:
                if ban == f"{ctx.message.author.id}":
                    return await ctx.send(f'Fuck you, {ctx.message.author.mention}! <:gachiFU:998171613247848448>')
            else:
                voice = get(bot.voice_clients, guild=ctx.guild)

                if voice:
                    voice.pause()
                    user = ctx.message.author.mention
                    await ctx.send(f"YeASS sir {user}, song is paused. <:gachiSleeper:998171510990708817>")

@bot.command()
async def resume(ctx):
    """Resume song"""
    if ctx.channel.name == settings['bot_channel_name']:
        global bans

        for ban in bans:
            if ban == f"{ctx.message.author.id}":
                return await ctx.send(f'Fuck you, {ctx.message.author.mention}! <:gachiFU:998171613247848448>')
        else:
            global skipBans

            for ban in skipBans:
                if ban == f"{ctx.message.author.id}":
                    return await ctx.send(f'Fuck you, {ctx.message.author.mention}! <:gachiFU:998171613247848448>')
            else:
                voice = get(bot.voice_clients, guild=ctx.guild)

                if voice:
                    voice.resume()
                    user = ctx.message.author.mention
                    await ctx.send(f"Oh my master {user}, song resumed! <:gachiVan:998171539746861108>")

@bot.command()
async def skip(ctx):
    """Skip song"""
    if ctx.channel.name == settings['bot_channel_name']:
        global bans

        for ban in bans:
            if ban == f"{ctx.message.author.id}":
                return await ctx.send(f'Fuck you, {ctx.message.author.mention}! <:gachiFU:998171613247848448>')
        else:
            global skipBans

            for ban in skipBans:
                if ban == f"{ctx.message.author.id}":
                    return await ctx.send(f'Fuck you, {ctx.message.author.mention}! <:gachiFU:998171613247848448>')
            else:
                voice = get(bot.voice_clients, guild=ctx.guild)

                if voice:  
                    voice.pause()
                    playNext(ctx)

@bot.command()
async def addQueue(ctx, url):
    """Add song to queue"""
    if ctx.channel.name == settings['bot_channel_name']:
        global bans

        for ban in bans:
            if ban == f"{ctx.message.author.id}":
                return await ctx.send(f'Fuck you, {ctx.message.author.mention}! <:gachiFU:998171613247848448>')
        else:
            global song_queue

            try:
                song_queue.append(url)
                user = ctx.message.author.mention
                await ctx.send(f'``{url}`` Thank you sir {user}! I added your song to queue. <:gachiVan:998171539746861108>')
            except:
                await ctx.send(f"Couldnt add {url} to the queue!")

@bot.command()
async def removeQueue(ctx, number):
    """Remove song from queue"""
    if ctx.channel.name == settings['bot_channel_name']:
        global bans

        for ban in bans:
            if ban == f"{ctx.message.author.id}":
                return await ctx.send(f'Fuck you, {ctx.message.author.mention}! <:gachiFU:998171613247848448>')
        else:
            global skipBans

            for ban in skipBans:
                if ban == f"{ctx.message.author.id}":
                    return await ctx.send(f'Fuck you, {ctx.message.author.mention}! <:gachiFU:998171613247848448>')
            else:
                global song_queue

                try:
                    del(song_queue[int(number)])
                    if len(song_queue) < 1:
                        await ctx.send("Your queue is empty now! Now, I'm ready to cum! <:gachiVan:998171539746861108>")
                    else:
                        await ctx.send(f'Yeah, i did it! Now, swallow my cum <:gachiBASS:998171333127057428>: {song_queue}')
                except:
                    await ctx.send("<:gachiFU:998171613247848448> Fuck you!!! My laptop says this shit: List index out of range - the queue starts at 0! <:gachiFU:998171613247848448>")

@bot.command()
async def clearQueue(ctx):
    """Clear queue"""
    if ctx.channel.name == settings['bot_channel_name']:
        global bans

        for ban in bans:
            if ban == f"{ctx.message.author.id}":
                return await ctx.send(f'Fuck you, {ctx.message.author.mention}! <:gachiFU:998171613247848448>')
        else:
            global skipBans

            for ban in skipBans:
                if ban == f"{ctx.message.author.id}":
                    return await ctx.send(f'Fuck you, {ctx.message.author.mention}! <:gachiFU:998171613247848448>')
            else:
                global song_queue

                song_queue.clear()
                user = ctx.message.author.mention
                await ctx.send(f"Ohhh, thanks for free fisting {user} <:gachiBASS:998171333127057428>! Now, my ass is clean.")


@bot.command()
async def stop(ctx):
    """Stops and disconnects the bot from voice"""
    if ctx.channel.name == settings['bot_channel_name']:
        global bans

        for ban in bans:
            if ban == f"{ctx.message.author.id}":
                return await ctx.send(f'Fuck you, {ctx.message.author.mention}! <:gachiFU:998171613247848448>')
        else:
            global skipBans

            for ban in skipBans:
                if ban == f"{ctx.message.author.id}":
                    return await ctx.send(f'Fuck you, {ctx.message.author.mention}! <:gachiFU:998171613247848448>')
            else:
                await ctx.voice_client.disconnect()
                await ctx.send(f"Bye bye, my master! <:gachiSleeper:998171510990708817>")

@bot.command()
async def queue(ctx):
    """ outputs the queue """
    if ctx.channel.name == settings['bot_channel_name']:
        global bans

        for ban in bans:
            if ban == f"{ctx.message.author.id}":
                return await ctx.send(f'Fuck you, {ctx.message.author.mention}! <:gachiFU:998171613247848448>')
        else:
            for song in song_queue:
                await ctx.send(f'{song}')
            return await ctx.send(f"that's all")
            
# Youtube ends ###################################################

class Google(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def parse_google_card(self, node):
        if node is None:
            return None

        e = discord.Embed(colour=discord.Color.blue())

        # check if it's a calculator card:
        calculator = node.find(".//table/tr/td/span[@class='nobr']/h2[@class='r']")
        if calculator is not None:
            e.title = 'Calculator'
            e.description = ''.join(calculator.itertext())
            return e

        parent = node.getparent()

        # check for unit conversion card
        unit = parent.find(".//ol//div[@class='_Tsb']")
        if unit is not None:
            e.title = 'Unit Conversion'
            e.description = ''.join(''.join(n.itertext()) for n in unit)
            return e

        # check for currency conversion card
        currency = parent.find(".//ol/table[@class='std _tLi']/tr/td/h2")
        if currency is not None:
            e.title = 'Currency Conversion'
            e.description = ''.join(currency.itertext())
            return e

        # check for release date card
        release = parent.find(".//div[@id='_vBb']")
        if release is not None:
            try:
                e.description = ''.join(release[0].itertext()).strip()
                e.title = ''.join(release[1].itertext()).strip()
                return e
            except:
                return None

        # check for definition card
        words = parent.find(".//ol/div[@class='g']/div/h3[@class='r']/div")
        if words is not None:
            try:
                definition_info = words.getparent().getparent()[1]
            except:
                pass
            else:
                try:
                    e.title = words[0].text
                    e.description = words[1].text
                except:
                    return None
                for row in definition_info:
                    if len(row.attrib) != 0:
                        break
                    try:
                        data = row[0]
                        lexical_category = data[0].text
                        body = []
                        for index, definition in enumerate(data[1], 1):
                            body.append('%s. %s' % (index, definition.text))
                        e.add_field(name=lexical_category, value='\n'.join(body), inline=False)
                    except:
                        continue
                return e

        # check for translate card
        words = parent.find(".//ol/div[@class='g']/div/table/tr/td/h3[@class='r']")
        if words is not None:
            e.title = 'Google Translate'
            e.add_field(name='Input', value=words[0].text,  inline=True)
            e.add_field(name='Out', value=words[1].text,  inline=True)
            return e

        # check for "time in" card
        time_in = parent.find(".//ol//div[@class='_Tsb _HOb _Qeb']")
        if time_in is not None:
            try:
                time_place = ''.join(time_in.find("span[@class='_HOb _Qeb']").itertext()).strip()
                the_time = ''.join(time_in.find("div[@class='_rkc _Peb']").itertext()).strip()
                the_date = ''.join(time_in.find("div[@class='_HOb _Qeb']").itertext()).strip()
            except:
                return None
            else:
                e.title = time_place
                e.description = '%s\n%s' % (the_time, the_date)
                return e

        weather = parent.find(".//ol//div[@class='e']")
        if weather is None:
            return None

        location = weather.find('h3')
        if location is None:
            return None

        e.title = ''.join(location.itertext())

        table = weather.find('table')
        if table is None:
            return None

        try:
            tr = table[0]
            img = tr[0].find('img')
            category = img.get('alt')
            image = 'https:' + img.get('src')
            temperature = tr[1].xpath("./span[@class='wob_t']//text()")[0]
        except:
            return None
        else:
            e.set_thumbnail(url=image)
            e.description = '*%s*' % category
            e.add_field(name='Temperature', value=temperature)

        try:
            wind = ''.join(table[3].itertext()).replace('Wind: ', '')
        except:
            return None
        else:
            e.add_field(name='Wind', value=wind)

        try:
            humidity = ''.join(table[4][0].itertext()).replace('Humidity: ', '')
        except:
            return None
        else:
            e.add_field(name='Humidity', value=humidity)

        return e

    async def get_google_entries(self, query):
        params = {
            'q': query,
            'hl': 'en'
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64)'
        }
        entries = []
        card = None
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.google.com/search', params=params, headers=headers) as resp:
                if resp.status != 200:
                    raise RuntimeError('Google somehow failed to respond.')

                root = etree.fromstring(await resp.text(), etree.HTMLParser())
                card_node = root.find(".//div[@id='topstuff']")
                card = self.parse_google_card(card_node)
                search_nodes = root.findall(".//div[@class='g']")
                for node in search_nodes:
                    url_node = node.find('.//h3/a')
                    if url_node is None:
                        continue
                    url = url_node.attrib['href']
                    if not url.startswith('/url?'):
                        continue
                    url = parse_qs(url[5:])['q'][0]
                    entries.append(url)
        return card, entries

    # Google Command
    @commands.command(aliases=['google', 'G', 'Google'])
    async def g(self, ctx, *, query):
        """Google for whatever you like."""
        try:
            card, entries = await self.get_google_entries(query)
        except RuntimeError as e:
            await edit(ctx, content=str(e), ttl=3)
        else:
            if card:
                value = '\n'.join(entries[:3])
                if value:
                    card.add_field(name='Search Results', value=value, inline=False)
                return await edit(ctx, embed=card)
            if len(entries) == 0:
                return await edit(ctx, content='No results found... sorry.', ttl=3)
            next_two = entries[1:3]
            before = entries[0]
            before = before[:-1] + '%29' if before[-1] == ')' else before

            e = discord.Embed(colour=discord.Color.blue(), timestamp=datetime.datetime.now())
            e.set_author(name="Google Search", url="https://www.google.com/search?q=" + query.replace(" ", "+"), icon_url="https://cdn.discordapp.com/attachments/278603491520544768/300645219626647564/Google-logo-2015-G-icon.png")
            if next_two:
                formatted = '\n'.join(map(lambda x: '<%s>' % x, next_two))
                e.add_field(name="Search Result", value=before)
                e.add_field(name="More", value=formatted, inline=False)
            else:
                e.add_field(name="Search Result", value=before)
            await edit(ctx, embed=e)

    # Google Image Search (100 per day)
    @commands.command(aliases=["I", "image", "Image"])
    async def i(self, ctx, *, query):
        """Search for images on google."""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://www.googleapis.com/customsearch/v1?q=" + query.replace(' ', '+') + "&start=" + '1' + "&key=" + self.bot.google_api_key + "&cx=" + self.bot.custom_search_engine + "&searchType=image") as resp:
                if resp.status != 200:
                    await edit(ctx, content='Google somehow failed to respond.', ttl=3)
                result = json.loads(await resp.text())
                em = discord.Embed(colour=discord.Color.blue())
                if permEmbed(ctx.message):
                    link = result['items'][0]['link']
                    if ".gif?" in link:
                        link = result['items'][0]['link'].split(".gif?")[0] + ".gif"
                    await edit(ctx, content=None, embed=em.set_image(url=link))
                else:
                    await edit(ctx, content=result['items'][0]['link'])

@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))
    print('------')

    f = open("skipBans.dat", "r")
    for x in f:
        skipBans.append(x.rstrip("\n"))

    f = open("bans.dat", "r")
    for x in f:
        bans.append(x.rstrip("\n"))

    f = open("admins.dat", "r")
    for x in f:
        admins.append(x.rstrip("\n"))

bot.add_cog(Google(bot))

try:
    bot.run(settings['token'])
except discord.errors.HTTPException and discord.errors.LoginFailure as e:
    print("Login unsuccessful.")
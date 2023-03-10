from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}call':
        await message.channel.send("callback!")

@client.event
async def on_message(message):
    if message.content.startswith("!κ³μ’"):
        user = message.author
        if discord.utils.get(user.roles, name="π π π π‘ π‘ π π§"):
            await message.delete()
            embed = discord.Embed(description="**κ³μ’λ²νΈ : kλ±ν¬ 100 154 161775\n```μκΈν κΌ­ ν°μΌλ°©μ μκΈμλͺ μ μ΄μ£ΌμΈμ\nμκΈν μκΈμ¬μ§μ λ³΄λ΄μ£Όμλ©΄ κ°μ¬νκ² μ΅λλ€!```**".format(message.author.mention), color=0x00f7ff)
            await message.channel.send (embed=embed)
        else:
            await message.delete()
            embed = discord.Embed(colour=discord.Colour.blue(), description="**λΉμ μ κ·Έ λͺλ Ήμ μ¬μ©ν  μ μμ΅λλ€!**", timestamp=datetime.datetime.now(pytz.timezone('UTC')),)
            embed.set_footer(text="Bot Made by : RANI#0001", icon_url="https://i.imgur.com/O1e5tbE.jpg")            
            await message.channel.send(embed=embed)
  
    if message.content.startswith("!νμ΄ν"):
        user = message.author
        if discord.utils.get(user.roles, name="π π π π‘ π‘ π π§"):
            await message.delete()
            embed = discord.Embed(description="**paypal email : ansh6647@naver.com\n```Caution: Please send to Family Friend.\nIf not, the refund will be processed automatically.\nPlease send the money as Friend so there is no frozen,\nand please take a picture after purchase```**".format(message.author.mention), color=0x00f7ff)
            await message.channel.send (embed=embed)
        else:
            await message.delete()
            embed = discord.Embed(colour=discord.Colour.blue(), description="**You cannot use that command!**", timestamp=datetime.datetime.now(pytz.timezone('UTC')),)
            embed.set_footer(text="Bot Made by : RANI#0001", icon_url="https://i.imgur.com/O1e5tbE.jpg")            
            await message.channel.send(embed=embed)
  
    if message.content.startswith("!μ²­μ"):
        user = message.author
        if discord.utils.get(user.roles, name="π π π π‘ π‘ π π§"):
            ch = client.get_channel(969171860556238878)
            amount = message.content[4:]
            await message.delete()
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="λ©μμ§ μ­μ  μλ¦Ό", description="λ©μΈμ§ {}κ°κ° μ­μ λμμ΅λλ€.".format(amount), color=0x000000)
            embed.set_footer(text="Bot Made by : RANI#0001", icon_url="https://i.imgur.com/O1e5tbE.jpg")
            await message.channel.send(embed=embed)

            a = message.author
            embed2 = discord.Embed(title = f"[ {message.guild.name} ] μ²­μ λ‘κ·Έ", description = f"\n **{a}** κ΄λ¦¬μλμ΄ μ²­μ λͺλ Ήμ΄λ₯Ό μ¬μ©νμ΅λλ€.", color=0x00f7ff)
            await ch.send (embed = embed2)  
        else:
            await message.delete()
            embed = discord.Embed(colour=discord.Colour.blue(), description="**λΉμ μ κ·Έ λͺλ Ήμ μ¬μ©ν  μ μμ΅λλ€!**", timestamp=datetime.datetime.now(pytz.timezone('UTC')),)
            embed.set_footer(text="Bot Made by : RANI#0001", icon_url="https://i.imgur.com/O1e5tbE.jpg")            
            await message.channel.send(embed=embed)
        
    if message.content.startswith("!μ§κΈ"):
        user = message.author
        mention = message.author.mention
        author = message.guild.get_member(message.mentions[0].id)
        if discord.utils.get(user.roles, name="π π π π‘ π‘ π π§"):
            await message.delete()
            role = discord.utils.get(message.guild.roles, name="π° π½ π π π π")
            await message.mentions[0].add_roles(role)
            embed = discord.Embed(title="κ²°μ  νμΈ μλ£ Payment confirmation completed", description="**νκ·Έ ν΄λλ¦¬λ©΄ 609μλ² νμ° N μΌλ‘ μμ£ΌμΈμ.\nν°μΌμ μΈκ²μ λ λ λ²¨ λΆνλλ¦½λλ€\n\nIf I tag you please come to e609 Volcanic N\nSEND ME YOUR IG NAME AND LV**", clolor=0x00f7ff)
#            embed = discord.Embed(title="κ΅¬λ§€μ μ­ν  μ§κΈ", description="**μ­ν μ§κΈμ΄ μ μμ μΌλ‘ μ²λ¦¬ λμμ΅λλ€.\n λ΄λΉμ : " + str(mention) + "\n κ΅¬λ§€μ μ§κΈ μ μ  : <@" + str(message.mentions[0].id) + "> \n\nμ ν¬μ΅ μμ κ΅¬λ§€μ£Όμμ κ°μ¬ν©λλ€!:heart_eyes:**", clolor=0x00f7ff)
            embed.set_thumbnail(url="https://i.imgur.com/O1e5tbE.jpg")
            await message.channel.send (embed=embed)
        else:
            embed = discord.Embed(colour=discord.Colour.blue(), description="**λΉμ μ κ·Έ λͺλ Ήμ μ¬μ©ν  μ μμ΅λλ€!**", timestamp=datetime.datetime.now(pytz.timezone('UTC')),)
            embed.set_footer(text="Bot Made by : RANI#0001", icon_url="https://i.imgur.com/O1e5tbE.jpg")            
            await message.channel.send(embed=embed)    
        
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")

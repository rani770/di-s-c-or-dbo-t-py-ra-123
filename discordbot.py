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
    if message.content.startswith("!계좌"):
        user = message.author
        if discord.utils.get(user.roles, name="👑 𝙎 𝙚 𝙡 𝙡 𝙚 𝙧"):
            await message.delete()
            embed = discord.Embed(description="**계좌번호 : k뱅크 100 154 161775\n```입금후 꼭 티켓방에 입금자명 적어주세요\n입금후 입금사진을 보내주시면 감사하겠습니다!```**".format(message.author.mention), color=0x00f7ff)
            await message.channel.send (embed=embed)
        else:
            await message.delete()
            embed = discord.Embed(colour=discord.Colour.blue(), description="**당신은 그 명령을 사용할 수 없습니다!**", timestamp=datetime.datetime.now(pytz.timezone('UTC')),)
            embed.set_footer(text="Bot Made by : RANI#0001", icon_url="https://i.imgur.com/O1e5tbE.jpg")            
            await message.channel.send(embed=embed)
  
    if message.content.startswith("!페이팔"):
        user = message.author
        if discord.utils.get(user.roles, name="👑 𝙎 𝙚 𝙡 𝙡 𝙚 𝙧"):
            await message.delete()
            embed = discord.Embed(description="**paypal email : ansh6647@naver.com\n```Caution: Please send to Family Friend.\nIf not, the refund will be processed automatically.\nPlease send the money as Friend so there is no frozen,\nand please take a picture after purchase```**".format(message.author.mention), color=0x00f7ff)
            await message.channel.send (embed=embed)
        else:
            await message.delete()
            embed = discord.Embed(colour=discord.Colour.blue(), description="**You cannot use that command!**", timestamp=datetime.datetime.now(pytz.timezone('UTC')),)
            embed.set_footer(text="Bot Made by : RANI#0001", icon_url="https://i.imgur.com/O1e5tbE.jpg")            
            await message.channel.send(embed=embed)
  
    if message.content.startswith("!청소"):
        user = message.author
        if discord.utils.get(user.roles, name="👑 𝙎 𝙚 𝙡 𝙡 𝙚 𝙧"):
            ch = client.get_channel(969171860556238878)
            amount = message.content[4:]
            await message.delete()
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="메세지 {}개가 삭제되었습니다.".format(amount), color=0x000000)
            embed.set_footer(text="Bot Made by : RANI#0001", icon_url="https://i.imgur.com/O1e5tbE.jpg")
            await message.channel.send(embed=embed)

            a = message.author
            embed2 = discord.Embed(title = f"[ {message.guild.name} ] 청소 로그", description = f"\n **{a}** 관리자님이 청소 명령어를 사용했습니다.", color=0x00f7ff)
            await ch.send (embed = embed2)  
        else:
            await message.delete()
            embed = discord.Embed(colour=discord.Colour.blue(), description="**당신은 그 명령을 사용할 수 없습니다!**", timestamp=datetime.datetime.now(pytz.timezone('UTC')),)
            embed.set_footer(text="Bot Made by : RANI#0001", icon_url="https://i.imgur.com/O1e5tbE.jpg")            
            await message.channel.send(embed=embed)
        
    if message.content.startswith("!지급"):
        user = message.author
        mention = message.author.mention
        author = message.guild.get_member(message.mentions[0].id)
        if discord.utils.get(user.roles, name="👑 𝙎 𝙚 𝙡 𝙡 𝙚 𝙧"):
            await message.delete()
            role = discord.utils.get(message.guild.roles, name="BUYER")
            await message.mentions[0].add_roles(role)
            embed = discord.Embed(title="결제 확인 완료 Payment confirmation completed", description="**태그 해드리면 609서버 화산 N 으로 와주세요.\n티켓에 인게임 닉 레벨 부탁드립니다\n\nIf I tag you please come to e609 Volcanic N\nSEND ME YOUR IG NAME AND LV**", clolor=0x00f7ff)
#            embed = discord.Embed(title="구매자 역할 지급", description="**역할지급이 정상적으로 처리 되었습니다.\n 담당자 : " + str(mention) + "\n 구매자 지급 유저 : <@" + str(message.mentions[0].id) + "> \n\n저희샵 에서 구매주셔서 감사합니다!:heart_eyes:**", clolor=0x00f7ff)
            embed.set_thumbnail(url="https://i.imgur.com/O1e5tbE.jpg")
            await message.channel.send (embed=embed)
        else:
            embed = discord.Embed(colour=discord.Colour.blue(), description="**당신은 그 명령을 사용할 수 없습니다!**", timestamp=datetime.datetime.now(pytz.timezone('UTC')),)
            embed.set_footer(text="Bot Made by : RANI#0001", icon_url="https://i.imgur.com/O1e5tbE.jpg")            
            await message.channel.send(embed=embed)    
        
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")

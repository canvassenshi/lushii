import discord
import os
import random
import json
import string
import asyncio 
import requests 
from bs4 import BeautifulSoup as bs 
from discord.ext import commands

class Fun(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def reply(self, ctx, *, question):
		responses = ['yes','no','maybe']
		await ctx.send(f'**Q: {question}\nA: {random.choice(responses)}**')

	@commands.command(aliases = ['gay','faggy'])
	async def gayrate(self, ctx, member:discord.Member = None):

		member = member or ctx.author

		gayrate = random.randint(0,100)
		loading_message = await ctx.send('<a:thinkloading:729363436693094453> Calculating gayness..')
		await asyncio.sleep(3.8)
		await loading_message.edit(content = f'<:catbox:729165300200898560> You are **{gayrate}%** gay **{member.name}**')

	@commands.command(aliases = ['f'])
	async def F(self, ctx, *, text : commands.clean_content = None):

		if text == None:
			return False

		embed = discord.Embed(
			description = f'**Press F to pay respects for {text}**',
			color = discord.Color(0x98FB98)
		)
		embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/729823594133061692/732432845569523802/fforrespects.gif')
		press_f = await ctx.send(embed = embed)
		await press_f.add_reaction(emoji=':bredF:731714799750086706')

	@commands.command()
	async def pat(self,ctx,member:discord.Member,text:commands.clean_content = None):

		gif = ['https://media.discordapp.net/attachments/729041541334564875/729777634409578616/babypat.gif', 
		   'https://cdn.discordapp.com/attachments/733484817907187813/753359685452693614/pat1.gif', 
		   'https://cdn.discordapp.com/attachments/733484817907187813/753359748220583936/pat2.gif',
		   'https://cdn.discordapp.com/attachments/733484817907187813/753359755375804436/pat3.gif',
		   'https://cdn.discordapp.com/attachments/733484817907187813/753359757313704064/pat4.gif',
		   'https://cdn.discordapp.com/attachments/733484817907187813/753359760409231400/pat5.gif'
		  ]

		embed = discord.Embed(
			title = 'AYYY',
			description = f'{ctx.author.mention} **pats** {member.mention}',
			color = discord.Color(0xFFC0CB)
		)
		embed.set_footer(text = '')
		embed.set_image(url = random.choice(gif) )

		await ctx.send(embed = embed)


	@commands.command()
	async def hug(self,ctx,member:discord.Member,text:commands.clean_content = None):

		gif = ['https://cdn.discordapp.com/attachments/729041541334564875/729790801344725002/hugspam.gif',
		   'https://cdn.discordapp.com/attachments/729041541334564875/729791392473415770/crushinghug.gif',
		   'https://cdn.discordapp.com/attachments/729041541334564875/729791400958230617/kawaiihug.gif',
		   'https://media.discordapp.net/attachments/729041541334564875/729791478964158584/cutehug.gif',
		   'https://cdn.discordapp.com/attachments/729041541334564875/729791479026942062/jikookbackhug.gif',
		   'https://cdn.discordapp.com/attachments/729041541334564875/729791479588847666/pewdsmarzibackhug.gif',
		   'https://media.discordapp.net/attachments/729041541334564875/729791479643635752/comfyhug.gif'
		  ]

		embed = discord.Embed(
			title = 'AYYY',
			description = f'{ctx.author.mention} **hugs** {member.mention}',
			color = discord.Color(0xFAFAD2)
		)
		embed.set_footer(text = '')
		embed.set_image(url = random.choice(gif))

		await ctx.send(embed = embed)

	@commands.command()
	async def cuddle(self,ctx,member:discord.Member,text:commands.clean_content = None):

		gif = ['https://cdn.discordapp.com/attachments/733484817907187813/753360845920141511/cuddle1.gif',
		   'https://cdn.discordapp.com/attachments/733484817907187813/743868145399365823/wuvcuddle.gif',
		   'https://cdn.discordapp.com/attachments/733484817907187813/753360887896866864/cuddle5.gif',
		   'https://cdn.discordapp.com/attachments/733484817907187813/753360911112208514/cuddle4.gif',
		   'https://cdn.discordapp.com/attachments/733484817907187813/753360943987163186/cuddle2.gif',
		   'https://cdn.discordapp.com/attachments/733484817907187813/753360944414982195/cuddle3.gif'
		  ]

		embed = discord.Embed(

			title = 'AYYY',
			description= f'{ctx.author.mention} **cuddles** {member.mention}',
			color = discord.Color(0x00FFFF) 
		)
		
		embed.set_image(url = random.choice(gif))

		await ctx.send(embed = embed)

	@commands.command()
	async def foreheadkiss(self,ctx,member:discord.Member,text:commands.clean_content = None):

		embed = discord.Embed(
			title = '',
			description = f'{ctx.author.mention} **kissed you on the forehead** {member.mention}',
			color = discord.Color(0xFF1493)
		)
		embed.set_image(url = 'https://media.discordapp.net/attachments/729823594133061692/730675791909748797/foreheadkiss.gif')

		await ctx.send(embed = embed)



def setup(client):
	client.add_cog(Fun(client))
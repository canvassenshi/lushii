import discord
import requests
import asyncio
from bs4 import BeautifulSoup as bs 
from discord.ext import commands

class Server(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.guild_only()
	async def user(self, ctx, *, member:discord.Member = None):

		member = member or ctx.author
		join_date = member.joined_at.strftime('%b %d, %Y %H:%M %p')
		account_date = member.created_at.strftime('%b %d, %Y %H:%M %p')

		embed = discord.Embed(
			color = discord.Color(0x98FB98)
		)
		embed.set_thumbnail(url=ctx.guild.icon_url)
		embed.set_author(name=f'{member.name} | {member.id}', icon_url=member.avatar_url)
		embed.add_field(name='Join Date:', value=f'**{join_date}**', inline = True)
		embed.add_field(name ='Created Account:', value=f'**{account_date}**', inline = False)
		embed.add_field(name='Server:', value=f'**{ctx.guild.name}**', inline = True)
		embed.add_field(name='Role: ', value=member.top_role.mention, inline = True)
		embed.add_field(name='Tag:', value=f'**{member}**', inline = True)

		await ctx.send(embed = embed)


	@commands.command()
	async def ping(self, ctx):
		await ctx.send(f'My ping is **{round(self.client.latency * 1000)}ms**')

	@commands.command()
	@commands.guild_only()
	async def avatar(self, ctx, *, avamember : discord.Member = None):
		avamember = avamember or ctx.author 
		userAvatarUrl = avamember.avatar_url
		embed = discord.Embed(
			title = f"**{avamember.name}'s avatar**",
			color = discord.Color(0x66CDAA)
	    )
		embed.set_image(url = f'{userAvatarUrl}')

		await ctx.send(embed = embed)

	@commands.command()
	@commands.guild_only()
	async def server(self, ctx):

		if (ctx.guild.id == 704165535226527765): #going-merry-server
			text_ch = ctx.guild.text_channels
			length = len(text_ch) 

			roles = ctx.guild.roles 
			b = len(roles) - 1

			server_date = ctx.guild.created_at.strftime('%b %d, %Y')
			region = str(ctx.guild.region)

			embed = discord.Embed(
				color = discord.Color(0x66CDAA)
			)
			embed.set_thumbnail(url = ctx.guild.icon_url)
			embed.add_field(name='Server: ', value=ctx.guild.name, inline = True)
			embed.add_field(name= 'Owner:', value='dawnu#2265', inline = True)
			embed.add_field(name = 'Created on:', value=server_date, inline = True)
			embed.add_field(name = f'Members:', value=ctx.guild.member_count, inline = True)
			embed.add_field(name = f'Text Channels:', value=length, inline = True)
			embed.add_field(name = f'Roles:', value=b, inline = True)
			embed.add_field(name='Server Region:', value=region.capitalize(), inline = True)

			await ctx.send(embed = embed)
		else:
			text_ch = ctx.guild.text_channels
			length = len(text_ch) 

			roles = ctx.guild.roles 
			b = len(roles) - 1

			server_date = ctx.guild.created_at.strftime('%b %d, %Y')
			region = str(ctx.guild.region)

			embedd = discord.Embed(
				color = discord.Color(0x66CDAA)
			)
			embedd.set_thumbnail(url = ctx.guild.icon_url)
			embedd.add_field(name='Server: ', value=ctx.guild.name, inline = True)
			embedd.add_field(name= 'Owner:', value=ctx.guild.owner, inline = True)
			embedd.add_field(name = 'Created on:', value=server_date, inline = True)
			embedd.add_field(name = f'Members:', value=ctx.guild.member_count, inline = True)
			embedd.add_field(name = f'Text Channels:', value=length, inline = True)
			embedd.add_field(name = f'Roles:', value=b, inline = True)
			embedd.add_field(name='Server Region:', value=region.capitalize(), inline = True)


			await ctx.send(embed = embedd)

def setup(client):
	client.add_cog(Server(client))
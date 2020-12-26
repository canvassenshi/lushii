import discord
from discord.ext import commands

class Reactions(commands.Cog):

	def __init__(self, client):
		self.client = client 


	@commands.command()
	async def no(self, ctx):
		embed = discord.Embed(
			title = f'{ctx.author.name} dislikes the idea',
			color = discord.Color.red()
		)
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/733484817907187813/743923225997869126/no.gif')

		await ctx.send(embed = embed)

	@commands.command()
	async def sleepy(self, ctx):
		embed = discord.Embed(
			title = f'{ctx.author.name} is sleeeeepppy',
			color = discord.Color(0x66CDAA)
		)
		embed.set_image(url = 'https://media.discordapp.net/attachments/729823594133061692/730194375904329788/sleepy.gif')

		await ctx.send(embed = embed)

	@commands.command(aliases = ['cry','doha'])
	async def crie(self, ctx):
		embed = discord.Embed(
			title = f'{ctx.author.name} is crying.. give them pats everyone!',
			color = discord.Color(0xB0C4DE)
		)
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/733484817907187813/743922839098490978/needy.gif')

		await ctx.send(embed = embed)

	@commands.command()
	async def scary(self, ctx):
		embed = discord.Embed(
			title = f'{ctx.author.name} is scared.. cuddle them now!',
			color = discord.Color(0x98FB98)
		)
		embed.set_image(url = 'https://media.discordapp.net/attachments/729823594133061692/730194385567744060/scared.gif')

		await ctx.send(embed = embed)

	@commands.command()
	async def want(self, ctx, text:commands.clean_content = None):
		embed = discord.Embed(
			title = f'{ctx.author.name} makes the puppy eyes..',
			color = discord.Color(0xFF00FF)
		)
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/733484817907187813/743923236877893774/want.gif')

		await ctx.send(embed = embed)

	@commands.command(aliases = ['nani','dafuq'])
	async def whait(self, ctx):
		embed = discord.Embed(
			title = 'Wait.. what',
			description = '',
			color = discord.Color(0xE6E6FA) #lavender
		)
		embed.set_footer(text = '')
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/729041541334564875/729808086109388831/whut.gif')

		await ctx.send(embed = embed)

	@commands.command()
	async def ok(self, ctx):

		embed = discord.Embed(
			title = 'Ah.. Rejection..',
			color = discord.Color(0x00FFFF)
		)
		embed.set_image(url = 'https://media.discordapp.net/attachments/729823594133061692/730662575225831454/taemincrie.gif')

		await ctx.send(embed = embed)

	@commands.command()
	async def needy(self, ctx):
		embed = discord.Embed(
			title = f'{ctx.author.name} needs attention.. ',
			color = discord.Color(0x66CDAA)
		)
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/733484817907187813/743924234031726732/attention.gif')

		await ctx.send(embed = embed)



def setup(client):
	client.add_cog(Reactions(client))

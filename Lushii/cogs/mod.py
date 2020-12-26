import discord
import asyncio
from discord.ext import commands

class Mod(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.has_permissions(manage_messages = True)
	async def clear(self,ctx,amount = 5):
		await ctx.channel.purge(limit = amount)


	@commands.command()
	@commands.has_permissions(administrator = True)
	async def load(self, ctx, extension):
		self.client.load_extension(f'cogs.{extension}')

	@commands.command()
	@commands.has_permissions(administrator = True)
	async def reload(self, ctx, extension):
		try:
			self.client.reload_extension(f'cogs.{extension}')
			await ctx.send(f"**ー( ´ ▽ ` )ﾉ** -- 👌 reloaded -- **{extension}.py**")
		except Exception as e:
			await ctx.send(e)

	@commands.command()
	@commands.has_permissions(administrator = True)
	async def unload(self, ctx, extension):
		self.client.unload_extension(f'cogs.{extension}')

	@commands.command()
	@commands.has_permissions(administrator = True)
	async def mute(self, ctx, member:discord.Member, time):

		time_int = int(time[:-1])
		mute_role = discord.utils.get(ctx.guild.roles, name="Bad Child")

		if time.endswith('h'):
			""""""
		elif time.endswith('m'):
			""" """
		elif time.endswith('s'):
			"""" """
		else:
			await ctx.send("Use h/m/s for now..")

	@commands.command()
	@commands.has_permissions(administrator = True)
	async def canvas(self, ctx, time, *, content):
		time_int = int(time[:-1])
		if time.endswith('h'):
			hours = time_int*3600
			await ctx.send(f"{ctx.author.mention} okii, i will remind you in {time_int} hour(s)")
			await asyncio.sleep(hours)
			await ctx.send(f"{ctx.author.mention} WAKE UPPP **--->** {content} **<---**")


	@commands.command()
	async def msg(self, ctx, member:discord.Member, *, text):
		await member.send(text)

	@commands.command()
	async def spam(self, ctx, *, text):
		for i in range(10):
			await ctx.send(text)


def setup(client):
	client.add_cog(Mod(client))


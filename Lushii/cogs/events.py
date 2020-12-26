import discord
import asyncio
import datetime
import re
import string
from discord.ext import commands

class Events(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print(f'Logged in as the best baby in the world UwU\n-- {self.client.user.name} -- ')
		await self.client.change_presence(status = discord.Status.dnd, activity = discord.Game('with Plue uwu')) 

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			message = await ctx.send('Invalid, Use `[/help command name]`')
			message
			await message.delete(delay = 3)
		elif isinstance(error, commands.CommandOnCooldown):
			await ctx.send(f"On cooldown, try again in {error.retry_after:.2f} seconds.")
		elif isinstance(error, commands.CommandNotFound):
			pass


	@commands.Cog.listener()
	async def on_member_ban(self, guild, user):
		embed = discord.Embed(
			title = 'User Banned',
			description = f'{user}, got rekt from {guild}',
			color = discord.Color(0xB22222)
		)
		embed.set_thumbnail(url = user.avatar_url)
		embed.set_footer(text = f'USER ID = {user.id}')

		channel = guild.get_channel(704186481354473502)
		if channel is None:
			pass
		else:
			await channel.send(embed = embed)


	@commands.Cog.listener()
	async def on_member_join(self, member):

		embed = discord.Embed(
			title = 'User joined',
			description = f'{member}, joined the server!',
			color = discord.Color(0x00FF7F)
		)
		embed.set_thumbnail(url = member.avatar_url)
		embed.set_footer(text = f'USER ID = {member.id}')

		channel = member.guild.get_channel(738019438724513884)
		if channel is None:
			pass
		else:
			await channel.send(embed = embed)


	@commands.Cog.listener()
	async def on_member_remove(self, member):

		embed = discord.Embed(
			title = 'User left',
			description = f'{member}, left the server',
			color = discord.Color(0x00FF7F)
		)
		embed.set_thumbnail(url = member.avatar_url)
		embed.set_footer(text = f'USER ID = {member.id}')

		channel = member.guild.get_channel(738019438724513884)
		if channel is None:
			pass
		else:
			await channel.send(embed = embed)


	@commands.Cog.listener()
	async def on_member_unban(self, guild, user):
		embed = discord.Embed(
			title = 'User Un-Banned',
			description = f"{user}, bribed the admins to get un-banned from {guild}",
			color = discord.Color(0x00FF7F)
		)
		embed.set_thumbnail(url = user.avatar_url)
		embed.set_footer(text = f'USER ID = {user.id}')

		channel = guild.get_channel(704186481354473502)
		if channel is None:
			pass
		else:
			await channel.send(embed = embed)


	@commands.Cog.listener()
	async def on_message_delete(self, message):

		message_time = message.created_at.strftime('%b %d, %H:%M %p')

		
		msg = f"** **\n**❗️ __Message Deleted__**\nUser: {message.author}\nChannel: {message.channel.mention}\nMessage: {message.content}\n** **"

		channel = message.guild.get_channel(738019438724513884)
		if (message.author.bot == True):
			pass
		else:
			if channel is None:
				pass
			elif (len(message.attachments) >= 1):
				
				txt = str(message.attachments[0])
				split_list = re.split("\s", txt)
				link = split_list[3]
				new_link = re.sub("cdn", "media", link)
				new_link2 = re.sub("com", "net", new_link)
				end_point = len(new_link2) - 2
				
				msg_attachment = f"** **\n**❗️ __Message Deleted__**\nUser: {message.author}\nChannel: {message.channel.mention}\nMessage: {new_link2[5:end_point]}\n** **"

				await channel.send(msg_attachment)
			else:
				await channel.send(msg)

	@commands.Cog.listener()
	async def on_message_edit(self, before, after):
		
		msg = f"** **\n**🔨 __Message Edited__**\nUser: {before.author}\nChannel: {before.channel.mention}\n-------------------\nBefore: {before.content}\n-------------------\nAfter: {after.content}\n-------------------\n** **"


		channel = after.guild.get_channel(738019438724513884)
		if (before.author.bot == True):
			pass
		else:
			if channel is None:
				pass
			else:
				await channel.send(msg)

	@commands.Cog.listener()
	async def on_message(self, message):
		attachment = message.attachments
		user = message.author
		length = len(attachment)
		channel = message.guild.get_channel(704183585913176145)

		if (message.channel ==  channel) and (length <=0) and (user.bot == False) and (message.guild.id == 704165535226527765):
			await message.delete(delay = 2)
			warn = await message.channel.send(f"{user.mention} this is an **Image-Only** channel.")
			await warn.delete(delay = 2)
		elif re.findall('nigger', message.content):
			await message.delete()
		else:
			pass



def setup(client):
	client.add_cog(Events(client))
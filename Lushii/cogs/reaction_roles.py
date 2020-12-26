import discord
import json
from discord.ext import commands

class ReactionRole(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_raw_reaction_add(self, payload):

		message_id = payload.message_id

		if message_id == 759957317612863541 or message_id == 759963924190986241:
			guild_id = payload.guild_id
			guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

			if str(payload.emoji) == '♀️':
				role1, role2 = discord.utils.get(guild.roles, name='Gorl'), discord.utils.get(guild.roles, name='Boi' )
			elif str(payload.emoji) == '♂️':
				role1, role2 = discord.utils.get(guild.roles, name='Boi'), discord.utils.get(guild.roles, name='Gorl' )
			elif str(payload.emoji) == '🏷':
				role = discord.utils.get(guild.roles, name='announcement')
			elif str(payload.emoji) == '🎏':
				role = discord.utils.get(guild.roles, name='events')
				
			member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)

			if member and str(payload.emoji) in ['♀️', '♂️']:
				await member.add_roles(role1)
				await member.remove_roles(role2)
			elif member and str(payload.emoji) in ['🏷','🎏']:
				await member.add_roles(role)
			
	
	@commands.Cog.listener()
	async def on_raw_reaction_remove(self, payload):

		message_id = payload.message_id

		if message_id == 759957317612863541 or message_id == 759963924190986241:
			guild_id = payload.guild_id
			guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

			if str(payload.emoji) == '♀️':
				role = discord.utils.get(guild.roles, name='Gorl')
			elif str(payload.emoji) == '♂️':
				role = discord.utils.get(guild.roles, name='Boi')
			elif str(payload.emoji) == '🏷':
				role = discord.utils.get(guild.roles, name='announcement')
			elif str(payload.emoji) == '🎏':
				role = discord.utils.get(guild.roles, name='events')
				
			member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)

			if member:
				await member.remove_roles(role)

	@commands.Cog.listener()
	async def on_reaction_add(self, reaction, user):

		channel = user.guild.get_channel(744332402406719530)

		if channel is None:
			pass
		else:
			if (reaction.emoji) == "♀️":
				await reaction.message.remove_reaction("♂️", user)
			elif (reaction.emoji) == "♂️":
				await reaction.message.remove_reaction("♀️", user)



def setup(client):
	client.add_cog(ReactionRole(client))
import discord
from discord.ext import commands
import json

path = "C:\\Users\\ivarn\\Desktop\\Lushii\\cogs\\db"

class Tags(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def createtag(self, ctx, name, *, content):

		d = {}
		d[f"{name}"] = f"{content}"

		with open(f"{path}\\tags.json") as f:
			data = json.load(f)

		key_names = []
		for key,value in data.items():
			key_names.append(key)

		if (name in key_names):
			await ctx.send(f"Tag name **{name}** is taken..")
		else:
			data.update(d)

			with open(f"{path}\\tags.json", "w") as f:
				json.dump(data,f, indent = 4)

			await ctx.send(f"Tag **{name}** has been created.")

		key_names.clear()


	@commands.command(aliases = ["t"])
	async def tag(self, ctx, name):

		with open(f"{path}\\tags.json") as f:
			data = json.load(f)

		key_names = []
		for key,value in data.items():
			key_names.append(key)

		if (name in key_names):
			await ctx.send(data[f"{name}"])
		else:
			await ctx.send(f"Tag **{name}** is not found")

		key_names.clear()


	@commands.command()
	async def edittag(self, ctx, name, *, content):

		d = {}
		d[f"{name}"] = f"{content}"

		with open(f"{path}\\tags.json") as f:
			data = json.load(f)

		key_names = []
		for key,value in data.items():
			key_names.append(key)

		if (name in key_names):
			data.update(d)

			with open(f"{path}\\tags.json", "w") as f:
				json.dump(data, f, indent = 4)

		await ctx.send(f"Tag **{name}**, successfully edited.")

		key_names.clear()

	@commands.command()
	async def deletetag(self, ctx, name):

		with open(f"{path}\\tags.json") as f:
			data = json.load(f)

		data.pop(f"{name}")

		with open(f"{path}\\tags.json", "w") as f:
			json.dump(data, f, indent = 4)

		await ctx.send(f"Tag **{name}** has been removed.")

	@commands.command()
	async def alltags(self, ctx):

		with open(f"{path}\\tags.json") as f:
			data = json.load(f)

		key_names = []

		for key,value in data.items():
			key_names.append(key)

		names = "\n".join(key_names) 
		await ctx.send(f"```{names}```")
		key_names.clear()
			 


def setup(client):
	client.add_cog(Tags(client))
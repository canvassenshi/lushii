import discord
import json
from discord.ext import commands

path = "C:\\Users\\ivarn\\Desktop\\Lushii\\cogs\\images"
GM = 704165535226527765

class Shop(commands.Cog):

	def __init__(self, client):
		self.client = client


	@commands.command()
	async def shop(self, ctx):

		user_id = str(ctx.author.id)

		supreme = discord.utils.get(ctx.guild.roles, name="Supreme Court")
		haki = discord.utils.get(ctx.guild.roles, name="Conqueror's Haki")

		embed = discord.Embed(
			title = "GM KIRA KIRA SHOP ヾ(｡･ω･)ｼ",
			description = f"{supreme.mention} -- 50,000 💎 -- `[/buy supreme]`\n{haki.mention} -- 80,000 💎 -- `[/buy haki]`",
			color = discord.Color(0xFFC0CB)
		)
		embed.set_image(url = "https://media.discordapp.net/attachments/710308975169634375/726218706077876234/divider.gif")

		if(ctx.guild.id == GM):
			await ctx.send(embed = embed)

	@commands.command()
	async def buy(self, ctx, *, role):

		user_id = str(ctx.author.id)
		user_name = str(ctx.author)

		supreme, sup_price = discord.utils.get(ctx.guild.roles, name="Supreme Court"), 50000
		haki, haki_price = discord.utils.get(ctx.guild.roles, name="Conqueror's Haki"), 80000

		d = {}

		with open(f"{path}\\moni.json") as f:
			data = json.load(f)

		d[user_id] = [user_name, data[user_id][1]]

		if (ctx.guild.id == GM):
			if (role == "supreme" and sup_price <= data[user_id][1]):
				await ctx.author.add_roles(supreme)

				d[user_id][1] = (data[user_id][1] - sup_price)
				data.update(d)
				with open(f"{path}\\moni.json", "w") as f:
					json.dump(data, f, indent = 4)

				await ctx.send("Role successfully purchased!")
			elif (role == "haki" and haki_price <= data[user_id][1]):
				await ctx.author.add_roles(haki)

				d[user_id][1] = (data[user_id][1] - haki_price)
				data.update(d)
				with open(f"{path}\\moni.json", "w") as f:
					json.dump(data, f, indent = 4)

				await ctx.send("Role successfully purchased!")
			else:
				await ctx.send("Check gems or the role name again..")


def setup(client):
	client.add_cog(Shop(client))

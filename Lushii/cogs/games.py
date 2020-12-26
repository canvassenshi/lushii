import discord
import random
import asyncio
import json
import re
from discord.ext import commands

path = "C:\\Users\\ivarn\\Desktop\\Lushii\\cogs\\db"
GM = 704165535226527765

class Games(commands.Cog):
	def __init__(self, client):
		self.client = client 


	@commands.command()
	async def createprofile(self, ctx):
		user_id = str(ctx.author.id)
		user_name = ctx.author.name 
		user_tag = str(ctx.author)

		d = {}
		d[user_id] = [user_tag, 2500]

		with open(f"{path}\\moni.json") as f:
			data = json.load(f)

		users = []
		for key,value in data.items():
			users.append(key)

		if (user_id in users):
			await ctx.send(f"**{user_name}**, game profile already exists.")
		else:
			data.update(d)
			with open(f"{path}\\moni.json", "w") as f:
				json.dump(data, f, indent = 4)
			await ctx.send(f"Your profile has successfully been created, **{ctx.author.name}**.\nAnd, **2500 💎** has been added to your account!")

		if ctx.guild.id == GM:
			role = discord.utils.get(ctx.guild.roles, name = 'GMG')
			await ctx.author.add_roles(role)
		else:
			pass

	@commands.command()
	async def profile(self, ctx, member:discord.Member = None):
		member = member or ctx.author

		member_id = str(member.id)
		member_name = member.name 

		with open(f"{path}\\moni.json") as f:
			data = json.load(f)

		users = []
		for key,value in data.items():
			users.append(key)

		embed = discord.Embed(
			title = f"{member_name} profile",
			color = discord.Color(0xFFC0CB)
		)
		embed.set_thumbnail(url = member.avatar_url)
		embed.add_field(name=f"** ヽ(　･∀･)ﾉ **", value=f"**Gems: {data[member_id][1]} 💎**", inline = True)
		embed.set_footer(text = f"{ctx.guild.name}", icon_url = ctx.guild.icon_url)

		if (member_id in users):
			await ctx.send(embed = embed)
		else:
			await ctx.send(f"**{ctx.author.name}**, create a profile first! use `/create_profile` command.")


	@commands.command()
	@commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
	async def slots(self, ctx, bet):

		user_id = str(ctx.author.id)
		user_name = str(ctx.author)

		with open(f"{path}\\moni.json") as f:
			data = json.load(f)

		bet_int = int(bet)

		emojis = '🍎🍊🍐🍋🍉🍇🍓🍒'
		a = random.choice(emojis)
		b = random.choice(emojis)
		c = random.choice(emojis)

		responses = ['amazing!', 'excellent!', 'you are on fire!']

		slotmachine = f"**[{a} {b} {c}]\n{ctx.author.name}**,"

		if (bet_int > 0):
			if bet_int in range(1,5001) and (bet_int <= data[user_id][1]):

				if (a==b==c):
					await ctx.send(f"{slotmachine} 3 in a row holy shi-, Take them out of the casino, you win <a:GMnani:705494493117415544> **{7*bet_int}** 💎!")
					
					profit = data[user_id][1] + 7*bet_int
					profit_func(data, profit, user_id, user_name)

				elif (a==b) or (a==c) or (b==c):
					await ctx.send(f"{slotmachine} 2 matches! {random.choice(responses)} you win <a:GMnani:705494493117415544> **{3*bet_int}** 💎!")
					
					profit = data[user_id][1] + 3*bet_int
					profit_func(data, profit, user_id, user_name)

				else:
					await ctx.send(f"{slotmachine} No match, you lost <a:GMPepeRainSad:705494501082529802>")
					
					loss = data[user_id][1] - bet_int
					loss_func(data, loss, user_id, user_name)
					
			elif bet_int not in range(1,5001):
				message = await ctx.send('Max Amount Limit is **5,000**')
				await message.delete(delay = 2)

			elif bet_int > data[user_id][1]:
				await ctx.send("You don't have that much gems in your account")


	@commands.command()
	@commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
	async def flip(self, ctx, choice, bet):

		user_id = str(ctx.author.id)
		user_name = str(ctx.author)

		with open(f"{path}\\moni.json") as f:
			data = json.load(f)

		bet_int = int(bet)
		sides = ['heads', 'tails']
		outcome = random.choice(sides)

		if bet_int > 0:
			if choice not in sides:
				await ctx.send('Invalid choice, choose **heads** or **tails**.')
			else:
				if bet_int in range(1,2501) and (bet_int <= data[user_id][1]):

					if (choice == outcome):
						await ctx.send(f'**{ctx.author.name}**, the coin landed on **{outcome}**, you win **{2*bet_int}** 💎!')

						profit = data[user_id][1] + 2*bet_int
						profit_func(data, profit, user_id, user_name)
					else:
						await ctx.send(f'**{ctx.author.name}**, the coin landed on **{outcome}**, you lose..')

						loss = (data[user_id][1] - bet_int)
						loss_func(data, loss, user_id, user_name)

				elif bet_int not in range(1,2501):
					message = await ctx.send('Max Amount Limit is **2,500**')
					await message.delete(delay = 2)

				elif bet_int > data[user_id][1]:
					await ctx.send("You don't have that much gems in your account")


	@commands.command()
	@commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
	async def shoot(self, ctx, bet):

		user_id = str(ctx.author.id)
		user_name = str(ctx.author)

		bet_int = int(bet)
		bullets = [0,0,0,1,1,0]
		random.shuffle(bullets)
		outcome = random.choice(bullets)

		with open(f"{path}\\moni.json") as f:
			data = json.load(f)

		if (bet_int > 0):
			if (bet_int in range(1,50001)) and (bet_int <= data[user_id][1]):

				if (outcome == 0):
					await ctx.send(f'**{ctx.author.name}**, you **died**, you shot yourself and you lost **{2*bet_int}** 💎')
					loss = (data[user_id][1] - 2*bet_int)
					loss_func(data, loss, user_id, user_name)
				else:
					await ctx.send(f'**{ctx.author.name}**, you lucky fuck, you are **safe**, here have **{4*bet_int}** 💎!! ')
					profit = data[user_id][1] + 4*bet_int
					profit_func(data, profit, user_id, user_name)

			elif bet_int not in range(1,50001):
				message = await ctx.send("Bet limit is **50,000**")
				await message.delete(delay = 3)

			elif bet_int > data[user_id][1]:
				await ctx.send("You don't have that much gems in your account")


	@commands.command()
	async def give(self, ctx, member:discord.Member, amount):

		user_id, user_name = str(ctx.author.id), str(ctx.author)
		member_id, member_name = str(member.id), str(member.name)
		amount_int = int(amount)

		with open(f"{path}\\moni.json") as f:
			data = json.load(f)

		d = {}
		d[user_id] = [user_name, data[user_id][1]]
		d[member_id] = [member_name, data[member_id][1]]

		if (user_id == member_id):
			await ctx.send("Fuck off be like mr beast")
		elif (amount_int <= 0):
			await ctx.send("What are you, feminist?")
		else:
			if (amount_int <= data[user_id][1]):

				d[member_id][1] = data[member_id][1] + amount_int 
				d[user_id][1] = data[user_id][1] - amount_int

				data.update(d)

				with open(f"{path}\\moni.json", "w") as f:
					json.dump(data, f, indent = 4)

				await ctx.send(f"**{member.name}**, you received **{amount}** 💎! from **{ctx.author.name}**")

			else:
				await ctx.send(f"**{ctx.author.name}**, you don't have enough gems to give")


	@commands.command()
	@commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
	async def roulette(self, ctx, bet):

		bet_int = int(bet)
		colors = "🔴🟢⚫"
		roulette_table = []

		game = f"**{ctx.author.name}, choose a color:\n🔴 : Red 2x \n🟢 : Green 12x\n⚫ : Black 2x**"

		with open(f"{path}\\moni.json") as f:
				data = json.load(f)

		for i in range(1,22):
			if i == 1:
				roulette_table.append(f"{i} 🟢 Green")
			elif i%2 == 0:
				roulette_table.append(f"{i} ⚫ Black")
			elif i%2 != 0:
				roulette_table.append(f"{i} 🔴 Red")

		color = random.choice(roulette_table)
	
		user_id = str(ctx.author.id)
		user_name = str(ctx.author)

		if bet_int > data[user_id][1] and bet_int in range(1,15001):
			await ctx.send("You don't have enough gems..")
		elif bet_int in range(1,15001):

			m = await ctx.send(game)
			for emoji in colors:
				await m.add_reaction(emoji)

			def check(reaction, user):
				return (
					reaction.emoji in colors
					and user == ctx.author
				)	

			try:
				reaction,user = await self.client.wait_for("reaction_add", timeout = 10, check = check)
			except asyncio.TimeoutError:
				await ctx.send("Timeout..")
			else:
				if bet_int in range(1,15001) and bet_int > 0:
					if(bet_int <= data[user_id][1]):
						msg = await ctx.send(f"Rolling.. you chose {reaction.emoji}")
						search_color = re.findall(f"{reaction.emoji}", color)

						await asyncio.sleep(2.5)

						if reaction.emoji in search_color and reaction.emoji == "🟢":
							await msg.edit(content = f"**{user.name}**, ball landed on **{color}**, you win **{12*bet_int}** 💎!")
							profit = data[user_id][1] + 12*bet_int
							profit_func(data, profit, user_id, user_name)

						elif reaction.emoji in search_color and reaction.emoji in ["⚫", "🔴"]:
							await msg.edit(content = f"**{user.name}**, the ball landed on **{color}** you win **{2*bet_int}** 💎!")
							profit = data[user_id][1] + 2*bet_int
							profit_func(data, profit, user_id, user_name)

						else:
							await msg.edit(content = f"**{user.name}**, you lose the ball rolled on **{color}**")
							loss = data[user_id][1] - bet_int
							loss_func(data, loss, user_id, user_name)
		elif bet_int <= 0:
			await ctx.send("Very nice, you idiot.")
		elif bet_int > 15000:
			await ctx.send("You can't bet more than **15,000**")


	@commands.command()
	async def leaderboard(self, ctx):

		with open(f"{path}\\moni.json") as f:
			data = json.load(f)

		dic = {}
		for key,value in data.items():
			dic[value[0]] = value[1]

		sorted_data = sorted(
			dic.items(), 
			key = lambda x : x[1], 
			reverse = True
		)
		
		lead_users, top_ten = [], []

		for i in sorted_data:
			lead_users.append(f"{i[0]} -- {i[1]} 💎")

		if len(lead_users) >= 10:
			for e in range(10):
				top_ten.append(f"{e+1}) {lead_users[e]}")

			names = "\n".join(top_ten)
			await ctx.send(f"**📈 Leaderboard**```css\n{names}```")
	
		elif  0 < len(lead_users) < 10:
			for e in range(len(lead_users)):
				top_ten.append(f"{e+1}) {lead_users[e]}"
					)
			names = "\n".join(top_ten)
			await ctx.send(f"**📈 Leaderboard**```css\n{names}```")

	@commands.command()
	@commands.cooldown(rate=1, per=300.0, type=commands.BucketType.user)
	async def beg(self, ctx):

		user_name, user_id = str(ctx.author), str(ctx.author.id)

		give = random.randint(50,600)

		with open(f"{path}\\moni.json") as f:
			data = json.load(f)

		d = {}
		d[user_id] = [user_name, data[user_id][1]]

		if 0 <= data[user_id][1] < 100:
			d[user_id][1] = data[user_id][1] + give
			data.update(d)
			with open(f"{path}\\moni.json", "w") as f:
				json.dump(data, f, indent = 4)
			await ctx.send(f"{ctx.author.mention}, here begger, i'll be your mr beast take **{give}** 💎")
		elif data[user_id][1] < 0:
			gamble_bad = random.randint(2500, 10001)
			d[user_id][1] = data[user_id][1] + gamble_bad
			data.update(d)
			with open(f"{path}\\moni.json", "w") as f:
				json.dump(data, f, indent = 4)
			await ctx.send(f'Get a life tf stop gambling, next time you gonna go to the ranch, anyway have **{gamble_bad}** 💎')
		else:
			await ctx.send(f"No fuck off.. ")

	@commands.command()
	async def numberguess(self, ctx, bet):

		user_id, user_name, bet_int = str(ctx.author.id), str(ctx.author), int(bet)

		numbers = []
		for number in range(1,16):
			numbers.append(str(number))

		bot_guess = (str(random.randint(1,15)))

		with open(f"{path}\\moni.json") as f:
			data = json.load(f)

		if bet_int > 0 and bet_int <= data[user_id][1] and bet_int in range(1,2501):
			i = 1
			already_guessed = []
			while i<=3:
				await ctx.send(f"```css\nGuess The Number (1-15) -- Tries Left: {4-i} -- {already_guessed} ```")
				def check(m):
					return(
						m.content in numbers
						and m.author == ctx.author
					)

				try:
					msg = await self.client.wait_for('message', timeout = 20, check=check)
				except asyncio.TimeoutError:
					await ctx.send("Timeout..")
				else:
					if bot_guess == msg.content and i==1:
						await ctx.send(f"First tryyyy.. are you black black widow? you get **{5*bet_int} 💎**")
						profit = data[user_id][1] + 5*bet_int
						profit_func(data, profit, user_id, user_name)
						break
					elif bot_guess == msg.content:
						await ctx.send(f"Mmmm, you found the number, here have **{3*bet_int} 💎**")
						profit = data[user_id][1] + 3*bet_int
						profit_func(data, profit, user_id, user_name)
						break
					elif bot_guess != msg.content and i==3:
						await ctx.send(f"Game over.. you suck at guessing lmfao, anyway the number is **{bot_guess}**")
						loss = data[user_id][1] - bet_int
						loss_func(data, loss, user_id, user_name)
					elif bot_guess != msg.content:
						bot_int, msg_int = int(bot_guess), int(msg.content)

						if bot_int < msg_int:
							await ctx.send("Try again.. it's a **lower** number")
						elif bot_int > msg_int:
							await ctx.send("Try again.. it's a **higher** number")
					already_guessed.append(f"{msg.content}")
				i = i+1
		else:
			await ctx.send("Not enough gesm.. yes **gesm** or invalid bet (max bet is **2500**), check balance.")


def setup(client):
	client.add_cog(Games(client))

def loss_func(data, loss, user_id, user_name):
	d={}
	d[user_id] = [user_name, loss]
	data.update(d)
	with open(f"{path}\\moni.json", "w") as f:
		json.dump(data, f, indent = 4)

def profit_func(data, profit, user_id, user_name):
	d={}
	d[user_id] = [user_name, profit]
	data.update(d)
	with open(f"{path}\\moni.json", "w") as f:
		json.dump(data, f, indent = 4)







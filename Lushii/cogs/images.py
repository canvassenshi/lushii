import discord
import os
import requests
import shutil
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from discord.ext import commands

path = "C:\\Users\\ivarn\\Desktop\\Lushii\\cogs\\images" 

class Images(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def image(self, ctx, *, text):  

		font = ImageFont.truetype("arial.ttf", 128)		
		w,h=font.getsize(text)
		x,y = (w+30, h+20)

		img = Image.new('RGBA', (x,y), (138, 58, 185))
		
		a = (x-w)/2
		b = (y-h)/2

		draw = ImageDraw.Draw(img)
		draw.text((a,b), text, font=font, fill='white') 

		saving = img.save(f"{path}\\{text}.png")
		await ctx.channel.send(file=discord.File(f"{path}\\{text}.png"))
		os.remove(f"{path}\\{text}.png") 
		

def setup(client):
	client.add_cog(Images(client))
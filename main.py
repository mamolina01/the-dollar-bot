#import urllib3
from config import discord_token
from grafico import getDollar
#import os
#import json
import discord
from discord.ext import commands



bot=commands.Bot(command_prefix="!",description="This is a testing bot") #Prefijo del bot

@bot.command(name="suma")
async def sumar(ctx,n1,n2):
    response=int(n1)+int(n2)
    await ctx.send(response)

@bot.command(name="multiplicacion")
async def multiplicacion(ctx,n1,n2):
    response=int(n1)*int(n2)
    await ctx.send(response)

@bot.command(name="dolar")
async def dollar(ctx,year_start,year_end):

        
    getDollar(int(year_start),int(year_end))
    response="C:/Users/mamolina/Desktop/Personal/Python/proyectos/bot Discord/grafico.png"
    try:
        await ctx.author.send(file=discord.File(response))
    except Exception as e:
        await ctx.send("Error "+e)

bot.run(discord_token)


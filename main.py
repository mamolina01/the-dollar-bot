from config import discord_token
from functions import *
import discord
from discord.ext import commands
from datetime import datetime

dia_actual=datetime.today().strftime('%d/%m/%Y')

bot=commands.Bot(command_prefix="/",description="This is a testing bot") #Prefijo del bot

@bot.command(name="getDollar")
async def getDollar(ctx,fecha=dia_actual):
    datos=getDollarDate(fecha) #Devuelve los datos en un vector [Valor dolar, Banco que lo provee]
    response=f"El valor del dolar oficial el día {fecha} es {datos[0]} y la información es obtenida del banco {datos[1]}"
    await ctx.send(response)

@bot.command(name="helpDollar")
async def help(ctx):
    response=f"""
    Hola!! Este bot sirve para consultar el valor del dolar :money_with_wings: 
:chart_with_upwards_trend: Para consultar la variación del valor del dolar a lo largo de los años utilizar el siguiente comando:
:point_right::skin-tone-1: /getDollarChart [año_inicio] [año_final] 
Ejemplo -> /getDollarChart 2003 2007
:warning: IMPORTANTE: Solo se pueden pasar años desde 2000 a 2022

:calendar_spiral: Para consultar el valor del dolar a día de hoy utilizar el siguiente comando: 
:point_right::skin-tone-1: /getDollar
En caso de que desees obtener el valor del dolar de un día especifico, enviarle también la fecha que desea.
:warning: Es MUY importante respetar el formato. dd/mm/aaaa :calendar_spiral: 
Ejemplo -> /getDollar 10/10/2015
    """
    await ctx.send(response)

@bot.command(name="getDollarChart")
async def getDollarChart(ctx,year_start,year_end):

    if (int(year_start)<2000 and int(year_start)<2022)or (int(year_end)<2000 and int(year_end)<2022):
        await ctx.send("Vuelva a ingresar un año mayor a los 2000 y menor al año actual")
    elif (int(year_start)>int(year_end)):
        await ctx.send("El primer año no puede ser mayor al segundo")
    else:
        getDollar(int(year_start),int(year_end))
        response="grafico.png"

        try:
            await ctx.author.send(file=discord.File(response))
        except Exception as e:
            await ctx.send("Error "+e)


bot.run(discord_token)


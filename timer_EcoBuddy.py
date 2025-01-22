import discord
from discord.ext import commands, tasks
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Declaramos el temporizador como una tarea de fondo
@tasks.loop(hours=24)  # Se ejecutará cada 24 horas
async def daily_timer(channel):
    if channel:
        await channel.send("Este es tu recordatorio diario de reciclar!!")

@daily_timer.before_loop
async def before_daily_timer():
    print("Esperando que el bot esté listo para iniciar el temporizador...")
    await bot.wait_until_ready()  # Asegura que el bot esté completamente conectado antes de iniciar el temporizador

# Comando para iniciar el temporizador
@bot.command()
async def timer(ctx):
    if not daily_timer.is_running():  # Verifica si el temporizador ya está corriendo
        await ctx.send("Temporizador de 24 horas iniciado.")
        daily_timer.start(ctx.channel)  # Inicia el temporizador en el canal actual
    else:
        await ctx.send("El temporizador ya está en ejecución.")

# Comando para detener el temporizador
@bot.command()
async def stoptimer(ctx):
    if daily_timer.is_running():  # Verifica si el temporizador está corriendo
        daily_timer.cancel()  # Detiene el temporizador
        await ctx.send("El temporizador se detuvo.")
    else:
        await ctx.send("El temporizador no está en ejecución.")

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f'Ocurrió un error: {error}')
    print(f'Error en el comando: {error}')
    

bot.run("token")

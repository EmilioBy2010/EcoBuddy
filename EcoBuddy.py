#codigo de Daniel
import discord
from discord.ext import commands
from juego import juegos

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("¡Hola! 🌍 Hoy puedes intentar reutilizar un frasco para organizar tus cosas. ¿Te animas? 🛠️ Si lo haces, comparte una foto y ganarás una medalla virtual. 🏅 ¡El planeta te lo agradecerá!")

@bot.command()
async def interesante(ctx):
    await ctx.send("¿Sabías que reciclar no solo ayuda al planeta, sino que también es una forma súper fácil de ser un héroe ambiental? 🌍 Cada botella de plástico que reciclas puede convertirse en algo nuevo, desde ropa hasta muebles. 🧴➡️🪑")

@bot.command()
async def soluciones(ctx):
    await ctx.send("puedes reutilizar tus cuadernos y darle un doble a las cosas y insistir a los demas a reutilizar")

@bot.command()
async def games(ctx):
    await ctx.send(juegos)

@bot.command()
async def opciones(ctx):
    await ctx.send("Reducir el uso de tu auto Utiliza el transporte público o camina o anda en bicicleta para trayectos cortos. Ahorrar agua Usa dos cubetas de agua para limpiar y enjuagar, y evita el desperdicio.  Apagar los dispositivos electrónicos Apaga los dispositivos cuando no los estés usando, como el celular o la computadora. ")

@bot.command()
async def joven(ctx):
    await ctx.send("Cerrar el grifo mientras te lavas los dientes, bañarte en 5 minutos, juntar el agua de la regadera mientras te bañas, son pequeñas acciones que ayudan a ahorrarla. Es importante separar los residuos en distintos botes: orgánica, vidrio, cartón, plásticos y desechos tóxicos.")

bot.run("token")

#codigo de Adam
import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import io

# Crear el bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Comando para generar una imagen
@bot.command()
async def reciclaje(ctx):
    # Crear una imagen con fondo verde
    img = Image.new('RGB', (500, 250), color=(34, 177, 76))  # Color verde
    draw = ImageDraw.Draw(img)

    # Usar una fuente estándar
    font = ImageFont.load_default()

    # Escribir un mensaje en la imagen
    mensaje = "¡Recicla y cuida el planeta!"
    textwidth, textheight = draw.textsize(mensaje, font=font)
    position = ((img.width - textwidth) // 2, (img.height - textheight) // 2)

    # Escribir el texto en la imagen
    draw.text(position, mensaje, font=font, fill=(255, 255, 255))

    # Crear un archivo de imagen en memoria
    with io.BytesIO() as image_binary:
        img.save(image_binary, 'PNG')
        image_binary.seek(0)

        # Enviar la imagen al canal de Discord
        await ctx.send("Aquí tienes tu mensaje de reciclaje:", file=discord.File(fp=image_binary, filename='reciclaje.png'))

# Comando de bienvenida
@bot.event
async def on_ready():
    print(f'Bot {bot.user} ha iniciado sesión correctamente en Discord!')
    
    # Enviar un mensaje de bienvenida al canal general
    general_channel = discord.utils.get(bot.get_all_channels(), name='general')
    if general_channel:
        await general_channel.send("¡Bienvenidos al servidor! Juntos podemos hacer un impacto positivo en el planeta. 🌍💚")

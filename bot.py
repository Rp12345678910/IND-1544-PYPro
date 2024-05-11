import discord

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$halo'):
        await message.channel.send(f"Hi,selamat datang {client.user}!")
    elif message.content.startswith('$bye'):
        await message.channel.send("semoga hari anda menyenangkan")
    elif message.content.startswith('$thank kuy'):    
        await message.channel.send("You're welcome")
    else:
        await message.channel.send(message.content)

client.run("MTIzNjU3OTY2MTU1MTYzMjQyNA.GOgaqO.HL2HAza32D4QFmMAHlyhVrDYdhajXeIkn140P0")

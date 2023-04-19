import os
import discord
from discord.ext import commands
import txtstr

#VARIABLES DE CONFIGURACION
token_dir = "discordSECRETS/token.txt"
PREFIX = "!"


#OBTENER INFORMACIÖN SECRETA
file_token = txtstr.readlines(token_dir)
token = file_token[0]


intents = discord.Intents.default().all()
intents.guild_reactions = True
intents.guild_messages = True
intents.messages = True
client = commands.Bot(command_prefix=PREFIX, intents=intents)





@client.command(pass_context=True)
async def userinfo(ctx, user_id):
    user = await client.fetch_user(user_id)
    print(user)
    print(user.display_avatar)
    await ctx.send("Hola")
    await ctx.send(user_id)




@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

client.run(token)


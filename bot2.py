import discord
import random
from discord.ext import commands
from Bot_logic2 import gen_pass
from Bot_logic2 import g_personagem

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(f'eu escolho {random.choice(choices)}')

@bot.command()
async def senha(ctx, tamanho = 8):
    await ctx.send(f'senha = {gen_pass(tamanho)}')

@bot.command(name="personagem")
async def comando_personagem(ctx, *, nome: str):
    resultado = g_personagem(nome)
    await ctx.send(resultado)


bot.run("Token")
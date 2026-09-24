from email.mime import image

import discord
from discord.ext import commands
from comandos import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def salvar(ctx):
    imagens = ctx.message.attachments

    for imagem in imagens:
        nome = imagem.filename

        await imagem.save(f"imagens/{nome}")
        await ctx.send("Imagem salva com sucesso!")


        classe = get_class(model = "keras_model.h5", label = "labels.txt", image = f"imagens/{nome}")
        await ctx.send(f"A classe da imagem é: {classe}")



        if classe == "Processador":
            await ctx.send("O processador é o cérebro do computador, responsável por executar cálculos e instruções.")
        elif classe == "Fonte":
            await ctx.send("A fonte converte e fornece energia elétrica para todos os componentes do computador.")
        elif classe == "Memoria RAM":
            await ctx.send("A memória RAM armazena temporariamente os dados dos programas que estão em execução.")
        elif classe == "Placa de video":
            await ctx.send("A placa de vídeo processa e renderiza imagens, gráficos e jogos.")
        elif classe == "Placa-mae":
            await ctx.send("A placa-mãe conecta e permite a comunicação entre todos os componentes do computador.")
        elif classe == "SSD":
            await ctx.send("O SSD armazena os dados do sistema e arquivos de forma rápida e permanente.")
        elif classe == "Water Cooler":
            await ctx.send("O water cooler utiliza líquido para resfriar o processador e manter as temperaturas baixas.")
        





bot.run("TOKEN")
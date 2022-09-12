import asyncio
import disnake
from disnake.ext import commands, tasks
from disnake import OptionChoice
from itertools import cycle

intents = disnake.Intents.all()

bot = commands.AutoShardedBot(shard_count=3, command_prefix=commands.when_mentioned_or(
    "!"), owner_ids=dev, intents=intents)
guild_list = bot.guilds


@bot.event
async def on_ready():
    print(f"[!] 다음으로 로그인에 성공했습니다.")
    print(f"[!] 다음 : {bot.user.name}")
    print(f"[!] 다음 : {bot.user.id}")

    change_status.start()


status = cycle(["봇 상태1","봇 상태2"])


@tasks.loop(seconds=3)
async def change_status():
    await bot.change_presence(activity=disnake.Game(next(status)))


@bot.slash_command(name="핑", description="핑을 측정합니다")
async def ping(inter: disnake.ApplicationCommandInteraction):
    await inter.response.defer(ephemeral=True)
    if round(bot.latency * 1000) <= 100:
        pl = '🔵'
    elif round(bot.latency * 1000) <= 150:
        pl = '🟢'
    elif round(bot.latency * 1000) <= 300:
        pl = '🟡'
    elif round(bot.latency * 1000) <= 500:
        pl = '🔴'
    else:
        pl = '🔴 error'
    await inter.followup.send(f"{pl}:{round(bot.latency * 1000)}ms")


@bot.slash_command(name="명령어 이름(띄어 쓰기 안됨)", description="명령어 설명")
async def 명령어이름(영어로) (inter: disnake.ApplicationCommandInteraction):


bot.run("봇 토큰")

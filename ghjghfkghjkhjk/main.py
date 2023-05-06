import disnake

from disnake.ext import commands

bot = commands.Bot(command_prefix="*", intents=disnake.Intents.all())


@bot.slash_command()
async def test(interaction: disnake.AppCmdInter):
    await interaction.send("тест")

bot.run("MTEwNDM4NjU3Mzg3ODk2ODM5Mg.GHYIUK.FIAKQJxO-rZ0uQmHXuH8U0xvA68J9MAhHSY3dI")
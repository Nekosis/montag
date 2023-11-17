import click
import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.all()
intents.bans = True
bot = commands.Bot(intents=intents)
server = 1174875776869478470


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.slash_command(
    name="incinerate",
    description="Bans a user loudly with an optional reason",
    guild_ids=[server],
)
async def incinerate(
    interaction: nextcord.Interaction,
    member: nextcord.Member,
    reason="No reason provided",
):
    role = nextcord.utils.get(interaction.guild.roles, name="Captain")
    if role in interaction.user.roles:
        await member.ban(reason=reason)
        await interaction.response.send_message(
            content=f"🔥 **@everyone: {member.name} has been banned for: {reason}**"
        )
    else:
        await interaction.send("Permission denied!")


@bot.slash_command(
    name="ping",
    description="Pong!",
    guild_ids=[server],
)
async def ping(
    interaction: nextcord.Interaction,
):
    await interaction.send("Pong!")


@click.command()
@click.option(
    "--token",
    help="The bot token to log in with.",
    default="redacted",
)
def main(token):
    bot.run(token)


if __name__ == "__main__":
    main()

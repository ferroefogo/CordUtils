import os
import nextcord
from nextcord.ext import commands
import config

def main():
    # init Intents to allow bots to interact with Members, Presence and Guilds
    intents = nextcord.Intents.all()
    client = commands.Bot(command_prefix=config.PREFIX, intents=intents, help_command=None)

    @client.event
    async def on_ready():
        print(f"{client.user.name} has connected to Discord.")
        await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.competing, name="bot development"))


    # load all cogs
    for folder in os.listdir("cogs"):
        if os.path.exists(os.path.join("cogs", folder, "cog.py")):
            client.load_extension(f"cogs.{folder}.cog")

    # run the bot
    client.run(config.BOT_TOKEN)


if __name__ == "__main__":
    main()

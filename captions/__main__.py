import logging

import os
import discord

logger = logging.getLogger(__name__)

bot = discord.Bot()

logger.debug("Starting Captions")


@bot.event
async def on_ready():
    logger.info("Logged in as %s", bot.user)


if __name__ == "__main__":
    if "DISCORD_BOT_TOKEN" not in os.environ:
        logger.critical("DISCORD_BOT_TOKEN is not set in the environment variables.")
    bot.run(os.environ["DISCORD_BOT_TOKEN"])

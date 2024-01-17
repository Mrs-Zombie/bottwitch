import os
import twitchio

# Configure Twitch
client = twitchio.Client()
client.set_access_token(os.getenv("TWITCH_ACCESS_TOKEN"))

# Définis les commandes du chatbot
@client.on("message")
async def on_message(event):
    # Réponds aux messages du chat
    if event.content.startswith("!salut"):
        await event.reply("Salut !")

# Lance le chatbot
client.run()

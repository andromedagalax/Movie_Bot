from pyrogram import Client, InlineKeyboardMarkup, InlineKeyboardButton
from FsBotz.bot import FsBotz

app = FsBotz# Replace "my_bot_token" with your actual bot token

@app.on_message
async def handle_message(client, message):
    if message.text == " Hello!":
        await message.reply_text("Hi! How are you?")
    elif message.text == "Channel":
        channel_link = "https://t.me/fs_moviez_channel"  # Replace with your channel link
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Join Channel", url=channel_link)]])
        await message.reply_text("Join our channel!", reply_markup=keyboard)

app.run()
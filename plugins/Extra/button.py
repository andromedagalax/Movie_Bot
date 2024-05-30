from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint
from FsBotz.bot import FsBotz

keyboard1 = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[[" Hello!", "Channel"]]  # List containing button labels
)

@FsBotz.message_handler()
async def kb_answer(message: types.Message):
    if message.text == '👋 Hello!':
        await message.reply("Hi! How are you?")
    elif message.text == 'Channel':
        await message.reply("https://t.me/fs_moviez_channel")
    else:
        await message.reply(f"Your message is: {message.text}")

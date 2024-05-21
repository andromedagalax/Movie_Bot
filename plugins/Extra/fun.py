from pyrogram import Client, filters
import os, re, json, base64, logging, random, asyncio
import time
from pyrogram import Client, filters, enums
from pyrogram.errors import ChatAdminRequired, FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import TOSS, DISE
from FsBotz.bot import FsBotz


# AESTHETIC------------ https://telegram.me/Josprojects ------------ #

def aesthetify(string):
    PRINTABLE_ASCII = range(0x21, 0x7f)
    for c in string:
        c = ord(c)
        if c in PRINTABLE_ASCII:
            c += 0xFF00 - 0x20
        elif c == ord(" "):
            c = 0x3000
        yield chr(c)


@FsBotz.on_message(
    filters.command(["ae"]))
async def aesthetic(client, message):
    status_message = await message.reply_text("...")
    text = "".join(str(e) for e in message.command[1:])
    text = "".join(aesthetify(text))
    await status_message.edit(text)

# EMOJI CONSTANTS
DART_E_MOJI = "🎯"
# EMOJI CONSTANTS


@FsBotz.on_message(
    filters.command(["throw", "dart"])
)
async def throw_dart(client, message):
    """ /throw an @AnimatedDart """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=DART_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )

logger = logging.getLogger(__name__)
BATCH_FILES = {}


async def toss(client, message):
    cap1="ᴛʜɪꜱ ɪꜱ ʏᴏᴜʀ ʀᴇꜱᴜʟᴛ"
    firos = await message.reply_sticker("CAACAgIAAxkBAAIVrmW44AABninrQsje8r0Nvl-EoJPn0AACvgkAAoSumEoSQwToTbAzsh4E") 
    time.sleep(3)
    await message.reply_photo(photo=random.choice(TOSS),caption=cap1)
    await firos.delete()

cap2="ᴛʜɪꜱ ɪꜱ ʏᴏᴜʀ ꜱᴄᴏʀᴇ"
@FsBotz.on_message(filters.command("dise")) 
async def roll_dice(client, message):
    rep_mesg_id = message.id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.id
    fs = await query.message.reply_text(f'🎲')
    await asyncio.sleep(1)
    await message.reply_photo(photo=random.choice(DISE),caption=cap2)
    await fs.delete()

# EMOJI CONSTANTS
TRY_YOUR_LUCK = "🎰"
# EMOJI CONSTANTS

@FsBotz.on_message(
    filters.command(["luck", "cownd"])
)
async def luck_cownd(client, message):
    """ /luck an @animatedluck """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=TRY_YOUR_LUCK,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )


# EMOJI CONSTANTS
GOAL_E_MOJI = "⚽"
# EMOJI CONSTANTS

@FsBotz.on_message(
    filters.command(["goal", "shoot"])
)
async def roll_dice(client, message):
    """ @Goal """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=GOAL_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )


import random

RUN_STRINGS = (
    "A broken of a demeanly filled with darkness \
    Why have you come to remind it ",
    "We have become the lives to be the underwater to the underwater that we do not know.",
    "You want the bad call ... but you need good thunder ....",
    "Oh Bloody Grama Virtues!",
    "Sea MUGGie I Am Going to Pay The Bill.",
    "Want with me!",
    "You are not a male chaff !!",
    "I locked it, and the good beach is done by the good beach.",
    "Kindi ... Kindi ...!",
    "Giving the stems and then showing one and show the ISI Mark",
    "Dayveyeese, Kingfisher ... Childe ...!.",
    "You have made your father for half of the midnight?",
    "This is the King of our work.",
    "I'm fetts to feed ...."
    "Mumak is every Bearby Kachyo ...",
    "Oh it moves it .... When we moves it ...",
    "The self of carpenter is the virtue of a carpenter.",
    "Why not to feel this intelligence in Da Vijaya ...!",
    "Where was this time ...."
    "Save me only ...."
    "I know his father's name is Bhavaniami ....",
    "Da Dasa ...",
    "Uppukam's English Salt Mongo Tree .....",
    "Children ..",
    "Your father to Paul ....",
    "Car Engine Out Completely .....",
    "This is the eye or magnety ...",
    "Before falling in the 4th pegging, I will arrive there.",
    "The drunk rains and wast ...."
    "To tell me I love Yo ...."
    "No, the Meenaka of Verbapur is not ....",
)


@FsBotz.on_message(
    filters.command("runs")
)
async def runs(_, message):
    """ /runs strings """
    effective_string = random.choice(RUN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)
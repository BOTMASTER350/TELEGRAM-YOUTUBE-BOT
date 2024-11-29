# ©️ STRIKERBOY

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/BOTMASTER350/TELEGRAM-YOUTUBE-BOT



from pyrogram import Client, filters
import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from Youtube.config import Config
from Youtube.script import Translation
from Youtube.forcesub import handle_force_subscribe


#########################

# Calculate current time greeting
currentTime = datetime.datetime.now()
if currentTime.hour < 12:
    wish = "Good morning 🌞"
elif 12 <= currentTime.hour < 18:
    wish = "Good afternoon 🌤️"
else:
    wish = "Good evening 🌝"




########################🎊 STRIKERBOY | BOTS 🎊######################################################
@Client.on_callback_query(filters.regex("cancel"))
async def cancel(client, callback_query):
    await callback_query.message.delete()

# About command handler
@Client.on_message(filters.private & filters.command("about"))
async def about(client, message):
    if Config.CHANNEL:
      fsub = await handle_force_subscribe(client, message)
      if fsub == 400:
        return
    await message.reply_text(
        text=Translation.ABOUT_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton('⛔️ Close', callback_data='cancel')]
        ]
    ))


# Start command handler
@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    if Config.CHANNEL:
      fsub = await handle_force_subscribe(client, message)
      if fsub == 400:
        return
    #user = message.from_user
    await message.reply_text(
        text=Translation.START_TEXT.format(message.from_user.first_name, wish),
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('📍 Update Channel', url='https://t.me/+6eDn6xs29i1mMWE0'),
            ],
            [
                InlineKeyboardButton('👩‍💻 Developer', url='https://t.me/Strikerboy350'),
                InlineKeyboardButton('👥 Support Group', url='https://t.me/+CGtwxtB6nwplYjZk'),
            ],
            [
                InlineKeyboardButton('⛔️ Close', callback_data='cancel')
            ]
        ]
    ))

# Help command handler
@Client.on_message(filters.command("help"))
async def help(client, message):
    help_text = """
Welcome to the STRIKERBOY YouTube Video Uploader Bot!

To upload a YouTube video, simply send me the YouTube link.

Enjoy using the bot!

©️ Channel : https://t.me/+6eDn6xs29i1mMWE0
    """
    await message.reply_text(help_text)


########################🎊 STRIKERBOY | BOTS 🎊######################################################

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>🤖 My Name :</b> <a href='https://http://t.me/AnimeKhazana_DL_Bot'>File Sharing Bot</a> \n<b>📝 Language :</b> <a href='https://python.org'>Python 3</a> \n<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram {__version__}</a> \n<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a> \n<b>📢 Channel :</b> <a href='https://t.me/+3maR-tIE0AA4N2E9'>Anime Khazana Encodes</a> \n<b>🧑‍💻 Developer :</b> <a href='tg://user?id={5009476236}'>『𝗠𝗔𝗗𝗔𝗥𝗔』</a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass





# 『𝗠𝗔𝗗𝗔𝗥𝗔』 
# Don't Remove Credit 🥺
# Telegram Channel @AnimeKhazanaEncodes
# Backup Channel @AnimeFlix07
# Developer @II_Madara_II

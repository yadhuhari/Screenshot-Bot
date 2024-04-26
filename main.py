from pyrogram import Client, filters
import random
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import ForceReply
from pyrogram.types import CallbackQuery

API_ID = "23050566"
API_HASH = "25e954ccd4afb778eea69bd6754275ff"
BOT_TOKEN = "7037015366:AAGsTNCQ4lwm_dcSuWauRrk6MWsnKRMzNtI"

BOT_DEVELOPER = "t.me/MR_HKZ_TG"
PICS = [
 "https://telegra.ph/file/28f4c97f0d1248873d4bd.jpg"
]

Bot = Client(
    name="ScreenshotBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@Bot.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=f"""Hᴇʟʟᴏ {message.from_user.mention} 👋,

I'ᴍ Sᴄʀᴇᴇɴsʜᴏᴛ Gᴇɴᴇʀᴀᴛᴏʀ Bᴏᴛ. I ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ sᴄʀᴇᴇɴsʜᴏᴛs ʏᴏᴜʀ ᴠɪᴅᴇᴏ ғɪʟᴇs. Fᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟs ᴄʜᴇᴄᴋ ʜᴇʟᴘ

Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ: [×͜× 𝙼𝚛. 𝙷𝙺𝚉 𝚃𝙶 🇮🇳࿐](t.me/MR_HKZ_TG)""",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 👨‍💻", url="t.me/MR_HKZ_TG"),
            InlineKeyboardButton("𝖴𝗉𝖽𝖺𝗍𝖾𝗌 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 🔰", url="t.me/HKZTG"),
            ],[
            InlineKeyboardButton("𝖲𝗈𝗎𝗋𝖼𝖾 𝖼𝗈𝖽𝖾 😎", url="t.me/MR_HKZ_TG"),
            ],[
            InlineKeyboardButton("𝖧𝖾𝗅𝗉 🛠", callback_data='help'),
            InlineKeyboardButton("𝖢𝗅𝗈𝗌𝖾 📛", callback_data='close') 
            ]]
            )
    )
     

@Bot.on_callback_query(
    filters.create(lambda _, __, query: query.data.startswith("mscht"))
)
async def _(c, m):
    await m.answer()
    dur = m.message.text.markdown.split("\n")[-1]
    await m.message.delete(True)
    await c.send_message(
        m.from_user.id,
        f"#manual_screenshot\n\n{dur}\n\nNow send your list of seconds separated by `,`(comma).\nEg: `0,10,40,60,120`."
        "\nThis will generate screenshots at 0, 10, 40, 60, and 120 seconds. \n\n"
        "1. The list can have a maximum of 10 valid positions.\n"
        "2. The position has to be greater than or equal to 0, or less than the video length in order to be valid.",
        reply_to_message_id=m.message.reply_to_message.message_id,
        reply_markup=ForceReply(),
    )    


print("Bot Started..!")
Bot.run()

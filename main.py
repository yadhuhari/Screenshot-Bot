from pyrogram import Client, filters
import random
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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
     
    


print("Bot Started..!")
Bot.run()

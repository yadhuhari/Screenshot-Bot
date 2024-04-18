from pyrogram import Client, filters
import random

API_ID = "23050566"
API_HASH = "25e954ccd4afb778eea69bd6754275ff"
BOT_TOKEN = "7037015366:AAGsTNCQ4lwm_dcSuWauRrk6MWsnKRMzNtI"

BOT_DEVELOPER = "https://t.me/HKZTG"
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
        photo=random.choice(PICS)
        caption=f"""Hᴇʟʟᴏ {m.from_user.mention} 👋,

I'ᴍ Sᴄʀᴇᴇɴsʜᴏᴛ Gᴇɴᴇʀᴀᴛᴏʀ Bᴏᴛ. I ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ sᴄʀᴇᴇɴsʜᴏᴛs ʏᴏᴜʀ ᴠɪᴅᴇᴏ ғɪʟᴇs. Fᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟs ᴄʜᴇᴄᴋ ʜᴇʟᴘ

Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ: (BOT_DEVELOPER)"""
    )


print("Bot Started..!")
Bot.run()

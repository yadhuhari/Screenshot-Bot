from pyrogram import Client, filters

API_ID = "23050566"
API_HASH = "25e954ccd4afb778eea69bd6754275ff"
BOT_TOKEN = "7037015366:AAGsTNCQ4lwm_dcSuWauRrk6MWsnKRMzNtI"

Bot = Client(
    name="ScreenshotBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
   )



print("Bot Started..!")

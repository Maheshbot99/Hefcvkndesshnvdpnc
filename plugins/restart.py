import os 
from pyrogram import Client, filters
from helper.database import botdata, find_one, total_user
from config import *
from helper.progress import humanbytes

botid = BOT_TOKEN.split(':')[0]

@Client.on_message(filters.private & filters.command(["rebot"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"**⌾  ʙᴏᴛ ɪꜱ ʀᴇꜱᴛᴀʀᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟy**",quote=True)

from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("22931657")
APP_HASH = os.environ.get("99a1a4f1494632847629b0eda328166e")
BOT_USERNAME = os.environ.get("Jsjejnejbot")
session = os.environ.get("1BJWap1sBu3aSB8eGT4ddh4FaopI2bozZ4wIEQW8M8Nz0r1sY0gzgeA9ltTj78hc3drJcXEVbEjNa9ILkyF1aXFSJS6mz2ZYTNtJ8lK2C0pGgzLCTczlgNqyF6V7NzBICPqCCL8kLbnokm620PNn2jmmehWVEw_BomJtZ_vQhBjOuzRuX-w5Gq-VV3tLuqBzOKYH4rv5W3b60ttmodKEKa6DoHrkkYwGRkL822sR_oA92kacqO7XENSwrtzGyVYxgTuU4BsojqzbPGrwEE_Cvte3-DhWP9PDhvt9C007-Gq3aO5YtDVGVNOJV9C85MoJvGqb1jIj7PsQIieCAR1rNHEn4CNSVr1s=")
SESSION = os.environ.get("1BJWap1sBu3aSB8eGT4ddh4FaopI2bozZ4wIEQW8M8Nz0r1sY0gzgeA9ltTj78hc3drJcXEVbEjNa9ILkyF1aXFSJS6mz2ZYTNtJ8lK2C0pGgzLCTczlgNqyF6V7NzBICPqCCL8kLbnokm620PNn2jmmehWVEw_BomJtZ_vQhBjOuzRuX-w5Gq-VV3tLuqBzOKYH4rv5W3b60ttmodKEKa6DoHrkkYwGRkL822sR_oA92kacqO7XENSwrtzGyVYxgTuU4BsojqzbPGrwEE_Cvte3-DhWP9PDhvt9C007-Gq3aO5YtDVGVNOJV9C85MoJvGqb1jIj7PsQIieCAR1rNHEn4CNSVr1s=")
token = os.environ.get("6727350821:AAHI3NPCG24F4NdPZ9dCcsem1AN2QHLBGqs")
sython = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()


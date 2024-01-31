from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""» ʜᴇʏ⚡️{msg.from_user.mention}  ⚡️,
 ɪ ᴀᴍ⚡️{me2}⚡️,
» ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴘʏᴛʜᴏɴ ʟɪʙʀᴀʀʏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ꜰᴏʀ.
» ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴘ, ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ: [⚡️𝗦𝗛𝗜𝗩𝗔𝗡𝗦𝗛-𝗫𝗗⚡️](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="⚡𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐄 𝐒𝐓𝐑𝐈𝐍𝐆⚡", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("⚡️𝗦𝗨𝗣𝗣𝗢𝗥𝗧⚡️", url="https://t.me/MASTIWITHFRIENDSX"),
                    InlineKeyboardButton("⚡️𝗦𝗛𝗜𝗩𝗔𝗡𝗦𝗛-𝗫𝗗⚡️", url="https://t.me/SHIVANSH39")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )

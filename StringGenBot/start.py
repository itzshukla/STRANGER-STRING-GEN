from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from config import START_IMG, OWNER_ID, SUPPORT_CHAT, UPDATE_CHANNEL

# Custom Filters
def filter_cmd(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter_cmd("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention

    START_TXT = f"""**» ʜᴇʏ  {msg.from_user.mention}  ✤,

» ɪ ᴀᴍ {me2},

» ᴀɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

» ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴘʏᴛʜᴏɴ ʟɪʙʀᴀʀʏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ꜰᴏʀ.

» ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴘ, ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ !**"""

    START_BTN = [
        [InlineKeyboardButton("⌨️ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ", callback_data="generate")],
        [
            InlineKeyboardButton("💌 sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
            InlineKeyboardButton("💻 ᴏᴡɴᴇʀ", user_id=OWNER_ID),
        ],
        [InlineKeyboardButton("📘 ɢᴜɪᴅᴇ", callback_data="guide")]
    ]

    await bot.send_photo(
        chat_id=msg.chat.id,
        photo=START_IMG,
        caption=START_TXT,
        reply_markup=InlineKeyboardMarkup(START_BTN),
    )


GUIDE_TXT = """**✦ ʙᴀsɪᴄ ᴄᴏᴍᴍᴀɴᴅs

➻ ᴛʏᴘᴇ /gen ᴏʀ ᴛᴀᴘ ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ ғᴏʀ ɢᴇɴ sᴇssɪᴏɴ.

➻ ᴛʏᴘᴇ /ping ᴄʜᴇᴄᴋ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ

➻ ᴛʏᴘᴇ /stats ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ʙᴏᴛ sᴛᴀᴛs (ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴜsᴇ)

➻ ᴛʏᴘᴇ /broadcast ᴛᴏ sᴇɴᴅ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜsᴇʀs + ᴄʜᴀᴛs (ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴜsᴇ)

⦿ ᴊᴏɪɴ sᴜᴘᴘᴏʀᴛ ғᴏʀ ᴍᴏʀᴇ ᴜᴘᴅᴀᴛᴇs.**"""


@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    data = query.data

    if data == "guide":
        await query.message.edit_text(
            text=GUIDE_TXT,
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("💌 sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
                    InlineKeyboardButton("🪧 ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/{UPDATE_CHANNEL}"),
                ],
                [InlineKeyboardButton("⬅️ ʙᴀᴄᴋ", callback_data="start_menu")]
            ])
        )

    elif data == "start_menu":
        me2 = (await client.get_me()).mention

        START_TXT = f"""**» ʜᴇʏ  {query.from_user.mention}  ✤,

» ɪ ᴀᴍ {me2},

» Aɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

» ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴘʏᴛʜᴏɴ ʟɪʙʀᴀʀʏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ꜰᴏʀ.

» ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴘ, ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ !**"""

        START_BTN = [
            [InlineKeyboardButton("⌨️ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ", callback_data="generate")],
            [
                InlineKeyboardButton("💌 sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
                InlineKeyboardButton("💻 ᴏᴡɴᴇʀ", user_id=OWNER_ID),
            ],
            [InlineKeyboardButton("📘 ɢᴜɪᴅᴇ", callback_data="guide")]
        ]

        try:
            await query.message.edit_caption(
                caption=START_TXT,
                reply_markup=InlineKeyboardMarkup(START_BTN)
            )
        except:
            await query.message.edit_text(
                text=START_TXT,
                reply_markup=InlineKeyboardMarkup(START_BTN)
            )

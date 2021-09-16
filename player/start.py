from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from config import SOURCE_CODE, ASSISTANT_NAME, SUPPORT_GROUP, UPDATES_CHANNEL, BOT_USERNAME
from plugins.tr import *
from pyrogram.errors import MessageNotModified

@Client.on_message(filters.command("start"))
async def start(client, message):
   buttons = [
    [
        InlineKeyboardButton(
            text="༒ 𝙰𝙳𝙳 𝚅𝙰𝙻𝚃 𝙰𝙾𝙸 PLAYER 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 ༒",url="t.me/VALTAOIVCPLAYERBOT?startgroup=true"
        ),
    ],
    [
        InlineKeyboardButton(
          text="༺ 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 & 𝙷𝙴𝙻𝙿 ༻", callback_data="help_back"
        ),
    ],
    [
        InlineKeyboardButton(
          text="༄ 𝚄𝙿𝙳𝙰𝚃𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ༄", url="https://t.me/PigasusUpdates"
        ),
      
        InlineKeyboardButton(
          text="★ 𝙲𝙷𝙴𝙲𝙺 𝙼𝚈 𝙵𝚁𝙸𝙴𝙽𝙳 ★", url="http://t.me/VALTAOITHEBOT"
        ),
    ],
         
    [
       InlineKeyboardButton(
           text="✫ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝚃 ✫", url="https://t.me/PigasusSupport"
         ),
    ],
    [
      InlineKeyboardButton(
           text="彡 𝙼𝚈 𝙾𝚆𝙽𝙴𝚁 彡", url="https://t.me/Rohith_no_1"
         ),
    ],
    [
        InlineKeyboardButton(
          text="༆ 𝚜𝚘𝚞𝚛𝚌𝚎 ༆", callback_data="source_"
        ),
     
    ],
]


   reply_markup = InlineKeyboardMarkup(buttons)
   if message.chat.type == 'private':
       await message.reply_text(
          START_TEXT,
          reply_markup=reply_markup
       )
   else:
      await message.reply(f"**@Crimsonflashs is Alive! ✨**")

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("Bᴀᴄᴋ", callback_data="start"),
                InlineKeyboardButton ("Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/Pigasussupport"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="about":
        buttons = [
            [
                InlineKeyboardButton("Bᴀᴄᴋ", callback_data="start"),
                InlineKeyboardButton ("Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/pigasussupport"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                ABOUT_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="devs":
        buttons = [
    [
        InlineKeyboardButton(
            text="༒ 𝙰𝙳𝙳 𝚅𝙰𝙻𝚃 𝙰𝙾𝙸 PLAYER 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 ༒",url="t.me/VALTAOIVCPLAYERBOT?startgroup=true"
        ),
    ],
    [
        InlineKeyboardButton(
          text="༺ 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 & 𝙷𝙴𝙻𝙿 ༻", callback_data="help_back"
        ),
    ],
    [
        InlineKeyboardButton(
          text="༄ 𝚄𝙿𝙳𝙰𝚃𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ༄", url="https://t.me/PigasusUpdates"
        ),
      
        InlineKeyboardButton(
          text="★ 𝙲𝙷𝙴𝙲𝙺 𝙼𝚈 𝙵𝚁𝙸𝙴𝙽𝙳 ★", url="http://t.me/VALTAOITHEBOT"
        ),
    ],
         
    [
       InlineKeyboardButton(
           text="✫ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝚃 ✫", url="https://t.me/PigasusSupport"
         ),
    ],
    [
      InlineKeyboardButton(
           text="彡 𝙼𝚈 𝙾𝚆𝙽𝙴𝚁 彡", url="https://t.me/Rohith_no_1"
         ),
    ],
    [
      InlineKeyboardButton(
          text="༆ 𝚜𝚘𝚞𝚛𝚌𝚎 ༆", callback_data="source_"
        ),
     
    ],
]


        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                DEVS_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="start":
        buttons = [
    [
        InlineKeyboardButton(
            text="༒ 𝙰𝙳𝙳 𝚅𝙰𝙻𝚃 𝙰𝙾𝙸 PLAYER 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 ༒",url="t.me/VALTAOIVCPLAYERBOT?startgroup=true"
        ),
    ],
    [
        InlineKeyboardButton(
          text="༺ 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 & 𝙷𝙴𝙻𝙿 ༻", callback_data="help_back"
        ),
    ],
    [
        InlineKeyboardButton(
          text="༄ 𝚄𝙿𝙳𝙰𝚃𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ༄", url="https://t.me/PigasusUpdates"
        ),
      
        InlineKeyboardButton(
          text="★ 𝙲𝙷𝙴𝙲𝙺 𝙼𝚈 𝙵𝚁𝙸𝙴𝙽𝙳 ★", url="http://t.me/VALTAOITHEBOT"
        ),
    ],
         
    [
       InlineKeyboardButton(
           text="✫ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝚃 ✫", url="https://t.me/PigasusSupport"
         ),
    ],
    [
      InlineKeyboardButton(
           text="彡 𝙼𝚈 𝙾𝚆𝙽𝙴𝚁 彡", url="https://t.me/Rohith_no_1"
         ),
    ],
    [
      InlineKeyboardButton(
          text="༆ 𝚜𝚘𝚞𝚛𝚌𝚎 ༆", callback_data="source_"
        ),
     
    ],
]


        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                START_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

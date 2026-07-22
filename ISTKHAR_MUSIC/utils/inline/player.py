from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def player_markup(videoid: str, user_id: int):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("⏮", callback_data=f"prev|{videoid}"),
                InlineKeyboardButton("⏸", callback_data=f"pause|{videoid}"),
                InlineKeyboardButton("▶️", callback_data=f"resume|{videoid}"),
                InlineKeyboardButton("⏭", callback_data=f"skip|{videoid}"),
                InlineKeyboardButton("⏹", callback_data=f"stop|{videoid}"),
            ],
            [
                InlineKeyboardButton("⏪ 20s", callback_data=f"seekback|{videoid}"),
                InlineKeyboardButton("🔁", callback_data=f"loop|{videoid}"),
                InlineKeyboardButton("🔀", callback_data=f"shuffle|{videoid}"),
                InlineKeyboardButton("20s ⏩", callback_data=f"seekforward|{videoid}"),
            ],
            [
                InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ", url="https://t.me/YourBotUsername?startgroup=true"),
                InlineKeyboardButton("✖ ᴄʟᴏꜱᴇ", callback_data="close"),
            ]
        ]
    )
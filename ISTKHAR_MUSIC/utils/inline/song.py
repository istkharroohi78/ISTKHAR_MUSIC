from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def song_markup(videoid: str, user_id: int = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="▶️ Play",
                callback_data=f"play_{videoid}"
            ),
            InlineKeyboardButton(
                text="📥 Download",
                callback_data=f"download_{videoid}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🔁 Replay",
                callback_data=f"replay_{videoid}"
            ),
            InlineKeyboardButton(
                text="📊 Info",
                callback_data=f"info_{videoid}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❌ Close",
                callback_data="close"
            )
        ],
    ]

    return InlineKeyboardMarkup(buttons)
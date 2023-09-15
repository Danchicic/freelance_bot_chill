from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon import countries


def choose_country_kb() -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []
    for country in countries:
        buttons.append(InlineKeyboardButton(text=country, callback_data=country))
    kb_builder.row(*buttons, width=2)
    return kb_builder.as_markup()

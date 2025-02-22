from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main =  ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Каталог магазинов"), KeyboardButton(text="Каталог продуктов")],
        [KeyboardButton(text="Корзина продуктов")]
    ], resize_keyboard=True, input_field_placeholder="Выберите пункт меню...")
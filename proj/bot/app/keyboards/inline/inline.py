from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

store_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Магнит", callback_data="store_magnit")],
        [InlineKeyboardButton(text="Пятёрочка", callback_data="store_pyatyorochka")],
        # [InlineKeyboardButton(text="Семишагофф", callback_data="store_semishagof")],
        [InlineKeyboardButton(text="Ашан", callback_data="store_ashan")],
        [InlineKeyboardButton(text="Метро", callback_data="store_metro")],
        [InlineKeyboardButton(text="Окей", callback_data="store_okei")],
        [InlineKeyboardButton(text="Лента", callback_data="store_lenta")],
        [InlineKeyboardButton(text="Дикси", callback_data="store_dixy")],
        # [InlineKeyboardButton(text="Перекрёсток", callback_data="store_perekryostok")]
    ])

product_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Хлеб", callback_data="product_hleb"),
         InlineKeyboardButton(text="Молоко", callback_data="product_moloko"),
         InlineKeyboardButton(text="Масло", callback_data="product_maslo")],
        [InlineKeyboardButton(text="Крупа", callback_data="product_krupa"),
         InlineKeyboardButton(text="Макароны", callback_data="product_makarony"),
         InlineKeyboardButton(text="Яйца", callback_data="product_aitsa")],
        [InlineKeyboardButton(text="Сосиски", callback_data="product_sosiski"),
         InlineKeyboardButton(text="Сыр", callback_data="product_syr"),
         InlineKeyboardButton(text="Мясо", callback_data="product_myaso")]
    ])

add_to_cart_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Хлеб", callback_data="add_to_cart_hleb"),
         InlineKeyboardButton(text="Молоко", callback_data="add_to_cart_moloko"),
         InlineKeyboardButton(text="Масло", callback_data="add_to_cart_maslo")],
        [InlineKeyboardButton(text="Крупа", callback_data="add_to_cart_krupa"),
         InlineKeyboardButton(text="Макароны", callback_data="add_to_cart_makarony"),
         InlineKeyboardButton(text="Яйца", callback_data="add_to_cart_aitsa")],
        [InlineKeyboardButton(text="Сосиски", callback_data="add_to_cart_sosiski"),
         InlineKeyboardButton(text="Сыр", callback_data="add_to_cart_syr"),
         InlineKeyboardButton(text="Мясо", callback_data="add_to_cart_myaso")],
        [InlineKeyboardButton(text="Просмотреть корзину", callback_data="view_cart")],
        #[InlineKeyboardButton(text="Убрать продукт", callback_data="remove_product")]
    ])

cart_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Вернуться к корзине", callback_data="back_to_cart")],
        [InlineKeyboardButton(text="Убрать продукт", callback_data="remove_cart")],
        [InlineKeyboardButton(text="Рассчитать", callback_data="count_cart")]
    ])

remove_cart_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Хлеб", callback_data="remove_hleb"),
         InlineKeyboardButton(text="Молоко", callback_data="remove_moloko"),
         InlineKeyboardButton(text="Масло", callback_data="remove_maslo")],
        [InlineKeyboardButton(text="Крупа", callback_data="remove_krupa"),
         InlineKeyboardButton(text="Макароны", callback_data="remove_makarony"),
         InlineKeyboardButton(text="Яйца", callback_data="remove_aitsa")],
        [InlineKeyboardButton(text="Сосиски", callback_data="remove_sosiski"),
         InlineKeyboardButton(text="Сыр", callback_data="remove_syr"),
         InlineKeyboardButton(text="Мясо", callback_data="remove_myaso")],
        [InlineKeyboardButton(text="Вернуться к корзине", callback_data="back_to_cart")],
    ])



async def inline_store_cart(stores):
    keyboard = InlineKeyboardBuilder()
    for store in stores:
        text = " | ".join(map(str, store)) + "₽"
        cbdata = "view_products_" + store[0]
        keyboard.add(InlineKeyboardButton(text=text, callback_data=cbdata))
    return keyboard.adjust(1).as_markup()
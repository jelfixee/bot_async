import pandas as pd
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from bot.app.keyboards.inline.inline import store_keyboard
from pathlib import Path

store_router = Router()

@store_router.message(F.text == "Каталог магазинов")
async def store_search(message: Message):
    keyboard = store_keyboard
    await message.answer("Выберите магазин", reply_markup=keyboard)


@store_router.callback_query(lambda c: c.data.startswith("store_"))
async def store_button(callback: CallbackQuery):
    await callback.message.delete()
    abs_path = Path("dataframes/products/data.csv").resolve()
    df = pd.read_csv(abs_path, index_col=0).reset_index()
    categories = ["hleb", "moloko", "maslo", "krupa", "makarony", "aitsa", "sosiski", "syr", "myaso"]
    stores = {"magnit": "Магнит", "pyatyorochka": "Пятёрочка", "ashan": "Ашан", "metro": "Метро", "okei": "Окей", "lenta": "Лента", "dixy": "Дикси"}

    store = callback.data.split("_")[-1]

    items_sum = 0

    for category in categories:

        filtered_df = df.loc[(df['store'] == stores[store]) & (df['item_category'] == category)]

        if not filtered_df.empty:

            title = filtered_df.iloc[0].title
            price = filtered_df.iloc[0].price
            items_sum += price

            await callback.message.answer(f"{title}\n{price}₽")

        else:
            await callback.message.answer(f"Все товары не найдены. ({stores[store]}) ")

    await callback.message.answer(f"Всего {round(items_sum, 2)}₽ | {store}")

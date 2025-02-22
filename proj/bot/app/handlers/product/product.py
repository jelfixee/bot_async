import pandas as pd
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from bot.app.keyboards.inline.inline import product_keyboard
from pathlib import Path

product_router = Router()

@product_router.message(F.text == "Каталог продуктов")
async def product_search(message: Message):
    keyboard = product_keyboard
    await message.answer("Выберите раздел", reply_markup=keyboard)


@product_router.callback_query(lambda c: c.data.startswith("product_"))
async def item_button(callback: CallbackQuery):
    await callback.message.delete()
    abs_path = Path("dataframes/products/data.csv").resolve()
    df = pd.read_csv(abs_path, index_col=0).reset_index()
    product = callback.data.split("_")[-1]

    sought_series = df.set_index("item_category").sort_values(by=["price", "store"]).loc[product]  # not right

    median = sought_series.price.median()
    median_four_items = sought_series.price.iloc[:4].median()

    for index in range(4):
        item = sought_series.iloc[index]

        item_store = item.store
        price = item.price
        item_title = item.title

        await callback.message.answer(f"{item_title}\n\n{price}₽ | {item_store}")

    await callback.message.answer(
        text=f"Медиана по всем ценам: {round(median, 2)}₽\nМедиана по 4-м ценам: {round(median_four_items, 2)}₽")

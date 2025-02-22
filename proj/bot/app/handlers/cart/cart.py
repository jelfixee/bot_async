from aiogram.filters.callback_data import CallbackData

from bot.dataframes.users.users import *
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from bot.app.keyboards.inline.inline import cart_keyboard, remove_cart_keyboard, inline_store_cart, add_to_cart_keyboard

cart_router = Router()

class CartCbData(CallbackData, prefix="view_products"):
    dictionary: dict

@cart_router.message(F.text == "Корзина продуктов")
async def add_search(message: Message):
    keyboard = add_to_cart_keyboard
    await message.answer(text="Выберите продукт", reply_markup=keyboard)

@cart_router.callback_query(lambda c: c.data == 'view_cart')
async def view_cart(callback: CallbackQuery):

    users = read_users()
    user_id = callback.from_user.id

    try:
        cart = users.set_index("user_id").loc[user_id].dropna().keys()

    except:
        add_user(user_id)
        cart = users.set_index("user_id").loc[user_id].dropna().keys()

    if cart.empty:
        await callback.message.answer(text="Ваша корзина пуста.")

    else:
        keyboard = cart_keyboard
        await callback.message.answer(text=f"Ваша корзина:\n{"\n".join(cart)}\nВыберите продукт который хотите удалить", reply_markup=keyboard)


@cart_router.callback_query(lambda c: c.data.startswith('add_to_cart_'))
async def add_cart(callback: CallbackQuery):

    chat_id = callback.message.chat.id
    users = read_users()
    user_id = callback.from_user.id
    product = callback.data.split('_')[-1]

    try:
        put_product(user_id, product)

    except:
        add_user(user_id)
        put_product(user_id, product)

    await callback.message.answer(text=f"Вы добавили: {product}")


@cart_router.callback_query(lambda c: c.data == 'back_to_cart')
async def back_to_cart(callback: CallbackQuery):

    keyboard = add_to_cart_keyboard
    users = read_users()
    user_id = callback.from_user.id

    try:
        cart = users.set_index("user_id").loc[user_id].dropna().keys()

    except:
        add_user(user_id)
        cart = users.set_index("user_id").loc[user_id].dropna().keys()

    if not cart.empty:
        await callback.message.answer(text="Выберите продукт", reply_markup=keyboard)

    else:
        await callback.message.answer(text="Ваша корзина пуста.")

@cart_router.callback_query(lambda c: c.data == "remove_cart")
async def answer_remove_cart(callback:CallbackQuery):
    await callback.message.answer(text="Уберите продукт из корзины", reply_markup=remove_cart_keyboard)

@cart_router.callback_query(lambda c: c.data.startswith('remove_'))
async def remove_product(callback: CallbackQuery):
    await callback.message.delete()
    users = read_users()
    user_id = callback.from_user.id
    product = callback.data.split('_')[-1]

    try:
        cart = users.set_index("user_id").loc[user_id].dropna().keys()

    except:
        add_user(user_id)
        cart = users.set_index("user_id").loc[user_id].dropna().keys()

    if product in cart:
        delete_product(user_id, product)
        await callback.message.answer(text=f"Вы удалили {product} из корзины.", )

    else:
        await callback.message.answer(text="Продукт не найден в корзине.")

@cart_router.callback_query(lambda c: c.data == "count_cart")
async def count_cart(callback: CallbackQuery):
    users = read_users()
    user_id = callback.from_user.id
    products = users.set_index("user_id").loc[user_id].dropna().keys()
    stores = {"magnit": "Магнит", "pyatyorochka": "Пятёрочка", "ashan": "Ашан", "metro": "Метро", "okei": "Окей", "lenta": "Лента"}

    abs_path = Path("dataframes/products/data.csv").resolve()
    df = pd.read_csv(abs_path, index_col=0).reset_index()

    ###

    #   result: sorted list of stores and its price sum => button that gives product and all about it

    ###

    store_dict = {}

    for store in stores:

        items_sum = 0
        is_valid = True
        cart = []

        for product in products:
            # try:
            item = df.loc[(df['store'] == stores[store]) & (df['item_category'] == product)].iloc[0]

            title = item.title
            price = float(item.price)
            items_sum += float(price)

            cart.append((title, price))
            # await callback.message.answer(f"{title}\n{price}₽")

            # except:
            #     is_valid = False
            #     await callback.message.answer(f"В {store} отсутствует {product}")

        store_dict[(store, round(items_sum, 2))] = cart

    lst = sorted(list(store_dict.keys()), key=lambda x: x[1], reverse=True)
    CartCbData.dictionary = store_dict
    await callback.message.answer(text="Выберите магазин, для отображения продуктов", reply_markup=await inline_store_cart(lst))

        # if is_valid:
        #     await callback.message.answer(f"Всего: {items_sum}₽ | {store}")
        #
        # else:
        #     await callback.message.answer(f"Отсутсвует некоторые продукты")

@cart_router.callback_query(lambda c: c.data.startswith("view_products_"))
async def view_products(callback: CallbackQuery):
    store = callback.data.split("_")[-1]
    for store_name, price in CartCbData.dictionary.keys():
        if store == store_name:
            products_list = CartCbData.dictionary[(store, price)]
            break

    for product in products_list:
        title, price = product
        await callback.message.answer(text=f"{title}\n{price}₽")


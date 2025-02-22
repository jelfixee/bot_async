import logging
import asyncio
from aiogram import Bot, Dispatcher
from bot.app.handlers.start.start import start_router
from bot.app.handlers.store.store import store_router
from bot.app.handlers.cart.cart import cart_router
from bot.app.handlers.product.product import product_router
from bot.ttoken import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(start_router)
    dp.include_router(store_router)
    dp.include_router(product_router)
    dp.include_router(cart_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())

    except KeyboardInterrupt:
        print("Exit")

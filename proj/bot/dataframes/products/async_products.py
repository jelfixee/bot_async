import os
from datetime import datetime
import pandas as pd
import asyncio

products = []

async def retry(store, link, proxy, attemps=5, delay=3):
    while attemps:
        try:
            response = await store["func"](link, proxy)
            print(f"[INFO] succeeded | {store["name"]} | {link}")
            return response

        except Exception as e:
            print(f"[INFO] retry = {attemps} => {link} | {store["name"]} | {e}")
            if attemps:
                await asyncio.sleep(delay)
                attemps -= 1
            else:
                raise

async def get_response(item_category, store, link, proxy):
    price, title = await retry(store, link, proxy)
    cur_t = datetime.now()
    date = cur_t.strftime("%d.%m.%Y")
    sub_df = pd.DataFrame([item_category, price, price/100, title, date, cur_t, store["name"]],
                          columns=["product_category", "price", "float_price", "title", "date", "time", "store"])
    products.append(sub_df)

async def gather_data():
    tasks = []
    for store in stores:
        for item_category, link in store["items"].items():
            task = asyncio.create_task(get_response(item_category, store, link, proxy))
            tasks.append(task)
    await asyncio.gather(*tasks)

async def main():
    asyncio.run(gather_data())

    try:
        main_df = pd.read_csv("PRODUCTS.CSV_PATH") # REMEMBER TO ADD PATH
        os.remove("data.csv")
    except FileNotFoundError:
        main_df = pd.DataFrame(columns=["product", "price", "title", "date", "time", "store"])

    for sub_df in products:
        main_df = pd.concat([main_df, sub_df])
    main_df.to_csv("data.csv", index=False)


if __name__ == "__main__":
    main()
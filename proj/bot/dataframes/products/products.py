import pandas as pd
from proj.bot.app.config.config import stores
import time
from datetime import datetime
import schedule
import os


def retry(store, link, attemps=5, delay=3):
    while attemps:
        try:
            response = store["func"](link)
            print(f"[INFO] succeeded | {store["name"]} | {link}")
            return response


        except Exception as e:
            print(f"[INFO] retry = {attemps} => {link} | {store["name"]} | {e}")

            if attemps:
                time.sleep(delay)
                attemps -= 1

            else:
                raise

def fetch_data(df):
    current_t = datetime.now().strftime("%d.%m.%Y")

    for store in stores:

        for item_category, link in store["items"].items():

            try:
                response = retry(store, link)

                for pare in response:
                    store_name = store["name"]
                    price = pare[0]
                    title = pare[1]
                    # settled_df = df.set_index("title")

                    # if title in df.title.unique() and price != settled_df.loc["title"].price:
                    #     settled_df.loc[title, "price"] = price
                    #     settled_df.loc[title, "date"] = current_t
                    #     df = settled_df.reset_index()
                    #
                    # elif title in df.title.unique() and price == settled_df.loc[title].price:
                    #     continue

                    # else:
                    #     df = df._append({"item_category": item_category, "price": price, "title": title, "date": current_t, "store": store_name}, ignore_index=True)

                    df = df._append({"item_category": item_category, "price": price, "title": title, "date": current_t, "store": store_name}, ignore_index=True)
            except:
                continue

    return df

def collect_data():
    try:
        df = pd.read_csv("data.csv")
        df = fetch_data(df)
        os.remove("data.csv")
        df.to_csv('data.csv', index=False)


    except FileNotFoundError:
        columns = ["title", "item_category", "price", "date", "store"]
        df = pd.DataFrame(columns=columns)
        df = fetch_data(df)
        df.to_csv('data.csv', index=False)

    # current_t = datetime.now().strftime("%d.%m.%Y")
    #
    # for store in stores:
    #
    #     for item_category, link in store["items"].items():
    #
    #         try:
    #             response = retry(store, link)
    #
    #             for pare in response:
    #
    #                 store_name = store["name"]
    #                 price = pare[0]
    #                 title = pare[1]
    #                 # settled_df = df.set_index("title")
    #
    #                 # if title in df.title.unique() and price != settled_df.loc["title"].price:
    #                 #     settled_df.loc[title, "price"] = price
    #                 #     settled_df.loc[title, "date"] = current_t
    #                 #     df = settled_df.reset_index()
    #                 #
    #                 # elif title in df.title.unique() and price == settled_df.loc[title].price:
    #                 #     continue
    #
    #                 # else:
    #                 #     df = df._append({"item_category": item_category, "price": price, "title": title, "date": current_t, "store": store_name}, ignore_index=True)
    #
    #                 df = df._append({"item_category": item_category, "price": price, "title": title, "date": current_t, "store": store_name}, ignore_index=True)
    #
    #
    #         except:
    #             continue


if __name__ == "__main__":
    collect_data()
    # schedule.every().day.at("04:00").do(collect_data)
    print("System has been launched")

    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)

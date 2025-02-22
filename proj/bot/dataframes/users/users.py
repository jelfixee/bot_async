import pandas as pd
import os
from pathlib import Path

user_path = Path("../bot/dataframes/users/users.csv").resolve()
# user_path = Path("../users/users.csv").resolve()

def read_users():
    return pd.read_csv(user_path)


def create_users(path):
    columns = ["user_id", "hleb", "moloko", "maslo", "krupa", "makarony", "aitsa", "sosiski", "syr", "myaso"]
    users = pd.DataFrame(columns=columns)
    users.to_csv(path, index=False)


def save_changes(users):
    os.remove(user_path)
    users.to_csv(user_path, index=False)


def add_user(user_id):
    users = read_users()
    users = users._append({"user_id": user_id, "hleb": None, "moloko": None, "maslo": None, "krupa": None, "makarony": None, "aitsa": None, "sosiski": None, "syr": None, "myaso": None}, ignore_index=True)
    save_changes(users)


def put_product(user_id, item):
    users = read_users()
    settled_users = users.set_index("user_id")
    settled_users.loc[user_id, item] = 1
    users = settled_users.reset_index()
    save_changes(users)


def delete_product(user_id, item):
    users = read_users()
    settled_users = users.set_index("user_id")
    settled_users.loc[user_id, item] = None
    users = settled_users.reset_index()
    save_changes(users)
